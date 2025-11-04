import tkinter  # Import the tkinter library to create a simple GUI application

# Function to convert miles to kilometers
def miles_to_km():
    # Retrieve user input from the entry field and convert it to a float
    miles = float(miles_input.get())
    # Convert miles to kilometers (1 mile = 1.609 km) and round the result
    km = round(miles * 1.609)
    # Update the label with the converted value
    kilometer_result_label.config(text=f"{km}")

# Create the main window for the GUI
window = tkinter.Tk()
window.title("Miles to Kilometer Converter")  # Set the window title
window.config(padx=20, pady=20)  # Add padding around the content

# Entry widget for user to input miles
miles_input = tkinter.Entry(width=7)
miles_input.grid(column=1, row=0)

# Label for "Miles" text
miles_label = tkinter.Label(text="Miles")
miles_label.grid(column=2, row=0)

# Label for "is equal to" text
is_equal_to_label = tkinter.Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

# Label to display the converted kilometer result
kilometer_result_label = tkinter.Label(text="0")
kilometer_result_label.grid(column=1, row=1)

# Label for "Km" text
kilometer_label = tkinter.Label(text="Km")
kilometer_label.grid(column=2, row=1)

# Button that triggers the conversion function when clicked
calculate_button = tkinter.Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# Keep the window open and responsive until closed by the user
window.mainloop()
