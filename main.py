from tkinter import *

MAIN_WHITE = '#F7F7F7'
BG_COLOR = '#2E2787'
FG_YELLOW = "#FFDD36"


class KeepUp(Tk):
    def __init__(self):
        super().__init__()
        self.title('Keep It Up - Python Writing App')
        self.config(padx=20, pady=20, bg=BG_COLOR)
        self.minsize(width=500, height=500)
        self.name_label = Label(text='Keep It Up!', font=("Arial", 30, "bold"), bg=BG_COLOR, fg=FG_YELLOW, pady=10,
                                anchor="center")
        self.name_label.grid(column=0, row=0, columnspan=4)
        for col in range(4):
            self.grid_columnconfigure(col, weight=1)
        self.text = Text(height=20, width=80, font=("Helvetica", 11), bg=MAIN_WHITE,
                         highlightcolor=FG_YELLOW, highlightthickness=2)
        self.text.focus()
        self.text.grid(column=0, row=1, columnspan=4, pady=10, padx=20)
        self.text_length = 0
        self.char_count = 0
        self.char_count_label = Label(text=f"Total characters written: {self.char_count}",
                                      font=("Helvetica", 12, "bold"), bg=BG_COLOR, fg=FG_YELLOW, anchor="e")
        self.char_count_label.grid(column=0, row=2)
        self.timer = 0
        self.timer_label = Label(text=f"Elapsed time: {self.timer}s",
                                 font=("Helvetica", 12, "bold"), bg=BG_COLOR, fg=FG_YELLOW, anchor="w")
        self.timer_label.grid(column=3, row=2)
        self.inactivity = 0
        self.after(10, self.count_characters)
        self.after(1000, self.check_typing)
        self.after(1000, self.timer_function)
        self.after(500, self.update_text_length)

    def check_typing(self):
        if self.text_length == self.char_count:
            self.inactivity += 1
        else:
            self.inactivity = 0
        if self.inactivity == 5:
            self.text.delete("1.0", END)
            self.inactivity = 0
        self.after(1000, self.check_typing)

    def count_characters(self):
        self.char_count = len(self.text.get("1.0", END)) - 1
        self.char_count_label.config(text=f"Total characters written: {self.char_count}")
        self.after(10, self.count_characters)

    def timer_function(self):
        self.timer += 1
        self.timer_label.config(text=f"Elapsed time: {self.timer}s")
        self.after(1000, self.timer_function)

    def update_text_length(self):
        self.text_length = self.char_count
        self.after(500, self.update_text_length)


app = KeepUp()
app.mainloop()
