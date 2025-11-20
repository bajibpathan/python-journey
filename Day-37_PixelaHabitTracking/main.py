import requests
from datetime import datetime
import os

# Fetch sensitive credentials from environment variables for secure authentication
USERNAME = os.environ.get("USER_NAME")
TOKEN = os.environ.get("PIXEL_API_TOKEN")
GRAPH_ID = "<<YOUR_GRAPH_ID>>"

# Base endpoint for all Pixela API operations
PIXELA_ENDPOINT = "https://pixe.la/v1/users"


## -----------------------------------------
## 1. PIXELA USER CREATION
## -----------------------------------------
# Payload for creating a new Pixela user.
# This demonstrates usage of a POST request with JSON body.
user_params = {
    "token": TOKEN,                   # Unique API token for authentication
    "username": USERNAME,             # Pixela username
    "agreeTermsOfService": "yes",     # Required flag to agree with service terms
    "notMinor": "yes"                 # Confirms the user is not a minor
}

# Creating a new Pixela user account using POST method
response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
print(response.text)


## -----------------------------------------
## 2. PIXELA GRAPH CREATION
## -----------------------------------------
# Endpoint to create a new graph under the authenticated user
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

# Graph configuration defining how the habit-tracking graph behaves
graph_params = {
    "id": GRAPH_ID,               # Unique identifier for the graph
    "name": "Cycling Graph",      # Title of the activity being tracked
    "unit": "Km",                 # Unit of measurement
    "type": "float",              # Data type for pixel values
    "color": "ajisai"             # Display color of the graph
}

# Authentication header required for all operations after user creation
headers = {
    "X-USER-TOKEN": TOKEN
}

# Creating a new trackable graph using POST request
response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
print(response.text)

# NOTE: Use the following URL to visualize the created graph in a browser:
# https://pixe.la/v1/users/<YOUR_USER_NAME>/graphs/<YOUR_GRAPH_ID>.html


## -----------------------------------------
## 3. PIXEL CREATION (Adding Daily Data)
## -----------------------------------------
# Endpoint to add a new "pixel" (daily logged data point) to the graph
pixel_creation_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

# Capture today's date in the required YYYYMMDD format
today = datetime.now()

# Payload containing the pixel data (quantity logged for the day)
graph_id_params = {
    "date": today.strftime("%Y%m%d"),  # Current date
    "quantity": "10"                    # Example distance cycled
}

# Log the pixel data into the graph
# Demonstrates another POST request to update daily activity
response = requests.post(url=pixel_creation_endpoint, json=graph_id_params, headers=headers)
print(response.text)
