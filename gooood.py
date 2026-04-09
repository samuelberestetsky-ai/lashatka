import pyautogui
import time
import keyboard
import pyperclip

print("Press O to start, N to stop...")

keyboard.wait('o')
time.sleep(1)

with open("vnx.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f if line.strip() != ""]

running = True

while running:
    for i, line in enumerate(lines):

        if keyboard.is_pressed('n'):
            print("Stopped!")
            running = False
            break

        # Copy line to clipboard (instant)
        pyperclip.copy(line)

        # Open chat (Shift + T)
        pyautogui.keyDown('shift')
        pyautogui.press('t')
        pyautogui.keyUp('shift')

        # Paste (CTRL + V)
        pyautogui.hotkey('ctrl', 'v')

        pyautogui.press("enter")

        if i == 0:
            pyautogui.press("enter")

        time.sleep(0.0001)  # much smaller dela