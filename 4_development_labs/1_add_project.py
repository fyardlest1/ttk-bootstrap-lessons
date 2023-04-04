import ttkbootstrap as ttk
from ttkbootstrap.constants import *

# Setup a new window with title and theme
app = ttk.Window(title="Adding Project 1", themename="solar")

# Handle operator button press   
def press_operation():
    sum_value = int(te1.get()) + int(te2.get())
    te3.delete(0,END)
    te3.insert(END, sum_value)

# Reset the form
def press_clear():
    te1.delete(0,END)
    te2.delete(0,END)
    te3.delete(0,END)

# Place a text entries in the window
l1 = ttk.Label(app, text="First Value")
l1.grid(row=0, column=0, sticky=N+S+W+E)
te1 = ttk.Entry(app, text="", bootstyle=PRIMARY)
te1.grid(row=0, column=1, columnspan=2, sticky=N+S+W+E)

l2 = ttk.Label(app, text="Second Value")
l2.grid(row=1, column=0, sticky=N+S+W+E)
te2 = ttk.Entry(app, text="", bootstyle=PRIMARY)
te2.grid(row=1, column=1, columnspan=2, sticky=N+S+W+E)

# Place operation button in the window
btn_equals = ttk.Button(app, text="=", bootstyle=OUTLINE, command=lambda: press_operation())
btn_equals.grid(row=2, column=1, columnspan=2,padx=3, pady=3, sticky=N+S+E+W)

l3 = ttk.Label(app, text="Total")
l3.grid(row=3, column=0, sticky=N+S+W+E)
te3 = ttk.Entry(app, text="", bootstyle=PRIMARY)
te3.grid(row=3, column=1, columnspan=2, sticky=N+S+W+E)

# Reset button
btn_clear = ttk.Button(app, text="Clear", bootstyle=OUTLINE, command=press_clear)
btn_clear.grid(row=4, column=1, columnspan=2,padx=3, pady=3, sticky=N+S+E+W)


# Start the UI
app.mainloop()



