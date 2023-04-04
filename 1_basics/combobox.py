from tkinter.messagebox import showinfo
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


# Handle the selection event
def month_change(event):
    showinfo(
        title='Selection Made',
        message=f"You've selected {selected_month.get()}!"
    )

# Setup a new window with title and theme
app = ttk.Window(title='Combobox Style', themename='darkly')

# Setup lebel for instruction
l1 = ttk.Label(text='Please select a month:', bootstyle=INFO)
l1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+W+E)

# Create the combobox
selected_month = ttk.StringVar()
cb1 = ttk.Combobox(app, textvariable=selected_month, state='readonly', bootstyle=PRIMARY)

# Set the selection values as first 3 letters of every month
cb1['values'] = ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dev']

# Put combobox widget on the UI and wire to event
cb1.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)
cb1.bind('<<ComboboxSelected>>', month_change)

# Start the UI
app.mainloop()