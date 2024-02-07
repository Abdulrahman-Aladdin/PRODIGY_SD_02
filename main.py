import customtkinter as ctk
from settings import *
import random


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry(f'{WINDOW_SIZE}x{WINDOW_SIZE}')
        self.resizable(RESIZABLE, RESIZABLE)
        self.title(TITLE)
        self.configure(fg_color=WINDOW_COLOR)

        self.rowconfigure(list(range(6)), weight=1, uniform='a')
        self.columnconfigure(0, weight=1, uniform='b')

        self.number = random.randint(0, MAX_NUMBER)

        self.title_label = ctk.CTkLabel(master=self,
                                        text=TITLE,
                                        text_color=CREAMY,
                                        font=ctk.CTkFont(size=LARGE_FONT_SIZE, family=FONT))
        self.title_label.grid(row=0, column=0, padx=5, pady=5)

        self.input_var = ctk.StringVar(value='')
        self.input_entry = ctk.CTkEntry(master=self, textvariable=self.input_var, fg_color=CREAMY,
                                        text_color='black',
                                        corner_radius=CORNER_RADIUS,
                                        font=ctk.CTkFont(size=SMALL_FONT_SIZE, family=FONT))
        self.input_entry.bind('<KeyPress-Return>', command=lambda e: self.check())
        self.input_entry.grid(row=1, column=0, padx=40, pady=10, stick='nsew')

        self.check_btn = ctk.CTkButton(master=self, text='Check', fg_color=CREAMY, hover_color=BUTTON_HOVER_COLOR,
                                       text_color=BUTTON_TEXT_COLOR,
                                       corner_radius=CORNER_RADIUS,
                                       font=ctk.CTkFont(size=SMALL_FONT_SIZE, family=FONT, weight='bold'),
                                       command=self.check)
        self.check_btn.grid(row=2, column=0, padx=90, pady=10, stick='nsew')

        self.result_var = ctk.StringVar(value='RESULT')
        self.result_label = ctk.CTkLabel(master=self, textvariable=self.result_var, text_color=CREAMY,
                                         font=ctk.CTkFont(size=MEDIUM_FONT_SIZE, family=FONT))
        self.result_label.grid(row=3, column=0, padx=20, pady=10, stick='nsew')

        self.attempts_count = ctk.IntVar(value=0)
        self.attempts_var = ctk.StringVar(value='attempts: 0')
        self.attempts_label = ctk.CTkLabel(master=self, textvariable=self.attempts_var, text_color=CREAMY,
                                           font=ctk.CTkFont(size=MEDIUM_FONT_SIZE, family=FONT))
        self.attempts_label.grid(row=4, column=0, padx=20, pady=10, stick='nsew')

        self.hint_var = ctk.StringVar(value='Show Hint')
        self.hint_label = ctk.CTkLabel(master=self, textvariable=self.hint_var, text_color=CREAMY,
                                       font=ctk.CTkFont(size=MEDIUM_FONT_SIZE, family=FONT))
        self.hint_label.bind('<Button>', command=lambda e: self.show_hint())
        self.hint_label.grid(row=5, column=0, padx=20, pady=10, stick='nsew')

        self.mainloop()

    def check(self):
        try:
            value = int(self.input_var.get())
            if value > self.number:
                self.show('HIGH')
            elif value < self.number:
                self.show('LOW')
            elif value == self.number:
                self.show('EXACT')
            self.attempts_count.set(self.attempts_count.get() + 1)
            self.attempts_var.set(f'attempts: {self.attempts_count.get()}')
        except ValueError:
            self.show('Please enter a valid integer!')

    def show(self, message):
        if message == 'EXACT':
            self.result_label.configure(text_color=RIGHT_GUESS_COLOR)
            self.finalize()
        else:
            self.result_label.configure(text_color=WRONG_GUESS_COLOR)
        self.result_var.set(message)

    def finalize(self):
        self.input_entry.configure(state='disabled')
        self.check_btn.configure(text='reset', command=self.restart)

    def restart(self):
        self.input_entry.configure(state='normal')
        self.input_var.set('')
        self.check_btn.configure(text='check', command=self.check)
        self.result_var.set('Result')
        self.hint_var.set('Show Hint')
        self.number = random.randint(0, MAX_NUMBER)
        self.attempts_count.set(0)
        self.attempts_var.set('attempts: 0')
        self.result_label.configure(text_color=CREAMY)

    def show_hint(self):
        hint = min(MAX_NUMBER, self.number + random.randint(0, MAX_NUMBER))
        self.hint_var.set(f'Smaller than {hint}!')


if __name__ == '__main__':
    App()
