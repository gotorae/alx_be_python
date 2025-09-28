from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date_formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date, current_date_formatted

no_of_days = int(input("Enter number of days: "))

def calculate_future_date(days, current_date):
    future_date = current_date + timedelta(days=days)  # FIXED here
    future_date_formatted = future_date.strftime("%Y-%m-%d %H:%M:%S")
    return future_date_formatted


# Get current datetime and formatted version
current_date_obj, current_date_str = display_current_datetime()

# Calculate future date
future_date_str = calculate_future_date(no_of_days, current_date_obj)

print(current_date_str, "\n", future_date_str)