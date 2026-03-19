import random
import tkinter as tk
from tkinter import messagebox

massive = ["💵", "💶", "💷", "💰", "🏧", "🎰", "🍔"]
Balance = 1000000

def play():
    global Balance
    if Balance < 10000:
        messagebox.showinfo("Game Over", "Insufficient balance!")
        return

    Balance -= 10000
    R1 = random.choice(massive)
    R2 = random.choice(massive)
    R3 = random.choice(massive)

    slot1.config(text=R1)
    slot2.config(text=R2)
    slot3.config(text=R3)

    if R1 == R2 == R3:
        result.config(text="🎉 BIG WIN!")
        Balance += 30000
    elif R1 == R2 or R2 == R3 or R1 == R3:
        result.config(text="✨ WIN!")
        Balance += 15000
    else:
        result.config(text="😢 You lost!")

    balance_label.config(text=f"Balance: {Balance}")

root = tk.Tk()
root.title("Emoji Slot Machine")

balance_label = tk.Label(root, text=f"Balance: {Balance}", font=("Arial", 14))
balance_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

slot1 = tk.Label(frame, text="❓", font=("Arial", 40))
slot1.pack(side="left", padx=10)
slot2 = tk.Label(frame, text="❓", font=("Arial", 40))
slot2.pack(side="left", padx=10)
slot3 = tk.Label(frame, text="❓", font=("Arial", 40))
slot3.pack(side="left", padx=10)

result = tk.Label(root, text="", font=("Arial", 16))
result.pack(pady=10)

play_button = tk.Button(root, text="Spin", command=play, font=("Arial", 14))
play_button.pack()

root.mainloop()