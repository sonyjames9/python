from tkinter import Tk
from tkinter.ttk import Button, Entry, Label

def miles_to_km():
  miles = float(miles_input.get())
  km =  miles * 1.609
  km_result_label.config(text=f"{km}")

window = Tk()
window.title("Miles to KM")
window.config(padx=30, pady= 30)

miles_input =  Entry(width=7)
miles_input.grid(column=0, row =0)

miles_label = Label(text="miles")
miles_label.grid(column=2, row =0)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row =1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row =1)

km_label = Label(text="Km")
km_label.grid(column=2, row =1)

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row =2)

window.mainloop()