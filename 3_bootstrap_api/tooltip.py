import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tooltip import ToolTip

app = ttk.Window(title="Tooltips")

b1 = ttk.Button(app, text="Tooltip 1")
b1.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+E+W)

b2 = ttk.Button(app, text="Tooltip 2")
b2.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+E+W)

# default tooltip (pop-up message while hover over the button)
ToolTip(b1, text="This is the default style")

# styled tooltip
ToolTip(b2, text="This is dangerous", bootstyle=(DANGER, INVERSE))

app.mainloop()


