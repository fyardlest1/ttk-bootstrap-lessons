import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
root = ttk.Window(title='Menu Button Styles', themename='darkly')

# create a Notebook
nb1 = ttk.Notebook(root, bootstyle=SUCCESS)

# Create frames
fr1 = ttk.Frame(nb1)
fr2 = ttk.Frame(nb1)

# Place the first Label on the first frame
le1 = ttk.Label(fr1, text='Label 1 Tat 1 vontent')
le1.grid(row=0, column=0, padx=5, pady=5)

# Place the first Label on the first frame
le2 = ttk.Label(fr2, text='Label 2 Tat 2 vontent')
le2.grid(row=0, column=0, padx=5, pady=5)

# Add frames to notebook
nb1.add(fr1, text='The First Tab')
nb1.add(fr2, text='The Second Tab')

# Add the Notebook to the UI
nb1.grid(row=0, column=0, padx=15, pady=15)

# Start the UI
root.mainloop()