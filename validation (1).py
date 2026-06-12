def validate_task_title(title):
    return len(title) > 0
    
def validate_task_description(description):
    return len(description) > 0
    
def validate_due_date(due_date):
    try:
        parts = due_date.split("-")
        return len(parts) == 3
    except:
        return False