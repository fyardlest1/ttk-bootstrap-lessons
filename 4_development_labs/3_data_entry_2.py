import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter.filedialog import asksaveasfilename

# Setup a new window with title and theme
app = ttk.Window(title="Data Entry Form", themename="superhero")

def clear_form():
    te_FirstName.delete(0,END)
    te_LastName.delete(0,END)
    te_Email.delete(0,END)

def save_form():
    files = [('All Files', '*.*'), ('Text Document', '*.txt')]
    fileName = asksaveasfilename(filetypes = files, defaultextension = files, confirmoverwrite=False)
    if len(fileName) > 0:
        contactFile = open(fileName, 'a')
        contact = str(te_FirstName.get()) + "," + str(te_LastName.get()) + "," +str(te_Email.get())
        contactFile.write(contact + '\n')
        contactFile.close()   
    else:
        return

# Build frame for data entry
lf_instruct = ttk.LabelFrame(app,text="Enter Contact Information", bootstyle=PRIMARY)

lb_FirstName = ttk.Label(lf_instruct, text="First Name:")
te_FirstName = ttk.Entry(lf_instruct, width=20)
lb_FirstName.grid(row=0, column=0, padx=5, pady=5, sticky=N+S+W+E)
te_FirstName.grid(row=0, column=1, padx=5, pady=5, sticky=N+S+W+E)

lb_LastName = ttk.Label(lf_instruct, text="Last Name:")
te_LastName = ttk.Entry(lf_instruct, width=20)
lb_LastName.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+W+E)
te_LastName.grid(row=1, column=1, padx=5, pady=5, sticky=N+S+W+E)

lb_Email = ttk.Label(lf_instruct, text="Email:")
te_Email = ttk.Entry(lf_instruct, width=20)
lb_Email.grid(row=2, column=0, padx=5, pady=5, sticky=N+S+W+E)
te_Email.grid(row=2, column=1, padx=5, pady=5, sticky=N+S+W+E)

lb_spam = ttk.Label(lf_instruct, text="Spam Me:")
cb_spam = ttk.Checkbutton(lf_instruct, bootstyle=PRIMARY)
lb_spam.grid(row=3, column=0, padx=5, pady=5, sticky=N+S+W+E)
cb_spam.grid(row=3, column=1, padx=5, pady=5, sticky=N+S+W+E)

lf_instruct.grid(row=0, column=0,padx=5, pady=5, sticky=N+S+W+E)

# Place save or clear buttons in the window
b1 = ttk.Button(app, text="Clear", command=clear_form, bootstyle="OUTLINE")
b1.grid(row=1, column=0, padx=5, pady=5, sticky=N+S+W+E)

b2 = ttk.Button(app, text="Save", command=save_form, bootstyle="OUTLINE-DEFAULT")
b2.grid(row=2, column=0, padx=5, pady=5, sticky=N+S+W+E)


# Start the UI
app.mainloop()


