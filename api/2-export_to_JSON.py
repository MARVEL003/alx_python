import json
import requests
import sys


if len(sys.argv) != 2:
    print("Usage: python3 2-export_to_JSON.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]
url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = requests.get(url)
employee_name = response.json().get("username")

if not employee_name:
    print(f"No employee found with ID {employee_id}")
    sys.exit(1)

url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
response = requests.get(url)
todos = response.json()

# Prepare the data in JSON format
# Initialize as a list of dicts `employee_id` as the key and [] as the value

employee_tasks = []
for todo in todos:
    task_data = {
        "task": todo.get("title"),
        "completed": todo.get("completed"),
        "username": employee_name
    }
    employee_tasks.append(task_data)


output_file = f"{employee_id}.json"

with open(output_file, 'w') as json_file:
    json.dump({employee_id: employee_tasks}, json_file, indent=4)

print(f"Data exported to {output_file}")