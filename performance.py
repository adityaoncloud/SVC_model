#This is a Python script to test the deployed model's performance using the Kserve REST API.

import requests
import json

# Define the endpoint URL of the deployed model
endpoint_url = "http://my-model-predictor-default.default.10.64.140.43.nip.io"

#Enter your endpoint url

# Sample input data for testing
sample_input = {
    "data": [1.0, 2.0, 3.0, 4.0]
}

# Send a POST request to the endpoint with the sample input
response = requests.post(endpoint_url, json=sample_input)

# Check if the request was successful
if response.status_code == 200:
    # Parse the response JSON
    result = response.json()

    # Assuming the model's response contains a 'predictions' key
    predictions = result.get('predictions', [])

    # Print the predictions
    print("Predictions:", predictions)
else:
    print("Request failed with status code:", response.status_code)
    print("Response content:", response.content.decode('utf-8'))

