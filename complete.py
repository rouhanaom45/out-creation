import pyautogui
import random
import time
import subprocess
import string

def random_click(x1, y1, x2, y2):
    """Performs a random click within the given rectangular area."""
    x = random.randint(x1, x2)
    y = random.randint(y1, y2)
    pyautogui.moveTo(x, y, duration=random.uniform(0.3, 0.7))
    pyautogui.click()
    print(f"Clicked at ({x}, {y})")

def random_sleep(min_sec, max_sec):
    """Sleeps for a random time between min_sec and max_sec seconds."""
    sleep_time = random.uniform(min_sec, max_sec)
    time.sleep(sleep_time)
    print(f"Slept for {sleep_time:.2f} seconds")

def press_key_random_times(key, min_times, max_times, min_sleep, max_sleep):
    """Presses a key randomly between min_times and max_times, with random sleep in between."""
    times = random.randint(min_times, max_times)
    for _ in range(times):
        pyautogui.press(key)
        random_sleep(min_sleep, max_sleep)
    return times  # Return the number of times pressed

def generate_random_name(min_length, max_length):
    """Generates a random name where each consonant is followed by a vowel."""
    length = random.randint(min_length, max_length)
    consonants = "bcdfghjklmnpqrstvwxyz"
    vowels = "aeiou"
    name = "".join(random.choice(consonants) + random.choice(vowels) for _ in range(length // 2))
    return name[:length]  # Ensure the length matches exactly

def type_like_human(text):
    """Types text with a random human-like delay between keystrokes."""
    for char in text:
        pyautogui.write(char, interval=random.uniform(0.1, 0.3))
    print(f"Typed: {text}")

# Function to click at specified coordinates
def click_at(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()
time.sleep(4)
# Function to generate a random word of given length
def random_word(min_len, max_len):
    length = random.randint(min_len, max_len)
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

time.sleep(1)


random_click(71, 180, 81, 192)
random_sleep(3, 4)
random_click(1139, 175, 1174, 190)
time.sleep(1)
random_click(1151, 223, 1301, 236)
random_sleep(4, 5)
random_click(515, 424, 659, 429)
random_sleep(1, 1.5)
subprocess.run(["python3", "click.py"])
time.sleep(1)
# Type a random name (7-9 characters)
name1 = generate_random_name(7, 9)
type_like_human(name1)

random_sleep(0.7, 1)
random_click(65, 287, 239, 480)
time.sleep(0.5)
press_key_random_times('down', 13, 15, 0.35, 0.5)
random_click(917, 425, 1013, 433)
random_sleep(4, 5)
random_click(10, 310, 62, 493)
time.sleep(2)
pyautogui.press('down')
time.sleep(1)
subprocess.run(["python3", "file.py"])
random_sleep(3.5, 3.9)
random_click(84, 387, 616, 517)
random_sleep(0.6, 0.9)

subprocess.run(["python3", "generator1.py"])
time.sleep(1)
subprocess.run(["python3", "save-zara.py"])
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
random_sleep(1, 2)
random_click(4, 340, 9, 426)
random_sleep(0.5, 0.9)
for _ in range(random.randint(7, 9)):
    pyautogui.press('up')
    time.sleep(random.uniform(0.3, 0.4))

random_sleep(1, 2)
random_click(121, 285, 261, 290)
random_sleep(1, 1.6)

# Type a random filename (7-9 characters) followed by a random extension
name3 = generate_random_name(7, 9) + random.choice([".py", ".py", ".py"])
type_like_human(name3)

random_sleep(1, 2)
random_click(1218, 282, 1336, 295)
time.sleep(1.5)
random_click(1218, 282, 1336, 295)
random_sleep(4, 5)
random_click(787, 547, 886, 557)
time.sleep(1.5)
random_click(787, 547, 886, 557)
random_sleep(5, 6)
pyautogui.press('enter')
time.sleep(1.5)
random_click(826, 228, 885, 236)
random_sleep(4, 5)

for _ in range(random.randint(3, 3)):
    pyautogui.press('down')
    time.sleep(random.uniform(0.3, 0.4))
time.sleep(1)

random_click(90, 410, 352, 418)
random_sleep(1.3, 1.8)
random_click(91, 439, 334, 451)
random_sleep(4, 5)

for _ in range(random.randint(22, 25)):
    pyautogui.press('down')
    time.sleep(random.uniform(0.3, 0.4))
time.sleep(1)

random_click(401, 228, 405, 232)
random_sleep(1.3, 1.8)
random_click(406, 423, 435, 433)

random_sleep(4, 5)
random_click(341, 229, 403, 238)
random_sleep(3, 4)

subprocess.run(["python3", "set-workflow.py"])
random_sleep(3, 4)

subprocess.run(["python3", "generator2.py"])
time.sleep(1)
subprocess.run(["python3", "save-workflow.py"])
time.sleep(1)
pyautogui.hotkey('ctrl', 'v')
random_sleep(1, 2)
random_click(4, 317, 8, 498)
random_sleep(0.5, 0.9)
for _ in range(random.randint(6, 7)):
    pyautogui.press('up')
    time.sleep(random.uniform(0.3, 0.4))

random_sleep(1, 2)
random_click(294, 283, 445, 291)
random_sleep(1, 1.6)
pyautogui.hotkey('ctrl', 'a')
time.sleep(random.uniform(0.4, 0.7))
pyautogui.press('delete')
time.sleep(random.uniform(0.7, 0.95))
name4 = generate_random_name(7, 9) + random.choice([".yml", ".yml", ".yml"])
type_like_human(name4)

random_sleep(1, 2)
random_click(1220, 283, 1326, 295)
time.sleep(1.5)
random_click(1220, 283, 1326, 295)
random_sleep(4, 5)
random_click(789, 547, 890, 559)
time.sleep(1.5)
random_click(789, 547, 890, 559)
random_sleep(5, 6)
pyautogui.press('enter')
time.sleep(1.5)
