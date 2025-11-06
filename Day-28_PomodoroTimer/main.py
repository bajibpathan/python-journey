import tkinter
import math

# ---------------------------- CONSTANTS ------------------------------- #
# Define UI colors, fonts, and timer durations (in minutes)
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 25         # Duration of work session
SHORT_BREAK_MIN = 5   # Duration of short break
LONG_BREAK_MIN = 20   # Duration of long break

# Global variables to track session counts and timer reference
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    """Resets the timer, UI labels, and checkmarks to their initial state."""
    global reps
    window.after_cancel(timer)  # Stops the current countdown
    reps = 0
    title_label.config(text="Timer", fg=GREEN)
    check_marks.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    """Starts the timer and manages work/break cycles based on Pomodoro rules."""
    global reps
    reps += 1  # Increment repetition count to track work/break sessions

    # Convert minutes to seconds
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # Every 8th repetition triggers a long break
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    # Every even repetition (except 8th) triggers a short break
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    # Odd repetitions trigger a work session
    else:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    """Handles the countdown logic, updating the timer every second."""
    count_min = math.floor(count / 60)
    count_sec = count % 60

    # Display seconds with leading zero (e.g., 5 → 05)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # Update timer text on the canvas
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    # Continue countdown until zero is reached
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        # Automatically start next session when current one ends
        start_timer()
        # Add a checkmark for each completed work session
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
# Create main application window
window = tkinter.Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=20, bg=YELLOW)

# Canvas setup with background tomato image and timer text
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Title label showing the current session ("Timer", "Work", "Break")
title_label = tkinter.Label(text="Timer", bg=YELLOW, fg=GREEN,
                            font=(FONT_NAME, 50))
title_label.grid(row=0, column=1)

# Label displaying checkmarks for completed work sessions
check_marks = tkinter.Label(bg=YELLOW, fg=GREEN)
check_marks.grid(row=4, column=1)

# Start button to initiate Pomodoro cycles
start_btn = tkinter.Button(text="Start", highlightbackground=YELLOW,
                           command=start_timer)
start_btn.grid(row=3, column=0)

# Reset button to clear timer and restart the session
reset_btn = tkinter.Button(text="Reset", highlightbackground=YELLOW,
                           command=reset_timer)
reset_btn.grid(row=3, column=2)

# Keeps the GUI window active and responsive
window.mainloop()
