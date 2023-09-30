import json
import requests
import sys

# Function to fetch tasks for a specific user
def fetch_tasks(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    tasks = response.json()
    return tasks

# Function to export tasks to a JSON file
def export_to_json(user_id, tasks):
    data = {str(user_id): []}
    
    for task in tasks:
        data[str(user_id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": "Antonette"  # Replace with the actual username if needed
        })
    
    filename = f"{user_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_id = int(user_id)
    except ValueError:
        print("USER_ID must be an integer.")
        sys.exit(1)

    tasks = fetch_tasks(user_id)
    export_to_json(user_id, tasks)
    print(f"Data exported to {user_id}.json")
