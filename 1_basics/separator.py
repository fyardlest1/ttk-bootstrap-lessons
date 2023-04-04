import ttkbootstrap as ttk
from ttkbootstrap.constants import *

app = ttk.Window(title='Separator', themename='darkly')

ttk.Label(app, text='Horizontal Heading Here', bootstyle=INFO).grid(row=1, column=0, padx=5, pady=5)
ttk.Separator(app,orient=HORIZONTAL, bootstyle=PRIMARY).grid(row=2, columnspan=5, sticky=N+S)

ttk.Label(app, text='Vertical Heading Here', bootstyle=INFO).grid(row=8, column=0, columnspan=5, padx=5, pady=5)
ttk.Separator(app,orient=VERTICAL, bootstyle=PRIMARY).grid(column=1, row = 9, rowspan=5, sticky=N+S)

app.mainloop()



