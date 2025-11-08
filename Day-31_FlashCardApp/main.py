import tkinter
import pandas
import random

# ---------------------------- CONSTANTS ------------------------------- #
BACKGROUND_COLOR = "#B1DDC6"  # Light greenish background color for a soothing UI
current_card = {}             # Stores the currently displayed flashcard
to_learn = {}                 # Stores the list of words that are yet to be learned

# ---------------------------- DATA HANDLING ------------------------------- #
# Attempt to load progress (words not yet learned). If not found, load the original dataset.
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    # If user is running the app for the first time, load the full dataset
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # Load progress file so learning can continue from where the user left off
    to_learn = data.to_dict(orient="records")


# ---------------------------- FUNCTION: SHOW NEXT CARD ------------------------------- #
def next_card():
    """Display a new random French word from the list."""
    global current_card, flip_timer

    # Cancel any existing timer to prevent overlapping flips
    window.after_cancel(flip_timer)

    # Randomly choose a new word pair from the remaining list
    current_card = random.choice(to_learn)
    french_word = current_card["French"]

    # Update the canvas with the new word and reset the card front
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word, fill="black")
    canvas.itemconfig(canvas_background, image=card_front_image)

    # Automatically flip the card after 3 seconds
    flip_timer = window.after(3000, func=flip_card)


# ---------------------------- FUNCTION: FLIP CARD ------------------------------- #
def flip_card():
    """Flip the flashcard to show the English translation."""
    english_word = current_card["English"]

    # Change text and card background to indicate the card flip
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=english_word, fill="white")
    canvas.itemconfig(canvas_background, image=card_back_image)


# ---------------------------- FUNCTION: MARK WORD AS KNOWN ------------------------------- #
def is_known():
    """Remove the known word from the list and save progress."""
    to_learn.remove(current_card)

    # Save the updated list of words to continue learning next time
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)

    # Display the next word immediately
    next_card()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Flashy - Flashcard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Flip card after 3 seconds
flip_timer = window.after(3000, func=flip_card)

# Create the main canvas to hold the flashcard images and text
canvas = tkinter.Canvas(width=800, height=525, bg=BACKGROUND_COLOR, highlightthickness=0)

# Load card front and back images
card_front_image = tkinter.PhotoImage(file="images/card_front.png")
card_back_image = tkinter.PhotoImage(file="images/card_back.png")

# Display initial card front
canvas_background = canvas.create_image(410, 270, image=card_front_image)

# Text placeholders for word and language title
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# ---------------------------- BUTTONS ------------------------------- #
# Wrong (Unknown) button to skip or see next card
cross_image = tkinter.PhotoImage(file="images/wrong.png")
unknown_button = tkinter.Button(image=cross_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

# Right (Known) button to mark a word as learned
check_image = tkinter.PhotoImage(file="images/right.png")
known_button = tkinter.Button(image=check_image, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1)

# Show the first flashcard when the app starts
next_card()

# Keep the window open
window.mainloop()
