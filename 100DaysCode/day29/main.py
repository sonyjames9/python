from random import randint, shuffle, choice
from tkinter import Button, Canvas, Entry, PhotoImage, Tk, Label, messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  password_entered = password_entry.get()
  password_entry.delete(first= 0 , last=len(password_entered))

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  # nr_letters = random.randint(8, 10)
  # nr_symbols = random.randint(2, 4)
  # nr_numbers = random.randint(2, 4)

  # password_letters = [new_item for item in list]
  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols= [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers= [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters + password_numbers + password_symbols
  shuffle(password_list)

  # password = ""
  # for char in password_list:
  #   password += char

  #replaced above 3 lines
  password = "".join(password_list)
  # print(f"Your password is: {password}")
  password_entry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()

  if len(website.strip()) == 0 or len(password.strip()) == 0:
    messagebox.showinfo(title="Oops", message="Please make sure you havent left any fields empty")
  else:
    is_ok = messagebox.askokcancel(title=website, message=f"Details entered: \n Email: {email} \n Password: {password} \n Is it okay to save?")

    if is_ok:

      with open("100DaysCode/day29/data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(first= 0 , last=len(website))
        email_entry.delete(first= 0 , last=len(email))
        password_entry.delete(first= 0 , last=len(password))
  
    
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady= 50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="100DaysCode/day29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label= Label(text="Website")
website_label.grid(row=1, column=0)

email_label= Label(text="Email/Username")
email_label.grid(row=2, column=0)

password_label= Label(text="Password")
password_label.grid(row=3, column=0)

website_entry = Entry(width=37)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=37)
email_entry.grid(row=2, column=1,  columnspan=2)
email_entry.insert(0, "sj@ymail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate_pass_button = Button(text="Create Password", command=generate_password)
generate_pass_button.grid(row=3, column=2, columnspan=1)

add_button = Button(text="Add", width=35, command=save)
add_button.grid(row=4, column=1,  columnspan=2)

# canvas.pack()
window.mainloop()