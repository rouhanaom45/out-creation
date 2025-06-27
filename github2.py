# main_script.py
import pyautogui
import time
import subprocess
import random


def random_click_in_rectangle(top_left, bottom_right):
    x = random.randint(top_left[0], bottom_right[0])
    y = random.randint(top_left[1], bottom_right[1])
    pyautogui.moveTo(x, y, duration=random.uniform(0.2, 0.6))
    pyautogui.click()


def detect_web_button(script_name):
    """Run an external script to detect the web button and keep trying until successful."""
    while True:
        # Start the external detection script
        process = subprocess.Popen(['python3', script_name])
        process.wait()  # Wait for it to finish

        if process.returncode == 0:  # Success code indicates the button was found
            print(f"Web button detected and clicked by {script_name}. Proceeding with tasks...")
            return  # Exit the loop and proceed to next tasks
        else:
            print(f"Web button not detected by {script_name}. Retrying...")
            time.sleep(6)
                       
def perform_additional_tasks():
    """Define tasks to perform after the web button is detected."""
    print("Performing additional tasks...")
    time.sleep(2)
    pyautogui.click(648, 294)
    time.sleep(1.5) 
    pyautogui.hotkey('ctrl', 'shift', 'tab')
    time.sleep(1.5)
    pyautogui.click(96, 83)
    time.sleep(7)


    print("All tasks completed.")

if __name__ == "__main__":
    # Step 1: Detect the web button via the detection script
    detect_web_button('found1.py')

    # Step 2: Perform additional tasks after the web button is detected
    perform_additional_tasks()
    subprocess.run(["python3", "accept.py"])
    time.sleep(1)
    subprocess.run(["python3", "banner.py"])
    time.sleep(1)
