from tkinter import *
import time
import os
import sys


def resource_path(relative_path):
    """Get absolute path to resource"""
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# CONSTANTS - Dark Theme
DARK_BG = "#1a1a2e"
DARK_PURPLE = "#16213e"
ACCENT_PINK = "#e94560"
ACCENT_CYAN = "#0f3460"
LIGHT_TEXT = "#eaeaea"
WORK_COLOR = "#00d4ff"
BREAK_COLOR = "#ff6b9d"
LONG_BREAK_COLOR = "#c44569"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repetitions = 0
timer = None

def count_down(count):
    minutes = count//60
    seconds = count%60
    if seconds<10:
       canvas.itemconfig(timer_text, text=f"{minutes}:0{seconds}")
    elif minutes<10:
       canvas.itemconfig(timer_text, text=f"0{minutes}:{seconds}")
    else:
       canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count>0:
       global timer
       timer = window.after(1000, count_down, count-1)
    else:
       start_timer()


def start_timer():
    global repetitions
    repetitions += 1
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    
    if repetitions % 8 == 0:
       timer_label["text"] = "   LONG BREAK   "
       timer_label["fg"] = LONG_BREAK_COLOR
       count_down(long_break_time)
    elif repetitions % 2 == 0:
       timer_label["text"] = "  SHORT BREAK  "
       timer_label["fg"] = BREAK_COLOR
       count_down(short_break_time)
    else:
       timer_label["text"] = "   WORK TIME    "
       timer_label["fg"] = WORK_COLOR
       count_down(work_time)
    
    # Update check marks and session counter
    work_sessions = repetitions // 2
    check_marks = "●" * work_sessions
    check_mark["text"] = check_marks
    session_counter["text"] = f"SESSIONS: {work_sessions:02d}"

def reset_timer():
    global repetitions, timer
    if timer is not None:
        window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label["text"] = "POMODORO TIMER"
    timer_label["fg"] = LIGHT_TEXT
    check_mark["text"] = ""
    session_counter["text"] = "SESSIONS: 0"
    repetitions = 0


# UI setup
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=40, bg=DARK_BG)
window.resizable(False, False)

timer_label = Label(window, width=20)
timer_label["text"] = "POMODORO TIMER"
timer_label.config(fg=LIGHT_TEXT, font=(FONT_NAME, 28, "bold"), highlightthickness=0, bg=DARK_BG, anchor="center")
timer_label.grid(column=1, row=0, pady=20)


canvas = Canvas(window, width=200, height=223, bg=DARK_BG, highlightthickness=0)
background_photo = PhotoImage(file=resource_path("tomato.png"))
canvas.create_image(100, 110, image=background_photo)
timer_text = canvas.create_text(114, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill=LIGHT_TEXT)
canvas.grid(column=1, row=1)

star_button = Button(
    window,
    text="START", 
    highlightthickness=0, 
    command=start_timer,
    bg=WORK_COLOR,
    fg=DARK_BG,
    font=(FONT_NAME, 12, "bold"),
    width=8,
    pady=10,
    border=0,
    cursor="hand2"
)
star_button.grid(column=0, row=2, pady=20, padx=10)

reset_button = Button(
    window,
    text="RESET", 
    highlightthickness=0, 
    command=reset_timer,
    bg=ACCENT_PINK,
    fg=DARK_BG,
    font=(FONT_NAME, 12, "bold"),
    width=8,
    pady=10,
    border=0,
    cursor="hand2"
)
reset_button.grid(column=2, row=2, pady=20, padx=10)

check_mark = Label(window, fg=WORK_COLOR, bg=DARK_BG, font=(FONT_NAME, 24), height=1, width=20)
check_mark.grid(column=1, row=3, pady=10)

session_counter = Label(
    window,
    text="SESSIONS: 00", 
    fg=LIGHT_TEXT, 
    bg=DARK_BG, 
    font=(FONT_NAME, 12, "bold"),
    width=20
)
session_counter.grid(column=1, row=4, pady=5)

window.mainloop()