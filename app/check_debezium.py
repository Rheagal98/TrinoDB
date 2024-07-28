import requests
connector_name = "inventory-connector"

response = requests.get(f"http://localhost:8083/connectors/{connector_name}/status")

if response.ok:
    print(response.json())
else:
    print(response.content)
