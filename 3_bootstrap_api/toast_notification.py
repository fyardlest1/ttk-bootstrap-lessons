import ttkbootstrap as ttk
from ttkbootstrap.toast import ToastNotification

app = ttk.Window()

# Define the toast notice (temporary message)
toast = ToastNotification(
    title="Toast Message",
    message="This is a toast message...",
    duration=9000,
)

# Display message
toast.show_toast()

app.mainloop()



