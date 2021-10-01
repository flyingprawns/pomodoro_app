from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME_TIMER = "Courier"
FONT_NAME_BUTTONS = "Arial"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    pass


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    countdown(WORK_MIN*60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = floor(count / 60)
    seconds = count % 60
    time_display = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time_display)
    if count > 0:
        window.after(1000, countdown, count-1)


# ------------------------------ POMODORO TRACKER ------------------------------- #
def tracker_spinbox_used():
    pass


# ---------------------------- UI SETUP ------------------------------- #
# Main window
window = Tk()
window.title("Pomodoro")
window.config(padx=30, bg=YELLOW)

# Tomato image + timer display
tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=240, height=264, bg=YELLOW, highlightthickness=0)
canvas.create_image(119, 132, image=tomato_image)
timer_text = canvas.create_text(119, 152, text="0:00", fill="white", font=(FONT_NAME_TIMER, 35, "bold"))
canvas.grid(row=2, column=2)

# "Timer" text
timer_label = Label(text="Timer", font=(FONT_NAME_BUTTONS, 43, "bold"), bg=YELLOW, fg=GREEN)
timer_label.grid(row=1, column=2)

# "Start" Button
start_button = Button(text="Start", font=(FONT_NAME_BUTTONS, 15), command=start_timer)
start_button.grid(column=1, row=3, pady=5)

# "Reset" Button
start_button = Button(text="Reset", font=(FONT_NAME_BUTTONS, 15), command=reset_timer)
start_button.grid(column=3, row=3, pady=5)

# Pomodoro count tracker
tracker_spinbox = Spinbox(from_=0, to=10, width=5, command=tracker_spinbox_used)
tracker_spinbox.grid(column=2, row=4, pady=20)

# ----------------------- KEEP GUI WINDOW OPEN ------------------------ #
window.mainloop()
