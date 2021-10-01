from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=30, pady=20, bg=YELLOW)

tomato_image = PhotoImage(file="tomato.png")

canvas = Canvas(width=240, height=264, bg=YELLOW, highlightthickness=0)
canvas.create_image(115, 132, image=tomato_image)
canvas.create_text(115, 152, text="0:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.pack()

window.mainloop()
