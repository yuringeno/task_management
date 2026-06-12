def validate_task_title(title):
    if not isinstance(title, str):
        return False, "Error: Title must be text."
    if len(title.strip()) == 0:
        return False, "Error: Title cannot be empty."
    if len(title) > 100:
        return False, "Error: Title cannot exceed 100 characters."
    return True, "Title is valid."
    
def validate_task_description(description):
    if not isinstance(description, str):
        return False, "Error: Description must be text."
    if len(description.strip()) == 0:
        return False, "Error: Description cannot be empty."
    if len(description) > 500:
        return False, "Error: Description cannot exceed 500 characters."
    return True, "Description is valid."
    
def validate_due_date(due_date):
    if not isinstance(due_date, str):
        return False, "Error: Due date must be text."
    try:
        parts = due_date.split("-")
        if len(parts) != 3:
            return False, "Error: Due date format must be YYYY-MM-DD."
        year, month, day = parts
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            return False, "Error: Year, month, and day must be numbers."
        month_int = int(month)
        day_int = int(day)
        if not (1 <= month_int <= 12):
            return False, "Error: Month must be between 01 and 12."
        if not (1 <= day_int <= 31):
            return False, "Error: Day must be between 01 and 31."
        return True, "Due date is valid."
    except Exception as e:
        return False, f"Error: Invalid due date format. Use YYYY-MM-DD."
