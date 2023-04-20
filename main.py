from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 20
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
REPS = 0
CHECK = "✓"
clock = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(clock)
    canvas.itemconfig(text_timer, text="00:00")
    timer.config(text="Timer", fg=GREEN)
    global REPS
    REPS = 0
    global CHECK
    CHECK = "✓"
    checkmark.config(text=f"")

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global REPS
    REPS += 1
    if REPS == 1 or REPS == 3 or REPS == 5:
        count_down(WORK_MIN*60)
        timer.config(text="WORK BITCH")
    elif REPS == 2 or REPS == 4:
        count_down(SHORT_BREAK_MIN * 60)
        timer.config(text="CHILL", fg=PINK)
    elif REPS == 6:
        count_down(LONG_BREAK_MIN*60)
        timer.config(text="U. SHALL. RELAX!", fg=RED)
    if REPS % 2 == 0:
        global CHECK
        checkmark.config(text=f"{CHECK}")
        CHECK = CHECK + CHECK

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(text_timer, text=f"{count_min}:{count_sec}")
    if count > 0:
        global clock
        clock = window.after(1000, count_down, count-1)
    if count == 0:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=70, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
text_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, columnspan=3, row=2, rowspan=3)

timer = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "bold"))
timer.grid(column=2, columnspan=3, row=0, rowspan=2)
timer.config(padx=90)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=1, row=6)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=5, row=6)

checkmark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "bold"))
checkmark.grid(column=3, row=8)

window.mainloop()
