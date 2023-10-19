import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 3-dictionary_of_list_of_dictionaries.py <output_filename>")
    sys.exit(1)

output_filename = sys.argv[1]
data = {}

# Fetch data for all users
for employee_id in range(1, 11):  # Assuming there are 10 users
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(url)
    employee_name = response.json().get("username")

    if not employee_name:
        print(f"No employee found with ID {employee_id}")
        continue

    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(url)
    todos = response.json()

    # Create a list of dictionaries for this user
    user_data = [{"username": employee_name, "task": todo["title"],
                  "completed": todo["completed"]} for todo in todos]

    # Add the user data to the data dictionary
    data[str(employee_id)] = user_data

# Write the data to the output file in JSON format
with open(output_filename, "w") as json_file:
    json.dump(data, json_file)

print(f"Data exported to {output_filename}")