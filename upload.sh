#!/bin/bash

# Install megacmd
apt install -y wget
wget https://mega.nz/linux/repo/xUbuntu_20.04/amd64/megacmd-xUbuntu_20.04_amd64.deb
apt install -y ./megacmd-xUbuntu_20.04_amd64.deb
rm megacmd-xUbuntu_20.04_amd64.deb

# Log out if already logged in
mega-logout 2>/dev/null

# Log in to MEGA account
mega-login fouhom223@gmail.com 52981070mM

# Create part1 folder if it doesn't exist
mega-mkdir /part2 2>/dev/null

# Upload all .txt files starting with "deep" to /part1
for file in deep*.txt; do
    if [ -f "$file" ]; then
        mega-put "$file" /part2
    fi
done
