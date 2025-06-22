import tkinter as tk
from tkinter import  filedialog,messagebox
from tkinter.scrolledtext import ScrolledText

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path,"r") as file:
                text_area.delete(1.0, tk.END)
                text_area.insert(tk.END, file.read())
        except Exception as e:
            messagebox.showerror("Error", f"Could not open file: {e}")

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension='.txt',
                                             filetypes=[("Text Files", "*.txt")])
    if file_path:
        try:
            with open(file_path,"w")as file:
                file.write(text_area.get(1.0, tk.END))
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Ifuchi Text Editor")
text_area = ScrolledText(root, wrap=tk.WORD,undo=True)
text_area.pack(fill=tk.BOTH, expand=1)
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)
root.config(menu=menu_bar)
root.geometry("600x400")
root.mainloop()
# This code creates a simple text editor using Tkinter in Python.
# It allows users to open and save text files, with a scrollable text area for editing.
# The editor has a menu bar with options for file operations.       


