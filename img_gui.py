from tkinter import *
import webbrowser
from urllib.request import urlopen
from PIL import ImageTk, Image
import os
import requests
from io import BytesIO
import base64
import sys

master = Tk()
master.title("UofTHacks")
def show_entry_fields():
    image_url = e1.get()
    # webbrowser.open_new(image_url)

    try:
        resp = requests.get(image_url, stream=True).raw

    except requests.exceptions.RequestException as e:
        sys.exit(1)

    try:
        img = Image.open(resp)

    except IOError:
        print("Unable to open image")
        sys.exit(1)

    img.save('img1.jpg', 'jpeg')

    try:
        image1 = Image.open("img1.jpg")

    except IOError:
        print("Unable to load image")
        sys.exit(1)

    # image1.show()
    photo = ImageTk.PhotoImage(image1)
    cv = Canvas()
    cv.pack(side='top', fill='both', expand='yes')
    cv.create_image(10, 10, image=photo, anchor='nw')


Label(master, text="Enter image link").grid(row=0)

e1 = Entry(master)

e1.grid(row=0, column=1)

Button(master, text='Submit', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop()