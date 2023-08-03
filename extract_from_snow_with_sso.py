# Extract a list of incidents from ServiceNow using SSO and Python:
# 24-Feb-2023

import requests
import json

# Set the API endpoint and parameters
endpoint = "https://yourinstance.service-now.com/api/now/table/incident"
params = {'sysparm_limit': '100'}

# Set the headers for the API request
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'X-UserToken': 'your_SSO_token'
}

# Make the API request using the requests library
response = requests.get(endpoint, params=params, headers=headers)

# If the request was successful, parse the response JSON
if response.status_code == 200:
    data = response.json()

    # Extract the incident records from the response
    incidents = data['result']

    # Print the incident records
    for incident in incidents:
        print(incident['number'], incident['short_description'])

else:
    print('Error:', response.status_code, response.text)