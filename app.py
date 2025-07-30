import tkinter as tk
import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? He was outstanding in his field!"
]

fade_steps = 20

def fade_in(step=0):
    color_value = 255 - int(step * 255 / fade_steps)
    hex_color = f"#{color_value:02x}{color_value:02x}{color_value:02x}"
    label.config(fg=hex_color)
    if step < fade_steps:
        label.after(30, fade_in, step + 1)

def fade_out(step=0, new_text=""):
    color_value = int(step * 255 / fade_steps)
    hex_color = f"#{color_value:02x}{color_value:02x}{color_value:02x}"
    label.config(fg=hex_color)
    if step < fade_steps:
        label.after(30, fade_out, step + 1, new_text)
    else:
        if new_text:
            label.config(text=new_text)
            fade_in()

def tell_joke():
    joke = random.choice(jokes)
    fade_out(new_text=joke)

def copy_joke():
    joke = label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(joke)

root = tk.Tk()
root.title("Random Joke Generator")
root.geometry("450x250")
root.configure(bg="#2c3e50")
root.resizable(False, False)

label = tk.Label(
    root,
    text="Click the button for a joke!",
    wraplength=420,
    justify="center",
    font=("Helvetica", 14, "bold"),
    bg="#2c3e50",
    fg="white",
)
label.pack(pady=20)

button = tk.Button(
    root,
    text="Tell me a joke",
    command=tell_joke,
    font=("Helvetica", 12, "bold"),
    bg="#3498db",
    fg="white",
    activebackground="#2980b9",
    activeforeground="white",
    bd=0,
    padx=10,
    pady=5,
)
button.pack(pady=(0, 10))

copy_button = tk.Button(
    root,
    text="Copy joke",
    command=copy_joke,
    font=("Helvetica", 12),
    bg="#e67e22",
    fg="white",
    activebackground="#d35400",
    activeforeground="white",
    bd=0,
    padx=10,
    pady=5,
)
copy_button.pack()

root.mainloop()
