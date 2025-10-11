from io import BytesIO
from tkinter import *
from random import randint
from tkinter import messagebox
from captcha.image import ImageCaptcha

# CAPTCHA image generator
image = ImageCaptcha(
    fonts=[
        "captcha-generator\\ChelseaMarketsr.ttf",
        "captcha-generator\\DejaVuSanssr.ttf"
    ]
)

# Global captcha text
captcha_text = str(randint(100000, 999999))
data = image.generate(captcha_text)
image.write(captcha_text, "out.png")

def verify():
    global captcha_text
    x = entry.get().strip()
    if x == captcha_text:
        messagebox.showinfo("Success", "Verified")
    else:
        messagebox.showinfo("Alert", "Not verified")
        refresh()

def refresh():
    global captcha_text
    captcha_text = str(randint(100000, 999999))
    image.write(captcha_text, "out.png")
    photo = PhotoImage(file="out.png")
    l1.config(image=photo)
    l1.image = photo 
    entry.delete(0, END)


root = Tk()
root.title("CAPTCHA Verification")

photo = PhotoImage(file="out.png")
l1 = Label(root, image=photo, height=100, width=200)
l1.image = photo
entry = Entry(root, width=20)
b1 = Button(root, text="Submit", command=verify)
b2 = Button(root, text="Refresh", command=refresh)

l1.pack(pady=10)
entry.pack(pady=5)
b1.pack(pady=5)
b2.pack(pady=5)

root.mainloop()
