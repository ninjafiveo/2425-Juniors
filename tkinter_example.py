from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os

# Create the main window
root = Tk()
root.title("Ninja Noting App")
root.geometry("500x500")

# Define the directory to store notes
notes_dir = "notes"
if not os.path.exists(notes_dir):
    os.makedirs(notes_dir)

# Create a text widget for note input
text_area = Text(root, wrap=WORD, height=20)
text_area.pack(pady=20)

# Function to save the current note
def save_note():
    note_content = text_area.get("1.0", END).strip()
    if note_content:
        # Ask user for a filename
        filename = filedialog.asksaveasfilename(
            initialdir=notes_dir,
            title="Save Note",
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            with open(filename, "w") as file:
                file.write(note_content)
            messagebox.showinfo("Note Saved", f"Note saved as {os.path.basename(filename)}")
            refresh_note_list()
    else:
        messagebox.showwarning("Empty Note", "Please write something before saving.")

# Function to load a selected note
def load_note():
    selected_note = note_listbox.get(ACTIVE)
    if selected_note:
        filepath = os.path.join(notes_dir, selected_note)
        with open(filepath, "r") as file:
            note_content = file.read()
        text_area.delete("1.0", END)
        text_area.insert("1.0", note_content)

# Function to refresh the list of saved notes
def refresh_note_list():
    note_listbox.delete(0, END)
    for filename in os.listdir(notes_dir):
        if filename.endswith(".txt"):
            note_listbox.insert(END, filename)

# Create buttons for saving notes
save_button = Button(root, text="Save Note", command=save_note)
save_button.pack(pady=5)

# Create a listbox to display saved notes
note_listbox = Listbox(root)
note_listbox.pack(pady=10, fill=BOTH, expand=True)

# Bind the listbox selection event to automatically load the selected note
note_listbox.bind("<<ListboxSelect>>", lambda event: load_note())

# Populate the note list when the app starts
refresh_note_list()

# Start the Tkinter event loop
root.mainloop()