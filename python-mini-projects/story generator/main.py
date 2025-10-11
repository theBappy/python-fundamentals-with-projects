import random
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from ttkthemes import ThemedStyle

def generate_story():
    when = [
        "A few years age",
        "Yesterday",
        "Last night",
        "A long time ago",
        "On 20 the feb",
    ]
    who = ["a rabbit", "an elephant", "a mouse", "a turtle", "a cat", "a tiger"]
    name = ["ali", "miriam","daniel", "david", "mark", "john", "hoouk", "Starwalker"]
    residence = ["Barcelona", "India", "Germany", "Venice", "Maldives", "England"]
    went = ["cinema", "university", "seminar","school", "laundry", "restaurant"]
    happend = [
        "made a lot of friends",
        "ate a delicious meal", 
        "discovered a hidden treasure", 
        "playing pool",
        "solved a mystery",
        "wrote a best-selling novel"
    ]
    story = []
    total_words = 0

    while total_words < 100:
        sentence = (
            random.choice(when) + ", " + random.choice(who) + " named " + random.choice(name) + ", who lived in " + random.choice(residence) + ", decided to to the " + random.choice(went) + " " + random.choice(happend) + " while at the " + random.choice(went) + "."
        )

        story.append(sentence)
        total_words += len(sentence.split())

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "\n".join(story))
    result_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Python Story Generator")

# themed styled
style = ThemedStyle(root)
style.set_theme("arc")

custom_style = ttk.Style()
custom_style.configure(
    "BlueGradient.TButton",
    background="#007acc",
    foreground="Black",
    borderwidth=0,
    focuscolor="#007acc"
)

generate_button = ttk.Button(
    root, text="Generate Story",
    style="BlueGradient.TButton",
    command=generate_story
)
generate_button.pack(pady=10, ipadx=10, ipady=5)

result_text = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, height=10,
    width=10, state=tk.DISABLED
)
result_text.pack(padx=20, pady=10)

root.mainloop()