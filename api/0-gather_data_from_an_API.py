import requests
import sys

def fetch_employee_data(employee_id):
    # Endpoint for getting specific employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    # Endpoint for accessing TODO items for the employee
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        # Fetch employee data
        employee_response = requests.get(employee_url)
        employee_response.raise_for_status()
        employee_data = employee_response.json()

        # Fetch TODO list data
        todo_response = requests.get(todo_url)
        todo_response.raise_for_status()
        todo_data = todo_response.json()

        return employee_data, todo_data

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    employee_data, todo_data = fetch_employee_data(employee_id)

    employee_name = employee_data["name"]
    completed_tasks = [task for task in todo_data if task["completed"]]
    total_tasks = len(todo_data)

    print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t {task['title']}")

if __name__ == "__main__":
    main()
