#!/bin/bash

# Install megacmd if not already installed
apt install -y wget
wget https://mega.nz/linux/repo/xUbuntu_20.04/amd64/megacmd-xUbuntu_20.04_amd64.deb
apt install -y ./megacmd-xUbuntu_20.04_amd64.deb
rm megacmd-xUbuntu_20.04_amd64.deb

# Install unzip if not already installed
apt install -y unzip

# Log out if already logged in
mega-logout 2>/dev/null

# Log in to MEGA account
mega-login fouhom223@gmail.com 52981070mM

# File to track downloaded files
DOWNLOADED_LOG="downloaded_files.txt"

# Create downloaded log file if it doesn't exist
touch "$DOWNLOADED_LOG"

# List files in /github-firefox with details
files=$(mega-ls -l /github-firefox 2>/dev/null)

# Check if there are any files
if [ -z "$files" ]; then
    echo "No files found in /github-firefox."
    exit 1
fi

# Create a temporary file for sorting
temp_file=$(mktemp)

# Parse files and filter out already downloaded ones
while IFS= read -r line; do
    # Skip empty lines
    [ -z "$line" ] && continue
    # Skip directories (lines starting with 'd')
    if [[ "$line" =~ ^d ]]; then
        continue
    fi
    # Extract filename (last field) and creation date (second-to-last field)
    filename=$(echo "$line" | awk '{print $NF}')
    cdate=$(echo "$line" | awk '{print $(NF-1)}')
    # Skip invalid filenames or lines without proper format
    if [[ -z "$filename" || "$filename" == *":" || "$filename" == *"github-firefox"* ]]; then
        continue
    fi
    # Check if file is already downloaded
    if ! grep -Fx "$filename" "$DOWNLOADED_LOG" > /dev/null; then
        # Convert date to sortable format (YYYYMMDDHHMMSS)
        sortable_date=$(date -d "$cdate" +%Y%m%d%H%M%S 2>/dev/null)
        if [ -n "$sortable_date" ]; then
            echo "$filename|$sortable_date" >> "$temp_file"
        fi
    fi
done <<< "$files"

# Check if there are any files left to download
if [ ! -s "$temp_file" ]; then
    echo "All files in /github-firefox have already been downloaded or no valid files found."
    rm "$temp_file"
    exit 0
fi

# Sort files by creation date (oldest first)
sort -t'|' -k2 < "$temp_file" > sorted_files.txt

# Get the oldest file (first line after sorting)
oldest_file=$(head -n 1 sorted_files.txt | cut -d'|' -f1)

# Check if oldest_file is empty
if [ -z "$oldest_file" ]; then
    echo "No valid files to download."
    rm "$temp_file" sorted_files.txt
    exit 1
fi

# Download the oldest file
echo "Downloading oldest file: $oldest_file"
mega-get "/github-firefox/$oldest_file" .

# Verify download
if [ -f "$oldest_file" ]; then
    echo "Successfully downloaded $oldest_file"
    # Add to downloaded log
    echo "$oldest_file" >> "$DOWNLOADED_LOG"
else
    echo "Failed to download $oldest_file"
    rm "$temp_file" sorted_files.txt
    exit 1
fi

# Unzip to a temp directory
UNZIPPED_TOP="${oldest_file%.zip}"
mkdir -p "$UNZIPPED_TOP"
unzip -o "$oldest_file" -d "$UNZIPPED_TOP" | grep -Eiv 'inflating|extracting'

if [ $? -ne 0 ]; then
    echo "Error unzipping $oldest_file!"
    rm "$temp_file" sorted_files.txt
    exit 1
fi

echo "Unzipping completed successfully."

# Detect actual Firefox profile folder (must contain prefs.js)
REAL_PROFILE=$(find "$UNZIPPED_TOP" -type f -name "prefs.js" | head -n1 | xargs dirname)

if [ -z "$REAL_PROFILE" ]; then
    echo "Error: Could not find valid Firefox profile folder (missing prefs.js)."
    rm "$temp_file" sorted_files.txt
    exit 1
fi

echo "Detected Firefox profile folder: $REAL_PROFILE"

# Add Firefox preferences and clean up session restore files
cat <<EOF > "$REAL_PROFILE/user.js"
user_pref("browser.sessionstore.resume_from_crash", false);
user_pref("browser.startup.page", 0);
user_pref("browser.startup.homepage_override.mstone", "ignore");
user_pref("browser.tabs.warnOnClose", false);
user_pref("browser.warnOnQuit", false);
user_pref("browser.sessionstore.max_tabs_undo", 0);
EOF

rm -f "$REAL_PROFILE/sessionstore.js" \
      "$REAL_PROFILE/sessionCheckpoints.json" \
      "$REAL_PROFILE/recovery.jsonlz4" \
      "$REAL_PROFILE/recovery.baklz4"

# Set DISPLAY if running in headless or VNC session
export DISPLAY=:1

# Start Firefox with the profile if not already running
if ! pgrep firefox > /dev/null; then
    nohup firefox --no-remote --new-instance --profile "$REAL_PROFILE" --purgecaches &> /dev/null &
    echo "Firefox launched successfully with the new profile."
else
    echo "Firefox is already running."
fi

# Clean up
rm "$temp_file" sorted_files.txt
