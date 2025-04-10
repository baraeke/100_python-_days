from tkinter import *

MY_NAME = "Eke Ifiemi"

window = Tk()
window.title("About Me")
window.minsize(width=100, height=100)

def send_msg():
    # Name label and entry
    name_label = Label(text="Name")
    name_label.grid(row=2, column=1, sticky="w", padx=10)

    senders_name = Entry(width=40)
    senders_name.insert(END, "Enter your full name here.")
    senders_name.grid(row=3, column=1, pady=(0, 10))

    # Message label and text box
    msg_label = Label(text="Message")
    msg_label.grid(row=4, column=1, sticky="w", padx=10)

    msg = Text(width=40, height=5)
    msg.insert(END, "Enter your message here.")
    msg.grid(row=5, column=1)

    # Submit button
    def submit():
        name = senders_name.get()
        message = msg.get("1.0", END)
        print("Sender's Name:", name)
        print("Message:", message)

    submit_btn = Button(text="Submit", command=submit)
    submit_btn.grid(row=6, column=1, pady=10)

# Top-left: Header
header = Label(text=MY_NAME, font=("Arial", 14, "bold"))
header.grid(row=0, column=0, sticky="w", padx=10, pady=10)

# Top-right: Button
want_to_send_msg_btn = Button(text="Send Me Message", command=send_msg)
want_to_send_msg_btn.grid(row=0, column=2, sticky="e", padx=10, pady=10)

# Middle center: Description
description = Label(
    text="""I'm a passionate software engineer and educational technologist with experience in building applications, teaching programming, and integrating technology into education. I enjoy creating user-friendly tools and exploring how tech can solve real-life problems, especially in EdTech, FinTech, and mental health.""",
    wraplength=380,
    justify="center",
    font=("Arial", 5)
)
description.grid(row=1, column=1, padx=10, pady=(0, 10))

window.mainloop()
