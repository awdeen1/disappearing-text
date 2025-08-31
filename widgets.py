from tkinter import *
from tkinter.ttk import *

class TextInputWidget(Text):
    def __init__(self):
        super().__init__(font=("ariel", 15), width=70, height=12, pady=10, padx=10, wrap="word")

    def reset(self):
        self.delete("1.0", END)

    @property
    def word_count(self):
        return len(self.get("1.0", "end-1c").split())


class TkTimerWidget(Label):
    def __init__(self, master, callback, timer_length):
        self.master = master
        self.callback = callback

        self.timer_length = timer_length
        self.current_timer_length = timer_length

        self.running = None

        self.time_display = StringVar()
        self.time_display.set("Start Typing!")

        super().__init__(master=self.master, textvariable=self.time_display, font=("tnr", 30))


    def run_timer(self):
        if self.current_timer_length > 0:
            self.running = self.master.after(ms=1000, func=self.run_timer)
            self.time_display.set(f"{self.current_timer_length} seconds.")
        else:
            self.time_display.set("Game Over! Start typing to start again!")
            self.callback()
        self.current_timer_length -=1

    def restart_timer(self):
        self.time_display.set("Start Typing!")
        if self.running:
            self.master.after_cancel(self.running)
        self.current_timer_length = self.timer_length
        self.run_timer()

