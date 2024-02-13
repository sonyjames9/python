import tkinter
from tkinter.ttk import Button, Entry

window = tkinter.Tk()
window.title("Gui Programming")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text = "I am label", font=("Arial", 12, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
  print("I clicked")
  new_text = input.get()
  # my_label.config(text="Button got clicked")
  my_label.config(text=new_text)


button = Button(text="Click me", command= button_clicked)
button.pack()

input = Entry(width=10)
input.pack()
print(input.get())

window.mainloop()