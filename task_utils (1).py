from validation import validate_task_title, validate_task_description, validate_due_date

tasks = []

def add_task(title, description, due_date):
    if not validate_task_title(title) or not validate_task_description(description) or not validate_due_date(due_date):
        print("Invalid input!")
        return
    
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added!")
    
def mark_task_as_complete(task_index):
    try:
        if 0 <= task_index - 1 < len(tasks):
            tasks[task_index - 1]["completed"] = True
            print("Task completed!")
        else:
            print("Task not found!")
    except:
        print("Invalid task number!")
    
def view_pending_tasks():
    pending = [t for t in tasks if not t["completed"]]
    if not pending:
        print("No pending tasks.")
        return
    for i, task in enumerate(pending, 1):
        print(f"{i}. {task['title']} - Due: {task['due_date']}")

def calculate_progress():
    if not tasks:
        print("No tasks.")
        return
    completed = sum(1 for t in tasks if t["completed"])
    total = len(tasks)
    percentage = (completed / total) * 100
    print(f"Progress: {completed}/{total} ({percentage:.1f}%)")