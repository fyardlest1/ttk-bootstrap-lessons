import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title='Menu Button Styles', themename='darkly')

#  First Meny Botton
mb1 = ttk.Menubutton(app, text='This is a LabelFrame', bootstyle=DEFAULT)
mb1.grid(row=0, column=0, padx=5, pady=5, sticky=(N+S+E+W))

# Create the menu and associate it with the button
mb1.menu = ttk.Menu(mb1, tearoff=0)
mb1['menu'] = mb1.menu

# Create the storage of the selection
opt1_var = ttk.IntVar()
opt2_var = ttk.IntVar()

# Adding checkbutton for our menu
mb1.menu.add_checkbutton(label='Hello!', variable=opt1_var)
mb1.menu.add_checkbutton(label='World!', variable=opt2_var)

# Start the UI
app.mainloop()