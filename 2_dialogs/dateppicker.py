import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import DatePickerDialog

# Setup a new window with title and theme
root = ttk.Window(title="Date Picker Styles", themename="darkly")

# Place a date picker in the window
dp1 = DatePickerDialog()

# Start the UI
root.mainloop()



