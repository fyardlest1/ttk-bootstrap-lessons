import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText
from tkinter.filedialog import askopenfilename

app = ttk.Window(title="Reader", themename="flatly")

# Handle the file open dialog and loading data
def open_file():
    path = askopenfilename()
    if not path:
        return

    with open(path, encoding='utf-8') as f:
        text_reader.delete('1.0', END)
        text_reader.insert(END, f.read())

        file_path.delete(0, END)
        file_path.insert(END, path)

# Setup scrolled text w/ scrollbar
text_reader = ScrolledText(app, padding=5, height=30, width=100,autohide=False, vbar=True, hbar=True)
text_reader.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=N+S+E+W)

# Add default text
text_reader.insert(END, 'Browse to select a file')

# Setup the file path and browse button
file_path = ttk.Entry(text="Browse to select a file", width=90)
file_path.grid(row=1, column=0, padx=5,pady=5, sticky=N+S+E+W)

btn_browse = ttk.Button(text="Browse", command=open_file)
btn_browse.grid(row=1, column=1, padx=5, pady=5, sticky=S+E)

# Start up the app
app.mainloop()



