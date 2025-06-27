import pyautogui
import random
import time
import string
import sys
import subprocess


time.sleep(2)

def generate_password():
    # Ensure at least one character from each category
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("@.,;!:")

    # Fill the rest of the password randomly to meet the length requirement
    all_chars = string.ascii_letters + string.digits + "@.,;!:"
    remaining_chars = random.choices(all_chars, k=random.randint(5, 8))

    # Combine and shuffle to randomize the order
    password = list(lower + upper + digit + special + ''.join(remaining_chars))
    random.shuffle(password)

    return ''.join(password)

def random_click_in_rectangle(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.6))
    pyautogui.click()

def random_human_typing(text):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(random.uniform(0.05, 0.15))

def random_string(length, chars):
    return ''.join(random.choice(chars) for _ in range(length))

# Step 1: Type website and press Enter
time.sleep(1.5)
subprocess.run(["python3", "git1.py"])
time.sleep(1)
# New Step: Detect the tab button using 'copilot_button.png'
try:
    tab_button_location = pyautogui.locateCenterOnScreen('copilot_button.png', confidence=0.8)
    if tab_button_location is not None:
        print("Copilot button detected, clicking at (1309, 264)...")
        pyautogui.click(1311, 174)
        time.sleep(2)
    else:
        print("Tab button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting tab button: {e}")
    print("Proceeding to Step 1...")

time.sleep(1)

# Step 2: Random clicks in one of two rectangles
rect1 = [(69, 320), (219, 536)]
rect2 = [(1132, 313), (1320, 501)]
chosen_rect = random.choice([rect1, rect2])
clicks = random.randint(1, 4)
for _ in range(clicks):
    random_click_in_rectangle(chosen_rect[0], chosen_rect[1])
    time.sleep(random.uniform(1, 2))

# Step 3: Click in specific rectangle
random_click_in_rectangle((1272, 184), (1321, 198))
time.sleep(random.uniform(12, 14))
subprocess.run(["python3", "get-email.py"])
time.sleep(1)
subprocess.run(["python3", "git2.py"])
time.sleep(1)
try:
    cooki_button_location = pyautogui.locateCenterOnScreen('cooki_button.png', confidence=0.8)
    if cooki_button_location is not None:
        print("Cooki button detected, clicking at (1309, 264)...")
        time.sleep(0.7)
        pyautogui.click(cooki_button_location)
        time.sleep(2)
    else:
        print("cooki button not detected, proceeding to Step 1...")
except Exception as e:
    print(f"Error detecting cooki button: {e}")
    print("Proceeding to Step 1...")

time.sleep(1)

# Step 4: Click in another rectangle
random_click_in_rectangle((693, 260), (777, 357))
time.sleep(random.uniform(1, 2))

# Step 5: Press down arrow 3 times with delay
for _ in range(3):
    pyautogui.press('down')
    time.sleep(random.uniform(0.1, 0.3))

# Step 6: Click and write clipboard content
random_click_in_rectangle((817, 163), (1214, 171))
time.sleep(random.uniform(0.5, 1))
pyautogui.hotkey('ctrl', 'v')
time.sleep(random.uniform(0.5, 1))

# Step 7: Click and write random password
random_click_in_rectangle((813, 244), (1199, 254))
time.sleep(random.uniform(0.5, 1))
random_password = generate_password()
random_human_typing(random_password)
time.sleep(random.uniform(1, 2))

# Step 8: Click and write random name
random_click_in_rectangle((813, 359), (1219, 370))
time.sleep(random.uniform(0.5, 1))
name = ''.join(
    random.choice(string.ascii_lowercase) + random.choice('aeiou') for _ in range(random.randint(3, 4))
) + str(random.randint(10, 99))
random_human_typing(name)
time.sleep(random.uniform(2, 3))

random_click_in_rectangle((1272, 235), (1335, 341))
time.sleep(0.6)
for _ in range(4):
    pyautogui.press('down')
    time.sleep(random.uniform(0.1, 0.3))

time.sleep(0.7)

# Step 9: Final click and wait
random_click_in_rectangle((818, 456), (1228, 477))
time.sleep(random.uniform(3.5, 4.5))
random_click_in_rectangle((1273, 203), (1342, 408))
time.sleep(1)

# --------- NEW BUTTON DETECTION SCRIPT ---------
failed_attempts = 0
max_attempts = 10  # Exit after 10 consecutive failures

while True:
    time.sleep(1)

    try:
        button_location = pyautogui.locateCenterOnScreen('pass_button.png', confidence=0.8, grayscale=True)
        if button_location:
            random_click_in_rectangle((818, 456), (1228, 477))
            time.sleep(2)
            failed_attempts = 0  # Reset failure count when button is found
        else:
            failed_attempts += 1  # Increment failure count

    except pyautogui.ImageNotFoundException:
        failed_attempts += 1  # Increment failure count if image is not found

    if failed_attempts >= max_attempts:
        print("Button not found for 10 consecutive attempts. Exiting.")
        sys.exit()  # Fully exit after 10 consecutive failures
