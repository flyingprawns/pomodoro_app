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
start_button_disabled = False
taking_break = False
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    # Stop timer and reset display
    global timer
    window.after_cancel(timer)
    if taking_break:
        display_time(BREAK_MIN*60)
    else:
        display_time(WORK_MIN*60)
    # Re-enable start button
    global start_button_disabled
    start_button_disabled = False


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer_button():
    # Prevent user from pressing start button twice
    global start_button_disabled
    if start_button_disabled:
        return
    else:
        start_button_disabled = True
        start_timer()


def start_timer():
    # Start the work timer or break timer
    global taking_break
    if taking_break:
        header_label.config(text="Break!", fg=RED)
        countdown(3)
    else:
        header_label.config(text="Work!", fg=GREEN)
        countdown(2)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def display_time(count):
    minutes = floor(count / 60)
    seconds = "%02d" % (count % 60)
    time_display = f"{minutes}:{seconds}"
    canvas.itemconfig(timer_text, text=time_display)


def countdown(count):
    display_time(count)
    # Keep counting
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    # Countdown over!
    else:
        # Increment pomodoro count if you were working
        global taking_break
        if not taking_break:
            pomodoros_completed.set(pomodoros_completed.get() + 1)
        # "Flip" the break status
        taking_break = not taking_break
        # Start timer after 2 seconds
        window.after(2000)
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

# "Timer" label
header_label = Label(text="Timer", font=(FONT_NAME_BUTTONS, 43, "bold"), bg=YELLOW, fg=GREEN)
header_label.grid(row=1, column=2)

# "Start" Button
start_button = Button(text="Start", font=(FONT_NAME_BUTTONS, 15), command=start_timer_button)
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
