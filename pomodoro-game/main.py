from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
tracker = 0
work_count = 1
running = False

# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    global running
    running = False
    global tracker
    global work_count
    canvas.itemconfig(timer_text, text="00:00")
    tracker = 0
    work_count = 1

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start():
    global tracker
    global work_count
    global running
    running = True
    tracker += 1
    work_min_in_secs = WORK_MIN * 60
    short_break_min_in_secs = SHORT_BREAK_MIN * 60
    long_break_min_in_secs = LONG_BREAK_MIN * 60

    if tracker % 8 == 0:
        count_down(long_break_min_in_secs)
        timer_label.config(text=f"Break", fg= RED)
    elif tracker % 2 == 0:
        count_down(short_break_min_in_secs)
        timer_label.config(text=f"Break", fg= PINK)
    else:
        count_down(work_min_in_secs)
        timer_label.config(text=f"Work", fg= GREEN)
        check.config(text=f"{('✓' * work_count)}")
        work_count += 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    if not running:
        return

    count_min = math.floor(count / 60)
    count_secs = count % 60

    if count_secs == 0:
        count_secs = "00"
    elif count_secs <= 9:
        count_secs = f"0{count_secs}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_secs}")

    if count > 0 and running:
        window.after(1000, count_down, count - 1)
    elif count == 0 and running:
        start()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pamadora")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text= "Timer", font= (FONT_NAME, 50), fg= GREEN, bg= YELLOW)
timer_label.grid(row= 0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness= 0)
tomato_img = PhotoImage(file= "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill= "white", font=(FONT_NAME, 30, "normal"))
canvas.grid(row= 1, column= 1)


start_btn = Button(text= "Start",highlightthickness= 0, command= start)
start_btn.grid(row= 2, column= 0)

reset_btn = Button(text= "Reset", highlightthickness=0, command= reset)
reset_btn.grid(row=2, column=2)

check = Label(text= "✓", fg= GREEN, bg= YELLOW, font= (FONT_NAME, 35, "bold"))
check.grid(row=3, column= 1)

window.mainloop()