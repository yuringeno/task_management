from task_manager.task_utils import add_task, mark_task_as_complete, view_pending_tasks, calculate_progress

def main():
    while True:
        print("\n" + "="*40)
        print("TASK MANAGEMENT SYSTEM")
        print("="*40)
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. View Pending Tasks")
        print("4. View Progress")
        print("5. Exit")
        print("="*40)
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            print("\n--- Add New Task ---")
            title = input("Enter task title: ").strip()
            description = input("Enter task description: ").strip()
            due_date = input("Enter due date (YYYY-MM-DD): ").strip()
            add_task(title, description, due_date)
            
        elif choice == "2":
            print("\n--- Mark Task as Complete ---")
            view_pending_tasks()
            try:
                task_num = int(input("Enter task number to mark complete: "))
                mark_task_as_complete(task_num)
            except ValueError:
                print("Error: Please enter a valid task number.")
            
        elif choice == "3":
            print("\n--- Pending Tasks ---")
            view_pending_tasks()
            
        elif choice == "4":
            print("\n--- Task Progress ---")
            calculate_progress()
            
        elif choice == "5":
            print("\nThank you for using Task Manager. Goodbye!")
            break
        else:
            print("Error: Invalid choice. Please enter a number between 1 and 5.")
        
if __name__ == "__main__":
    main()
