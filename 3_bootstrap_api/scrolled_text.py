import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText

app = ttk.Window()

# Set up scrolled text w/ autohide vertical scrollbar
st = ScrolledText(app, padding=5, height=10, autohide=True, vbar=True, hbar=True)
st.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+E+W)

# add text (every text will start at the "end" of the previous)
st.insert(END, 'Insert your text here.')

app.mainloop()



