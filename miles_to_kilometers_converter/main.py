from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=20, pady=20)

def miles_to_kilometers():
    miles = float(miles_input.get())
    km = round(miles * 1.60934, 2)
    result_label.config(text=f"{km}")

# Input field
miles_input = Entry(width=10)
miles_input.insert(END, "")  
miles_input.grid(row=0, column=1)

# Miles Label
miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

# "is equal to" Label
is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

# Result Label (displays conversion result)
result_label = Label(text="0")
result_label.grid(row=1, column=1)

# Km Label
km_label = Label(text="Km")
km_label.grid(row=1, column=2)

# Convert Button
convert_button = Button(text="Convert", command=miles_to_kilometers)
convert_button.grid(row=2, column=1)

window.mainloop() 