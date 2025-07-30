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

root = tk.Tk()
root.title("Random Joke Generator")
root.geometry("400x200")

label = tk.Label(
    root,
    text="Click the button for a joke!",
    wraplength=380,
    justify="center",
    font=("Arial", 12),
)
label.pack(pady=20)

button = tk.Button(root, text="Tell me a joke", command=tell_joke)
button.pack()

root.mainloop()
