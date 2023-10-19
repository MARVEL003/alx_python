import csv
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
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

total_tasks = len(todos)
done_tasks = sum(1 for todo in todos if todo.get("completed"))

print(
    f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
for todo in todos:
    if todo.get("completed"):
        print(f"\t {todo.get('title')}")

# Export to CSV
csv_filename = f'{employee_id}.csv'
with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
    # Write tasks
    for todo in todos:
        csv_writer.writerow([todo.get('"'), employee_id, employee_name,
                             todo.get("completed"), todo.get("title"), todo.get('"')])

print(f"Data exported to {csv_filename}")