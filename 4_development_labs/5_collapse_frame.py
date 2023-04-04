import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledFrame

app = ttk.Window(title='Collapsing Frame', themename='darkly')

# Build Frame 1
l1 = ttk.Label(app, text="Frame Area 1").grid(row=0, column=0, padx=5,pady=5, sticky=N+S+E+W)
b1_open = ttk.Button(app, text="v", command=lambda: sf1.grid(row=1, column=0, padx=5, pady=5, sticky=(N+S+E+W)), bootstyle=DEFAULT)
b1_open.grid(row=0, column=1, padx=5, pady=5, sticky=(N+S+E+W))
b1_close = ttk.Button(app, text="^", command=lambda: sf1.grid_forget(), bootstyle=DEFAULT)
b1_close.grid(row=0, column=2, padx=5, pady=5, sticky=(N+S+E+W))

sf1 = ScrolledFrame(app, autohide=True)
sf1.grid(row=1, column=0, padx=5, pady=5, sticky=(N+S+E+W))

# Add a number of checkbuttons into the scrolled frame
for x in range(10):
    ttk.Checkbutton(sf1, text=f"Collapse Frame 1 Item {x}").grid(row=x, column=0, sticky=(N+S+E+W))

# Build Frame 2
l2 = ttk.Label(app, text="Frame Area 2").grid(row=2, column=0, padx=5,pady=5, sticky=N+S+E+W)
b2_open = ttk.Button(app, text="v", command=lambda: sf2.grid(row=3, column=0, padx=5, pady=5, sticky=(N+S+E+W)), bootstyle=DEFAULT)
b2_open.grid(row=2, column=1, padx=5, pady=5, sticky=(N+S+E+W))
b2_close = ttk.Button(app, text="^", command=lambda: sf2.grid_forget(), bootstyle=DEFAULT)
b2_close.grid(row=2, column=2, padx=5, pady=5, sticky=(N+S+E+W))

sf2 = ScrolledFrame(app, autohide=True)
sf2.grid(row=3, column=0, padx=5, pady=5, sticky=(N+S+E+W))

# Add a number of checkbuttons into the scrolled frame
for x in range(10):
    ttk.Checkbutton(sf2, text=f"Collapse Frame 2 Item {x}").grid(row=x, column=0, sticky=(N+S+E+W))

# Build Frame 3
l3 = ttk.Label(text="Frame Area 3").grid(row=4, column=0, padx=5,pady=5, sticky=N+S+E+W)
b3_open = ttk.Button(app, text="v", command=lambda: sf3.grid(row=5, column=0, padx=5, pady=5, sticky=(N+S+E+W)), bootstyle=DEFAULT)
b3_open.grid(row=4, column=1, padx=5, pady=5, sticky=(N+S+E+W))
b3_close = ttk.Button(app, text="^", command=lambda: sf3.grid_forget(), bootstyle=DEFAULT)
b3_close.grid(row=4, column=2, padx=5, pady=5, sticky=(N+S+E+W))

sf3 = ScrolledFrame(app, autohide=True)
sf3.grid(row=5, column=0, padx=5, pady=5, sticky=(N+S+E+W))

# Add a number of checkbuttons into the scrolled frame
for x in range(10):
    ttk.Checkbutton(sf3, text=f"Collapse Frame 3 Item {x}").grid(row=x, column=0, sticky=(N+S+E+W))

app.mainloop()



