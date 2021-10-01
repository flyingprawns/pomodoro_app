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
BREAK_MIN = 5

# --------------------------- GLOBAL VARIABLES ---------------------------- #
taking_break = False


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global taking_break
    if taking_break:
        canvas.itemconfig(timer_text, text="5:00")
    else:
        canvas.itemconfig(timer_text, text="25:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global taking_break
    if taking_break:
        header_label.config(text="Break!", fg=RED)
        countdown(3)
    else:
        header_label.config(text="Work!", fg=GREEN)
        countdown(2)
    reset_timer()


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    # Display countdown
    minutes = floor(count / 60)
    seconds = "%02d" % (count % 60)
    time_display = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time_display)
    # Keep counting
    if count >= 0:
        window.after(1000, countdown, count-1)
    # Countdown over!
    else:
        global taking_break
        if not taking_break:
            # Increment pomodoro count
            pomodoros_completed.set(pomodoros_completed.get() + 1)
        # "Flip" the break status
        taking_break = not taking_break
        # Start timer after 3 seconds
        window.after(3000)
        start_timer()

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
header_label = Label(text="Timer", font=(FONT_NAME_BUTTONS, 43, "bold"), bg=YELLOW, fg=GREEN)
header_label.grid(row=1, column=2)

# "Start" Button
start_button = Button(text="Start", font=(FONT_NAME_BUTTONS, 15), command=start_timer)
start_button.grid(column=1, row=3, pady=5)

# "Reset" Button
start_button = Button(text="Reset", font=(FONT_NAME_BUTTONS, 15), command=reset_timer)
start_button.grid(column=3, row=3, pady=5)

# Pomodoro count tracker
pomodoros_completed = IntVar(value=0)
tracker_spinbox = Spinbox(from_=0, to=10, width=5, textvariable=pomodoros_completed)
tracker_spinbox.grid(column=2, row=4, pady=20)

# ----------------------- KEEP GUI WINDOW OPEN ------------------------ #
window.mainloop()
