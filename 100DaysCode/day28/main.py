from tkinter import *
from turtle import title
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  window.after_cancel(timer)
  # 00:00
  canvas.itemconfig(timer_text, text="00:00")
  # title_label  "Timer"
  title_label.config(text="Timer")
  # reset check_marks
  check_marks.config(text="")

  global reps
  reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
  global reps
  # if reps == 0:
  #   count_down(15)
  reps += 1
  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN *60
  long_break_sec = LONG_BREAK_MIN * 60

  # If its the 1st/3rd/5th/7yh rep:
  # WORK 25 mins
  # if its 2nd/4th/6th rep:
  # TAKE short break
  # if its 8th rep:
  # TAKE long break
  

  if reps % 8 == 0:
    count_down(long_break_sec)
    title_label.config(text="Long Break", fg= RED)
  elif reps % 2 == 0:
    count_down(short_break_sec)
    title_label.config(text="Short Break", fg= PINK)
  else:
    count_down(work_sec)
    title_label.config(text="Work", fg= GREEN)
  # count_down(5 * 60)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
  
  # "01:35"
  count_min = math.floor(count / 60)
  count_sec = count % 60

  # if count_sec == 0:
  #   count_sec = "00"
  if count_sec < 10:
    count_sec = f"0{count_sec}"

  canvas.itemconfig(timer_text, text= f"{count_min}:{count_sec}" )
  print(count)
  if count > 0:
    global timer
    timer = window.after(1000, count_down,  count-1 )
  else:
    start_timer()
    marks = ""
    work_sessions = math.floor(reps/2)
    for _ in range(work_sessions):
      marks += "✔"
    check_marks.config(text=marks)

  

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# def func_a(a,b,c):
#   print(a)
#   print(b)
#   print(c)



title_label = Label(text="Timer", fg= GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

canvas  = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="100DaysCode/day28/tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start",  fg=RED, bg=YELLOW,  font=(FONT_NAME, 15),  highlightbackground=YELLOW, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", fg=RED, bg=YELLOW,  font=(FONT_NAME, 15),  highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(column=2, row=2)

check_mark="✔"
check_marks = Label(text=check_mark, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25))
check_marks.grid(column=1, row=3)
# canvas.pack()




window.mainloop()
