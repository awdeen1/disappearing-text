from tkinter import *
from tkinter.ttk import *
from widgets import *
root = Tk()
root.geometry("730x400")
root.resizable(width=False, height=False)

def on_timer_end():
    text_widget.reset()

def on_key_press(event):
    timer_widget.restart_timer()
    word_count_var.set(f"Words: {text_widget.word_count}")

text_widget = TextInputWidget()
text_widget.grid(column=0, row=1)

timer_widget = TkTimerWidget(master=root, callback=on_timer_end, timer_length=5)
timer_widget.grid(column=0, row=0)

word_count_var = StringVar()
word_count = Label(textvariable=word_count_var)
word_count.grid(column=0, row=2)

text_widget.bind("<Key>", on_key_press)

root.mainloop()