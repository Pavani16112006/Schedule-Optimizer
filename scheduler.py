# scheduler.py

# -----------------------------
# USER INPUT
# -----------------------------

sleep_hours = 8
wake_time = int(input("Wake time?: "))

fixed_activities = [
    {
        "name": "College",
        "start": 9,
        "end": 16
    }
]

tasks = [
    {
        "name": "Project Work",
        "duration": 2,
        "priority": 3
    },
    {
        "name": "DSA Practice",
        "duration": 2,
        "priority": 2
    },
    {
        "name": "Gym",
        "duration": 1,
        "priority": 1
    }
]

# -----------------------------
# FUNCTIONS
# -----------------------------

def calculate_sleep_time(wake_time, sleep_hours):
    sleep_time = wake_time - sleep_hours

    if sleep_time < 0:
        sleep_time += 24

    return sleep_time


def sort_tasks_by_priority(tasks):
    return sorted(
        tasks,
        key=lambda task: task["priority"],
        reverse=True
    )


def generate_schedule(tasks, fixed_activities):
    schedule = []

    # Add fixed activities first
    for activity in fixed_activities:
        schedule.append({
            "name": activity["name"],
            "start": activity["start"],
            "end": activity["end"]
        })

    # Start scheduling after fixed activities
    current_time = fixed_activities[0]["end"]

    sorted_tasks = sort_tasks_by_priority(tasks)

    for task in sorted_tasks:
        start = current_time
        end = current_time + task["duration"]

        schedule.append({
            "name": task["name"],
            "start": start,
            "end": end
        })

        current_time = end

    return sorted(schedule, key=lambda item: item["start"])


# -----------------------------
# MAIN PROGRAM
# -----------------------------

sleep_time = calculate_sleep_time(
    wake_time,
    sleep_hours
)

daily_schedule = generate_schedule(
    tasks,
    fixed_activities
)

print("\nDAILY SCHEDULE")
print("-" * 30)

for item in daily_schedule:
    print(
        f"{item['start']}:00 - "
        f"{item['end']}:00 | "
        f"{item['name']}"
    )

print("\nSLEEP SCHEDULE")
print("-" * 30)
print(f"Sleep at: {sleep_time}:00")
print(f"Wake at : {wake_time}:00")
