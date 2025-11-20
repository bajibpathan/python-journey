# 🚴 Pixela Habit Tracking Automation  
_A simple Python automation project demonstrating the usage of multiple Pixela API endpoints including user creation, graph creation, and pixel logging._

## 📌 Project Overview
This project showcases how to interact with the **Pixela API**, a service that allows users to track habits and activities visually using graphs.  
Using Python and the `requests` library, the script performs:

1. **User Account Creation**  
2. **Graph Creation for Habit Tracking**  
3. **Daily Pixel Logging (Activity Tracking)**  

This is ideal for beginners learning **REST APIs**, **POST requests**, **JSON payload handling**, and **authentication using headers**.

---

## 🚀 Features Demonstrated

### ✓ **1. User Creation API**
Creates a Pixela account via:
```http
POST https://pixe.la/v1/users
```
Includes required fields such as token, username, and terms agreement.

---

### ✓ 2. Graph Creation API

Builds a custom habit graph:
```http
POST https://pixe.la/v1/users/<username>/graphs
```

Defines:

- Graph ID
- Name
- Unit (Km)
- Data type (float)
- Color

This graph visually represents your habit progress.

----

### ✓ 3. Pixel Creation API

Logs a daily activity "pixel" representing the progress tracked:

```http
POST https://pixe.la/v1/users/<username>/graphs/<graphId>
```

In this example, the script logs 10 Km cycled for the current day.

---

## 📂 Project Structure

```
pixelahabbittracking/
│── main.py        # Contains API requests for user, graph, and pixel creation
│── README.md      # Project documentation

```

---

## 🔧 Environment Variables

Before running the script, set the following variables:

|Variable Name|	Purpose|
|--|--|
|USER_NAME|	Your Pixela username|
|PIXEL_API_TOKEN|	API token for authentication|
|GRAPH_ID|	Unique graph identifier|

Example (Linux/macOS):

```bash
export USER_NAME="your_username"
export PIXEL_API_TOKEN="your_token"
export GRAPH_ID="cycling-graph"
```

---

## ▶️ How to Run

Install dependencies:
```bash
pip install requests
```

Execute the script:
```bash
python main.py
```

View your graph in the browser:
```bash
https://pixe.la/v1/users/<YOUR_USER_NAME>/graphs/<YOUR_GRAPH_ID>.html
```

---

## 🎯 Learning Outcomes

By working with this project, you will learn:

- How to interact with REST APIs using Python
- How to structure POST requests with JSON bodies
- How to handle headers for authentication
- How to work with dynamic URLs
- How to store and use environment variables securely

---

## 📝 Notes

- Ensure your token and username are stored securely.
- Pixela API will return meaningful messages if something goes wrong — check the response prints.
- You may extend this project by adding update/delete pixel, graph deletion, or scheduling automated runs.

---

## 🙌 Credits

Project inspired by Python 100 Days of Code Bootcamp by Angela Yu.
Created as part of Python learning projects.

---

## 📜 License

This project is open for educational and learning purposes.
Feel free to fork and experiment.
