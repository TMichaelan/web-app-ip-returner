import requests

headers = {
    "Accept": "application/html"
    # "Accept": "application/xml"
    # "Accept": "application/x-yaml"
    # "Accept": "application/txt"
}

response = requests.get("http://127.0.0.1:5000", headers=headers)

print(response.text)