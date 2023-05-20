import requests
import json

query = ''  # Search query for '' in code contents
url = f"https://api.github.com/search/code?q={query}&language=javascript&page=2"

# Add your GitHub access token in the headers to increase API rate limits
headers = {'Authorization': 'bearer'}

response = requests.get(url, headers=headers)  # Send the GET request to the API with your access token

if response.status_code == 200:  # If the request was successful
    data = response.json()  # Extract the JSON data from the response
    items = data["items"]  # Extract the list of search results from the JSON data

    # Write the search results to a JSON file
    with open('search_results.json', 'w') as f:
        json.dump(items, f)

    # Process the search results as needed
    for item in items:
        repository = item["repository"]["full_name"]
        file_name = item["name"]
        file_url = item["html_url"]
        print(f"{repository}/{file_name}: {file_url}")
else:
    print(f"Error: {response.status_code} - {response.reason}")
