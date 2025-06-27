#!/bin/bash


scripts=(
  "save.py"
  "omocaptcha.py"
  "outlook1.py"
  "microsoft.py"
  "outlook2.py"
  "cap-press.py"
  "outlook3.py"
  "upload.py"
)

# Run each script in order
for script in "${scripts[@]}"; do
  echo "Running $script..."
  python3 "$script"
  if [ $? -ne 0 ]; then
    echo "Error: $script failed. Exiting."
    exit 1
  fi
  echo "$script finished successfully."
done

sleep 2
echo "stop now" > /root/failure.txt
sleep 1
