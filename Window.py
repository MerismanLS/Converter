import tkinter as tk
from tkinter import messagebox
from ConverterCurrency import ConverterCurrency as ConC


class Window(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x150")

        self.number = tk.StringVar(value="0.0")
        self.from_cur = tk.StringVar()
        self.to_cur = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        container = tk.Frame(self)
        container.pack(expand=True, fill=tk.BOTH, padx=10, pady=20)

        entry = tk.Entry(container, textvariable=self.number)
        entry.pack(fill=tk.BOTH)

        options_frame = tk.Frame(container)
        options_frame.pack(fill=tk.BOTH)

        currency = ConC.currencies

        from_cur = tk.OptionMenu(options_frame, self.from_cur, *currency)
        from_cur.pack(side=tk.LEFT, fill=tk.X, expand=True)

        to_cur = tk.OptionMenu(options_frame, self.to_cur, *currency)
        to_cur.pack(side=tk.RIGHT, fill=tk.X, expand=True)

        btn_frame = tk.Frame(container)
        btn_frame.pack(fill=tk.BOTH)

        button = tk.Button(btn_frame, text="Convert")
        button['command'] = self.convert
        button.pack(fill=tk.X, side=tk.LEFT, expand=True)

        button_clear = tk.Button(btn_frame, text="Clear")
        button_clear['command'] = self.clear
        button_clear.pack(fill=tk.X, side=tk.RIGHT)

    def convert(self):
        try:
            money = float(self.number.get())
            amount = ConC.converter(self.from_cur.get(), self.to_cur.get(), money)
            self.number.set(str(amount))
        except ValueError as e:
            messagebox.showinfo(title="Error converting", message="U are debil!")

    def clear(self):
        self.number.set("0.0")
