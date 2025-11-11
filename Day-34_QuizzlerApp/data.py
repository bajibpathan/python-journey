import requests

# ---------------------------- FETCH QUESTIONS FROM API ---------------------------- #
# Using Open Trivia DB API to dynamically retrieve 10 computer science questions.
parameters = {
    "amount": 10,          # Number of questions
    "category": 18,        # 18 = Science: Computers
    "difficulty": "easy",  # Difficulty level
    "type": "boolean"      # True/False questions
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]
