import tkinter as tk
from tkinter import scrolledtext

class Terminal(tk.Frame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.text_area = scrolledtext.ScrolledText(
            self, wrap=tk.WORD,
            width=80,
            height=25,
            font=("Fixedsys", 10),
            bg="black",
            fg="white",
            insertbackground="white",
            blockcursor=True
        )
        self.text_area.pack(fill="both", expand=True)
        self.text_area.bind("<Return>", self.execute_command)
        self.text_area.config(insertofftime=200, insertontime=200)  # Blinking cursor
        self.text_area.focus_set()  # Set focus to the text area
        self.text_area.bind("<KeyPress>", self.prevent_deletion)

    def execute_command(self, event):
        command = self.text_area.get("insert linestart", "insert lineend")
        self.text_area.insert(tk.END, f"\nExecuted: {command}\n")
        self.text_area.see(tk.END)  # Autoscroll to the end
        return "break"

    def prevent_deletion(self, event):
        if event.keysym in ("BackSpace", "Delete"):
            if self.text_area.index(tk.INSERT) == self.text_area.index("insert linestart"):
                return "break"
