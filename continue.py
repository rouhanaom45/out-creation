import pyautogui
import time
import random
import subprocess
import pyperclip
import time

time.sleep(1)
pyautogui.hotkey('ctrl', 'shift', 'tab')
time.sleep(1.5)

# Define the rectangular area corners
top_left_x, top_left_y = 803, 359
bottom_right_x, bottom_right_y = 832, 390

# Generate random x and y coordinates within the rectangle
random_x = random.randint(top_left_x, bottom_right_x)
random_y = random.randint(top_left_y, bottom_right_y)

# Move the mouse smoothly to the random position to mimic human behavior
pyautogui.moveTo(random_x, random_y, duration=random.uniform(0.5, 1.2))

# Perform the click
pyautogui.click()

# Wait for a random time between 10 and 12 seconds
time.sleep(random.uniform(1, 2))
text = pyperclip.paste()
for char in text:
    pyautogui.write(char)
    time.sleep(random.uniform(0.3, 0.45))
time.sleep(random.uniform(10, 12))

time.sleep(1)
def random_click_in_rectangle(top_left, bottom_right):
    """Perform a random click within a given rectangular area."""
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.6))
    pyautogui.click()

# Step 1: Perform random click in the first rectangle
random_click_in_rectangle((81, 203), (370, 473))
time.sleep(random.uniform(0.5, 1))

# Step 2: Press down arrow 7 to 9 times with random short delay
for _ in range(random.randint(7, 9)):
    pyautogui.press('down')
    time.sleep(random.uniform(0.5, 0.8))

# Step 3: Perform random click in the second rectangle
random_click_in_rectangle((570, 343), (786, 356))
time.sleep(random.uniform(10, 14))
time.sleep(1)

