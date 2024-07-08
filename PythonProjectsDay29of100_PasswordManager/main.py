from tkinter import *
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_pswd():
  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)
  
  password_list = []

  password_letters = [random.choice(letters) for char in range(nr_letters)]
  password_symbols = [random.choice(numbers) for char in range(nr_numbers)]
  password_numbers = [random.choice(symbols) for char in range(nr_symbols)]

  password_list = password_letters + password_numbers + password_symbols
  random.shuffle(password_list)
  
  password = "".join(password_list)


  password_entry.delete(0,END)
  password_entry.insert(0,password)


  

# ---------------------------- SAVE PASSWORD ------------------------------- #

def add_entry():
  website = website_entry.get()
  user = username_entry.get()
  pswd = password_entry.get()

  if len(website)==0 or len(user)==0 or len(pswd)==0:
    messagebox.showinfo(title="Error", message="One of your fields is empty! Please try again!")

  else:
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details you entered:\nEmail/Username: {user}\nPassword: {pswd}\nWebsite: {website}\nIs it ok to save?")
  
  
    if is_ok:
      user_pwd_file = open("MyPass.txt", "a")
      user_pwd_file.write(f"\n{website} | {user} | {pswd}\n")
      user_pwd_file.close()
      website_entry.delete(0,END)
      username_entry.delete(0,END)
      username_entry.insert(0, user)
      password_entry.delete(0,END)
    
  
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg= "white", highlightthickness=0)
MyPass = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=MyPass)
canvas.grid(column=1, row=0)

website_label = Label(text="Website: ", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_label = Label(text="Email/Username: ", bg="white")
username_label.grid(column=0, row=2)

username_entry = Entry(width=35)
username_entry.grid(column=1, row=2, columnspan=2)

password_label = Label(text="Password: ", bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=18)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_pswd)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add_entry)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()