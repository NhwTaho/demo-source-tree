import tkinter as tk
from tkinter import Menu, Scrollbar, filedialog, messagebox, colorchooser, simpledialog, font

# Global variable to store the current file path
current_file = None

# Function to open a file
def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text files", ".txt"), ("All files", ".*")]
    )
    if file_path:
        try:
            with open(file_path, "r") as file:
                content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)
            root.title(f"{file_path} - Notepad")
            current_file = file_path
        except Exception as e:
            messagebox.showerror("Error", f"Error opening file: {e}")

# Function to save the current file
def save_file():
    global current_file
    if current_file:
        try:
            with open(current_file, "w") as file:
                file.write(text_area.get(1.0, tk.END))
            messagebox.showinfo("Save", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {e}")
    else:
        save_as_file()

# Function to save as a new file
def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", ".txt"), ("All files", ".*")]
    )
    if file_path:
        try:
            with open(file_path, "w") as file:
                file.write(text_area.get(1.0, tk.END))
            root.title(f"{file_path} - Notepad")
            current_file = file_path
            messagebox.showinfo("Save As", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Error saving file: {e}")

# Function to show about information
def show_about():
    messagebox.showinfo("About Notepad", "Simple Notepad using Tkinter\nDeveloped by [Your Name]")

# Function to perform cut operation
def cut():
    text_area.event_generate("<<Cut>>")

# Function to perform copy operation
def copy():
    text_area.event_generate("<<Copy>>")

# Function to perform paste operation
def paste():
    text_area.event_generate("<<Paste>>")

# Function to perform undo operation
def undo():
    text_area.event_generate("<<Undo>>")

# Function to perform redo operation
def redo():
    text_area.event_generate("<<Redo>>")

# Function to change text color
def change_text_color():
    color = colorchooser.askcolor(title="Choose Text Color")
    if color[1]:
        text_area.config(fg=color[1])

# Function to change background color
def change_bg_color():
    color = colorchooser.askcolor(title="Choose Background Color")
    if color[1]:
        text_area.config(bg=color[1])

# Function to change font
def change_font():
    font_family = simpledialog.askstring("Font", "Enter font family (e.g., Arial, Courier, Times):")
    if font_family:
        current_font = font.nametofont(text_area.cget("font"))
        current_font.config(family=font_family)
        text_area.config(font=current_font)

# Function to change font size
def change_font_size():
    font_size = simpledialog.askinteger("Font Size", "Enter font size (e.g., 10, 12, 14):", minvalue=1)
    if font_size:
        current_font = font.nametofont(text_area.cget("font"))
        current_font.config(size=font_size)
        text_area.config(font=current_font)

# Create the main application window
root = tk.Tk()
root.title("Untitled - Notepad")
root.geometry("600x400")

# Create a Text widget
text_area = tk.Text(root, wrap='word', undo=True)
text_area.pack(expand=1, fill='both')

# Set default font
default_font = font.nametofont(text_area.cget("font"))
default_font.config(family="Arial", size=12)
text_area.config(font=default_font)

# Create a Scrollbar and attach it to the Text widget
scroll_bar = Scrollbar(text_area)
text_area.config(yscrollcommand=scroll_bar.set)
scroll_bar.config(command=text_area.yview)
scroll_bar.pack(side='right', fill='y')

# Create a Menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# Add File menu
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=lambda: text_area.delete(1.0, tk.END))
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="Save As...", command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Undo", command=undo)
edit_menu.add_command(label="Redo", command=redo)
edit_menu.add_separator()
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)
menu_bar.add_cascade(label="Edit", menu=edit_menu)

# Add Format menu for font and color options
format_menu = Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Font...", command=change_font)
format_menu.add_command(label="Font Size...", command=change_font_size)
format_menu.add_separator()
format_menu.add_command(label="Text Color...", command=change_text_color)
format_menu.add_command(label="Background Color...", command=change_bg_color)
menu_bar.add_cascade(label="Format", menu=format_menu)

# Add Help menu
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About Notepad", command=show_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

# Start the Tkinter event loop
root.mainloop()