class ImageState:
    def __init__(self):
        self.counter = 0

    def get_counter(self):
        return self.counter

    def add_counter(self):
        self.counter += 1
    

import tkinter as tk 
from tkinter import filedialog, Text, messagebox, PhotoImage, Label
import pyautogui as pg
import time
import mouse

root = tk.Tk()

# Full Screen
root.attributes("-fullscreen", True)
root.bind("<Escape>", lambda event: root.destroy())

# Size of window
width_value = root.winfo_screenwidth()
height_value = root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (width_value, height_value))

# Pause Image Frame
canvas = tk.Canvas(root, borderwidth =  0, height = height_value, width = width_value, bg = "white")
canvas.pack()

# Play Image Frame
canvas2 = tk.Canvas(root, borderwidth =  0, height = height_value, width = width_value, bg = "white")
canvas2.pack()

pause = PhotoImage(file = "pause.png")
play = PhotoImage(file = "play.png")
canvas.create_image(970, 500, image = pause)
canvas.pack()

canvas2.create_image(970, 500, image = play)
canvas.pack()

# Function of Button
def button_click():
    pg.hotkey('playpause')
    mouse.move("975", "800")
    #tk.messagebox.showinfo("Message", "Pause/Play")

# Changing Images
def play_image():
    time.sleep(2)
    canvas.pack_forget()
    canvas2.pack_forget()
    button_click()
    canvas2.pack()

def pause_image():
    time.sleep(2)
    canvas.pack_forget()
    canvas2.pack_forget()
    button_click()
    canvas.pack()

# Change image and play music
state = ImageState()

def initialization():
    if ((state.counter % 2) == 0):
        play_image()
        state.add_counter()
    else :
        pause_image()
        state.add_counter()
    print(state.counter)

# Button 1
play_pause1 = tk.Button(root, text = "Pause or Play", padx = width_value / 8,
                    pady = height_value / 2, fg = "white", bg = "#263D42", command = button_click )
play_pause1.pack()

# Presses button after mouse is moved 
play_pause1.bind("<Enter>", lambda event: initialization())

# Moves location of Button
play_pause1.place(relx = 0.0, rely = 0.0, bordermode = "inside")
#play_pause1.place(bordermode)

# Button 2
play_pause2 = tk.Button(root, text = "Pause or Play", padx = width_value / 8,
                    pady = height_value / 2,  fg = "white", bg = "#263D42", command = button_click )
play_pause2.pack()

# Moves location of Button
play_pause2.place(x = width_value - (width_value / 3.5), rely = 0, bordermode = "inside")

# Presses button after mouse is moved 
play_pause2.bind("<Enter>", lambda event: initialization())

root.mainloop()