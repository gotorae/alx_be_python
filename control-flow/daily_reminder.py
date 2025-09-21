# daily_reminder.py  (requires Python 3.10+)

task = input("Enter your task: ")

priority = input("Priority (high/medium/low): ")
while priority.lower() not in ("high", "medium", "low"):
    priority = input("Priority (high/medium/low): ")

time_bound = input("Is it time-bound? (yes/no): ")
while time_bound.lower() not in ("yes", "no"):
    time_bound = input("Is it time-bound? (yes/no): ")

priority = priority.lower()
time_bound = time_bound.lower()

match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a high priority task. Plan to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Try to complete it soon.")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a low priority task that requires immediate attention today!")
        else:
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered.")
