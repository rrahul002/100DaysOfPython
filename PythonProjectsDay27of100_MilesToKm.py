from tkinter import *

def miles2km():
  miles = float(miles_input.get())
  km = miles * 1.609
  km_result.config(text=f"{km}")

window = Tk()
window.title("Miles to Kilometers")

window.minsize(width=500, height=300)
window.config(padx=50, pady=50)

#gridder
l1 = Label(text="                                      ")
l1.grid(column=1, row=1)

#Entry
miles_input = Entry(width=7)
miles_input.grid(column=2, row= 2)

#Miles
miles_label = Label(text="Miles")
miles_label.grid(column= 3, row= 2)

#Result
km_result = Label(text="0")
km_result.grid(column= 2, row= 3)

#Km
km_label = Label(text="Kilometers")
km_label.grid(column= 3, row= 3)

#Convert
convert = Button(text="Convert!", command=miles2km)
convert.grid(column= 2, row= 4)



window.mainloop()
