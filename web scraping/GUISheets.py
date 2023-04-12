import tkinter as tk
from tkinter import filedialog
import pandas as pd

class TableSheet:
    def __init__(self, root):
        self.root = root
        self.root.title("Table Sheet")
        self.df = None
        self.create_widgets()

    def create_widgets(self):
        self.load_button = tk.Button(self.root, text="Load CSV", command=self.load_csv)
        self.load_button.pack(side="top", padx=10, pady=10)
        self.table = tk.Frame(self.root)
        self.table.pack(side="top", fill="both", expand=True)

    def load_csv(self):
        file_path = filedialog.askopenfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv"), ("All Files", "*.*")])
        if file_path:
            self.df = pd.read_csv(file_path)
            self.display_table()

    def display_table(self):
        for widget in self.table.winfo_children():
            widget.destroy()
        headers = list(self.df.columns)
        num_rows = len(self.df.index)
        num_cols = len(self.df.columns)
        for i, header in enumerate(headers):
            label = tk.Label(self.table, text=header, font=("Arial", 12, "bold"), borderwidth=1, relief="solid")
            label.grid(row=0, column=i, sticky="nsew")
        for i in range(num_rows):
            for j in range(num_cols):
                val = self.df.iloc[i, j]
                label = tk.Label(self.table, text=val, font=("Arial", 12), borderwidth=1, relief="solid")
                label.grid(row=i+1, column=j, sticky="nsew")

if __name__ == "__main__":
    root = tk.Tk()
    app = TableSheet(root)
    root.mainloop()
