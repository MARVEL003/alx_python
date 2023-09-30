import csv
import requests
import sys

# Function to fetch tasks for a specific user
def fetch_tasks(user_id):
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    response = requests.get(url)
    tasks = response.json()
    return tasks

# Function to export tasks to a CSV file
def export_to_csv(user_id, tasks):
    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for task in tasks:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": "Antonette",  # You can replace this with any username of your choice
                "TASK_COMPLETED_STATUS": str(task['completed']),
                "TASK_TITLE": task['title']
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    user_id = sys.argv[1]

    try:
        user_id = int(user_id)
    except ValueError:
        print("USER_ID must be an integer.")
        sys.exit(1)

    tasks = fetch_tasks(user_id)
    export_to_csv(user_id, tasks)
    print(f"Data exported to {user_id}.csv")
