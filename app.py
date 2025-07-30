import tkinter as tk
import random

jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I'm reading a book about anti-gravity. It's impossible to put down!",
    "What do you call fake spaghetti? An impasta!",
    "Why did the scarecrow win an award? He was outstanding in his field!"
]

def tell_joke():
    joke = random.choice(jokes)
    label.config(text=joke)

def copy_joke():
    joke = label.cget("text")
    root.clipboard_clear()
    root.clipboard_append(joke)

root = tk.Tk()
root.title("Random Joke Generator")
root.geometry("400x200")

label = tk.Label(root, text="Click the button for a joke!", wraplength=380, justify="center", font=("Arial", 12))
label.pack(pady=20)

button = tk.Button(root, text="Tell me a joke", command=tell_joke)
button.pack()

copy_button = tk.Button(root, text="Copy joke", command=copy_joke)
copy_button.pack()

root.mainloop()
