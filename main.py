from tkinter import *
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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_timer.config(text="Timer")
    check_mark.config(text=" ")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label_timer.config(text="LONG BREAK", fg=PINK, font=(FONT_NAME,40,"bold"), bg=YELLOW)
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label_timer.config(text="SHORT BREAK", fg=PINK, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
    else:
        countdown(work_sec)
        label_timer.config(text="WORK TIME", fg=PINK, font=(FONT_NAME, 40, "bold"), bg=YELLOW)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec <10:
        count_sec = f"0{count_sec}"

    if count_min <10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,countdown, count - 1)
    else:
        start_timer()
        marks=""
        work_sessions =math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


label_timer = Label(text= "Timer", font=(FONT_NAME,40,"bold"), fg=GREEN,bg=YELLOW)
label_timer.grid(column=1, row=0)

canvas = Canvas(window, width=200, height=224,background=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00",fill="white",font=(FONT_NAME,25, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",  command=reset_time)
reset_button.grid(column=2, row=2)

check_mark = Label(text=" ", fg=GREEN, bg=YELLOW, font=(FONT_NAME,20, "bold"))
check_mark.grid(column=1, row=3)

window.mainloop()