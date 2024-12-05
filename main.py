from tkinter import *
import math


# CONSTANTS
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------

#timer reset
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    checkmark_label.config(text="")
    global reps
    reps = 0

#timer mechanism
def start_timer():
    global reps
    reps += 1
    if reps in (1,3,5,7):
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    elif reps in (2,4,6):
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
    elif reps == 8:
        count_down(LONG_BREAK_MIN)
        timer_label.config(text="Long Break", fg=RED)
        reps = 0

#countdown mechanism
def count_down(count):

    minutes = math.floor(count / 60)
    seconds = round(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")

    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps in (3,7):
            checkmark_label.config(text="✔")





# UI SETUP
window = Tk()
window.title("Pomodoro")
window.minsize(300,300)
window.config(bg=YELLOW, padx=20, pady=20)



canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)



# timer label
timer_label = Label(text="Timer", font=(FONT_NAME, 45), bg=YELLOW, fg=GREEN)
timer_label.grid(column=2, row=1)

# countdown label
# countdown_label = Label(text="time")
# countdown_label.grid(column=2,row=2)

# start button
start_button = Button(text="Start", bg=YELLOW, highlightbackground=YELLOW)
start_button.grid(column=1, row=3)

start_button.config(command=start_timer)

#checkmark label
checkmark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 18))
checkmark_label.grid(column=2,row=4)

# reset button
reset_button = Button(text="Reset", highlightbackground=YELLOW)
reset_button.grid(column=3, row=3)
reset_button.config(command=reset_timer)


window.mainloop()