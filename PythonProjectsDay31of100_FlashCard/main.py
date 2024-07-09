from tkinter import *
from pandas import *
from random import *

BACKGROUND_COLOR = "#B1DDC6"

#-----WORDS IMPORT-----#
data = read_csv("data/french_words.csv")
Fr_En = {row.French: row.English for (index, row) in data.iterrows()}
temp_dict = Fr_En.copy()

current_word = None  # Variable to store the current word being displayed
timer_id = None  # To store the ID of the timer

#-----NEXT WORD FUNCTION-----#
def right_next_word():
    global current_word, timer_id
    if temp_dict:
        current_word = choice(list(temp_dict.items()))
        temp_dict.pop(current_word[0])
        language_label.config(text="French", bg="white", fg="black")
        word_label.config(text=current_word[0],bg="white", fg="black")
        cancel_timer()
        timer_id = window.after(5000, flip_card_to_back)
        canvas.itemconfig(canvas_img, image=FlashCard_front)

def wrong_next_word():
    global current_word, timer_id
    if temp_dict:
        current_word = choice(list(temp_dict.items()))
        language_label.config(text="French",bg="white", fg="black")
        word_label.config(text=current_word[0],bg="white", fg="black")
        cancel_timer()
        timer_id = window.after(5000, flip_card_to_back)
        canvas.itemconfig(canvas_img, image=FlashCard_front)
        words2learn = open("Words2Learn.txt", "a")
        words2learn.write(f"{current_word[0]} || {current_word[1]}\n")

#-----WORD REVEAL FUNCTION-----#
def flip_card_to_back():
    canvas.itemconfig(canvas_img, image=FlashCard_back)
    language_label.config(text="English", font=("Arial", 40, "italic"), bg=BACKGROUND_COLOR, fg="white")
    word_label.config(text=current_word[1], font=("Arial", 60, "bold"), bg=BACKGROUND_COLOR, fg="white")

def flip_card_to_front():
    canvas.itemconfig(canvas_img, image=FlashCard_front)
    language_label.config(text="French", font=("Arial", 40, "italic"), bg="white", fg="black")
    word_label.config(text=current_word[0], font=("Arial", 60, "bold"), bg="white", fg="black")

#-----CANCEL TIMER FUNCTION-----#
def cancel_timer():
    global timer_id
    if timer_id:
        window.after_cancel(timer_id)
        timer_id = None

#-----UI SETUP-----#
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=800, bg=BACKGROUND_COLOR, highlightthickness=0)
FlashCard_front = PhotoImage(file="images/card_front.png")
FlashCard_back = PhotoImage(file="images/card_back.png")

canvas_img = canvas.create_image(400, 270, image=FlashCard_front)
canvas.place(x=50, y=50)

checkmark = PhotoImage(file="images/right.png")
checkmark_button = Button(window, image=checkmark, highlightthickness=0, command=right_next_word)
checkmark_button.place(x=900, y=175)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(window, image=wrong, highlightthickness=0, command=wrong_next_word)
wrong_button.place(x=900, y=350)

language_label = Label(text="Language", font=("Arial", 40, "italic"), bg="white", fg="black")
language_label.place(x=300, y=200)

word_label = Label(text="Word", font=("Arial", 60, "bold"), bg="white", fg="black")
word_label.place(x=300, y=325)

window.mainloop()
