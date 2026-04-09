import pyautogui
import pyperclip
import keyboard
import time

FILE = "vnx.txt"

print("Focus your window (like Minecraft).")
print("Press K to start, P to stop.")

# --- Read file ---
with open(FILE) as f:
    lines = [line.strip() for line in f if line.strip()]

# --- Wait for K key ---
keyboard.wait('k')
print("K pressed! Starting...")

# --- Open chat (if using Minecraft) ---
pyautogui.press('t')
time.sleep(0.1)

# --- Paste loop ---
while True:
    for msg in lines:
        pyperclip.copy(msg)
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('enter')
        time.sleep(0.01)

        if keyboard.is_pressed('p'):
            print("Stopped!")
            exit()