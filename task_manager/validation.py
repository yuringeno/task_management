def validate_task_title(title):
    if not isinstance(title, str):
        raise ValueError("Title must be text.")
    if len(title.strip()) == 0:
        raise ValueError("Title cannot be empty.")
    if len(title) > 100:
        raise ValueError("Title cannot exceed 100 characters.")
    return True
    
def validate_task_description(description):
    if not isinstance(description, str):
        raise ValueError("Description must be text.")
    if len(description.strip()) == 0:
        raise ValueError("Description cannot be empty.")
    if len(description) > 500:
        raise ValueError("Description cannot exceed 500 characters.")
    return True
    
def validate_due_date(due_date):
    if not isinstance(due_date, str):
        raise ValueError("Due date must be text.")
    try:
        parts = due_date.split("-")
        if len(parts) != 3:
            raise ValueError("Due date format must be YYYY-MM-DD.")
        year, month, day = parts
        if not (year.isdigit() and month.isdigit() and day.isdigit()):
            raise ValueError("Year, month, and day must be numbers.")
        month_int = int(month)
        day_int = int(day)
        if not (1 <= month_int <= 12):
            raise ValueError("Month must be between 01 and 12.")
        if not (1 <= day_int <= 31):
            raise ValueError("Day must be between 01 and 31.")
        return True
    except ValueError as e:
        raise ValueError(f"Invalid due date format. Use YYYY-MM-DD.")
