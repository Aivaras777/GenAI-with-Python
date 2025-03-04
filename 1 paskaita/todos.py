import requests

def fetch_todos():
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)

    if response.status_code == 200:
        todos = response.json()  # Get the data as JSON
        # Print the first 10 todos
        for todo in todos[:10]:
            print(f"ID: {todo['id']}, Title: {todo['title']}, Completed: {todo['completed']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

# Run the function
fetch_todos()
