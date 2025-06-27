import pyautogui
import time
import os
import random




def random_click(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x + random.uniform(-2, 2), y + random.uniform(-2, 2), duration=random.uniform(0.1, 0.4))
    pyautogui.click()


time.sleep(1.5)

button_images = [
    'finish0_button.png'
]

max_attempts = 12

for image in button_images:
    if not os.path.isfile(image):
        print(f"Error: The image file '{image}' does not exist.")

for attempt in range(max_attempts):
    print(f"Attempt {attempt + 1} of {max_attempts}: Attempting to detect verification buttons...")
    time.sleep(2)

    for image in button_images:
        try:
            print(f"Trying to detect: {image}")
            location = pyautogui.locateOnScreen(image, confidence=0.8)
        except Exception as e:
            print(f"Error while detecting '{image}': {e}")
            location = None

        if location:
            time.sleep(1)
            print(f"'{image}' clicked")
            pyautogui.click(location)
            time.sleep(0.5)
            for _ in range(random.randint(6, 8)):
                pyautogui.press("down")
                time.sleep(0.35)

            time.sleep(1)
            random_click((804, 518), (872, 532))
            time.sleep(random.uniform(1.0, 1.5))
            exit()

    print("No buttons detected in this attempt. Pressing Down Arrow key to continue...")
    time.sleep(1)

print("Maximum detection attempts reached. Exiting...")
