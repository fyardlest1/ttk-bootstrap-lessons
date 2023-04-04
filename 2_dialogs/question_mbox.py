import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox

# Create and display dialog box
mbox = Messagebox.show_question("Message Box: Question", "TTKBootstrap",
                                buttons=['No:secondary', 'Yes:primary'])


