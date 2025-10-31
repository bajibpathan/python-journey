# -------------------------------
# Mail Merge Automation Project
# -------------------------------
# This script automates the process of generating personalized letters
# from a single template and a list of invitee names.
# It reads the template, replaces the placeholder with each person's name,
# and saves the customized letters to the "Output" folder.
# -------------------------------

# Define the placeholder text used in the letter template
PLACE_HOLDER = "[name]"

# Step 1: Read all the invitee names from the names file
# Each name appears on a new line in the file
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Step 2: Read the template letter from the file
# This letter contains a placeholder like [name] that will be replaced
with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

# Step 3: Generate a personalized letter for each invitee
for name in names:
    stripped_name = name.strip()  # Remove any whitespace or newline characters
    # Replace the placeholder with the actual name
    new_letter = letter_content.replace(PLACE_HOLDER, stripped_name)
    
    # Step 4: Save the new letter in the "ReadyToSend" folder
    # Each file is named uniquely using the invitee's name
    with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as ready_letter:
        ready_letter.write(new_letter)

# 🎯 Output:
# The script will create one personalized letter per name in the list,
# ready to send from the "./Output/ReadyToSend" directory.
