import tkinter as tk
from tkinter import messagebox

# Caesar Cipher logic
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - base + shift) % 26 + base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Function that runs when user clicks a button
def process_text():
    message = entry_message.get()
    shift_text = entry_shift.get()

    if not shift_text.isdigit():
        messagebox.showerror("Invalid Input", "Shift must be a number.")
        return

    shift = int(shift_text)
    if var.get() == 1:
        result = caesar_encrypt(message, shift)
    else:
        result = caesar_decrypt(message, shift)

    output_label.config(text=f"Result: {result}")

# GUI layout
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("800x600")
root.configure(bg="#000000")

# Title
tk.Label(root, text="Caesar Cipher Encrypt/Decrypt", fg="white", bg="#1a1a1a", font=("Arial", 20)).pack(pady=50)

# Message input
tk.Label(root, text="Enter your message:", fg="white", bg="#1a1a1a").pack()
entry_message = tk.Entry(root, width=40)
entry_message.pack(pady=10)

# Shift input
tk.Label(root, text="Enter shift value:", fg="white", bg="#1a1a1a").pack()
entry_shift = tk.Entry(root, width=20)
entry_shift.pack(pady=10)

# Encrypt or Decrypt selection
var = tk.IntVar(value=1)  # 1 for encrypt, 2 for decrypt
tk.Radiobutton(root, text="Encrypt", variable=var, value=1, fg="white", bg="#1a1a1a").pack()
tk.Radiobutton(root, text="Decrypt", variable=var, value=2, fg="white", bg="#1a1a1a").pack()

# Process button
tk.Button(root, text="Run", command=process_text, bg="#007acc", fg="white").pack(pady=10)

# Result display
output_label = tk.Label(root, text="Result:", fg="lightgreen", bg="#1a1a1a", font=("Arial", 12))
output_label.pack(pady=10)

root.mainloop()
