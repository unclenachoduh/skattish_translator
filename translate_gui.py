import tkinter as tk
from tkinter import *
from tkinter.ttk import *

import translate

root = tk.Tk()
root.title("Skattish Translation Engine")

# Title Frame
title_frame = tk.Frame(root, bg="#dfdfdf")

title_label = tk.Label(title_frame, text="Enter some text below and click Translate to generate Skattish mp3", bg="#dfdfdf")
title_label.pack()

# Text Frame
text_frame = tk.Frame(root, width=500, height=200, background="#ffffff")
text_frame.grid(row=1, column=1)

text_box = Text(text_frame)
scroll_bar = Scrollbar(text_frame)
scroll_bar.config(command=text_box.yview)
text_box.config(yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y)
text_box.pack(expand=YES, fill=BOTH)

def clicked():

	if status.cget("text") == "Status: Finished" or status.cget("text") == "Status: PLEASE RESET SYSTEM BEOFRE RERUNNING!!":
		status.configure(text="Status: PLEASE RESET SYSTEM BEOFRE RERUNNING!!")
	else:
		status.configure(text="Status: Finished")
		input_text = text_box.get("1.0", "end-1c")
		translate.translate(input_text, v.get())

def reset():
	status.configure(text="Status: Ready")
	text_box.delete('1.0', 'end')

def close():
	root.destroy()

btn = Button(text_frame, text="Translate", command=clicked)
btn.pack()
btn2 = Button(text_frame, text="Reset", command=reset)
btn2.pack()
btn3 = Button(text_frame, text="Close", command=close)
btn3.pack()

status = tk.Label(text_frame, text="Status: Ready")
status.pack(fill="both", expand=True)

# Mood Frame
mood_frame = tk.Frame(root, width=150, bg="#ababab")

mood_label = tk.Label(mood_frame, text="Mood", bg="#dfdfdf")
mood_label.pack(fill=X)

v = IntVar()
v.set(7)

rad1 = Radiobutton(mood_frame,text='Angry', value=1, variable=v)
rad2 = Radiobutton(mood_frame,text='Bright', value=2, variable=v)
rad3 = Radiobutton(mood_frame,text='Calm', value=3, variable=v)
rad4 = Radiobutton(mood_frame,text='Dark', value=4, variable=v)
rad5 = Radiobutton(mood_frame,text='Dramatic', value=5, variable=v)
rad6 = Radiobutton(mood_frame,text='Funky', value=6, variable=v)
rad7 = Radiobutton(mood_frame,text='Happy', value=7, variable=v)
rad8 = Radiobutton(mood_frame,text='Inspirational', value=8, variable=v)
rad9 = Radiobutton(mood_frame,text='Romantic', value=9, variable=v)
rad10 = Radiobutton(mood_frame,text='Sad', value=10, variable=v)

rad1.pack(anchor=W)
rad2.pack(anchor=W)
rad3.pack(anchor=W)
rad4.pack(anchor=W)
rad5.pack(anchor=W)
rad6.pack(anchor=W)
rad7.pack(anchor=W)
rad8.pack(anchor=W)
rad9.pack(anchor=W)
rad10.pack(anchor=W)

# Assembly
title_frame.grid(row=0, column=0, columnspan=2,  sticky="ew")
mood_frame.grid(row=1, column=1, sticky="ns")
text_frame.grid(row=1, column=0, sticky="nsew")

root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(1, weight=1)

root.mainloop()