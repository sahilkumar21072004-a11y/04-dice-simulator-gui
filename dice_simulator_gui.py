import tkinter as tk
import random

# -------- Dice Logic --------
def roll_dice():
    value = random.randint(1, 6)
    result_label.config(text=f"🎲 {value}")

# -------- GUI Window --------
root = tk.Tk()
root.title("Dice Simulator")
root.geometry("300x300")
root.resizable(False, False)
root.configure(bg="#1e1e1e")

# -------- Title --------
tk.Label(
    root,
    text="🎲 Dice Simulator",
    font=("Arial", 18, "bold"),
    bg="#1e1e1e",
    fg="white"
).pack(pady=20)

# -------- Result Display --------
result_label = tk.Label(
    root,
    text="Roll the Dice!",
    font=("Arial", 24),
    bg="#1e1e1e",
    fg="#4caf50"
)
result_label.pack(pady=30)

# -------- Roll Button --------
tk.Button(
    root,
    text="Roll Dice",
    font=("Arial", 14),
    bg="#4caf50",
    fg="white",
    width=12,
    command=roll_dice
).pack(pady=20)

# -------- Run App --------
root.mainloop()

