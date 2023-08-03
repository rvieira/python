import requests
import json

# Set the API endpoint and headers
endpoint = "https://yourinstance.service-now.com/api/now/table/sys_user?sysparm_limit=1"
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

# Make the API request using the requests library
response = requests.get(endpoint, headers=headers)

# If the request was successful, parse the response JSON and extract the SSO token
if response.status_code == 200:
    data = response.json()
    sso_token = data['result'][0]['x_user_token']
    print('SSO token:', sso_token)
else:
    print('Error:', response.status_code, response.text)