import tkinter as tk
from tkinter import messagebox
from app import input_int, get_page
from book import BOOK

class Program(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mitt äventyr")
        self.geometry("640x480")
        self.current_id = 1
        current_page = get_page(BOOK, self.current_id)
        self.show_page(current_page)

    def show_page(self, page):
        for widget in self.winfo_children():
            widget.destroy()
        self.label = tk.Label(self, text=page["title"])
        self.label.pack(padx=10, pady=10)
        self.text = tk.Label(self, text=page["text"], wraplength=500)
        self.text.pack(padx=10, pady=10)
        for i, option in enumerate(page["options"]):
            self.button = tk.Button(self, text=option["text"], command=lambda next_id=option["next_id"]: self.next_page(next_id))
            self.button.pack(pady=10)

    def next_page(self, next_id):
        self.current_id = next_id
        next_page = get_page(BOOK, self.current_id)
        self.show_page(next_page)

if __name__ == "__main__":
    prg = Program()
    prg.mainloop()
