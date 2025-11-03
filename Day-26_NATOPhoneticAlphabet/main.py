# ---------------------------------------------
# NATO Phonetic Alphabet Project
# ---------------------------------------------
# This Python program converts any given word
# into its NATO phonetic alphabet equivalent.
#
# Example:
# Input:  "HELLO"
# Output: ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
#
# It demonstrates:
# - Reading CSV data with pandas
# - Creating a dictionary from tabular data
# - Using list comprehension for transformation
# ---------------------------------------------

import pandas

# ---------------------------------------------
# STEP 1: READ THE CSV DATA
# ---------------------------------------------
# The CSV file (nato_phonetic_alphabet.csv) contains
# two columns: 'letter' and 'code'
# Example:
# A, Alfa
# B, Bravo
# C, Charlie
# ...
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# ---------------------------------------------
# STEP 2: CREATE A DICTIONARY FROM THE DATA
# ---------------------------------------------
# Iterate through each row of the DataFrame and build
# a dictionary mapping each letter to its phonetic code.
# Example result:
# {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', ...}
phonetic_dic = {row.letter: row.code for (index, row) in data.iterrows()}

# ---------------------------------------------
# STEP 3: GET USER INPUT
# ---------------------------------------------
# Ask the user for a word to convert.
# Convert it to uppercase to match dictionary keys.
word = input("Enter a word: ").upper()

# ---------------------------------------------
# STEP 4: CONVERT WORD TO PHONETIC CODES
# ---------------------------------------------
# Use list comprehension to replace each letter
# with its corresponding NATO phonetic code.
# Example:
# word = "HELLO"
# output_list = ['Hotel', 'Echo', 'Lima', 'Lima', 'Oscar']
output_list = [phonetic_dic[letter] for letter in word]

# ---------------------------------------------
# STEP 5: DISPLAY THE RESULT
# ---------------------------------------------
print(output_list)
