from datetime import datetime, timedelta

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def to_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def format_time(dt):
    return dt.strftime("%H:%M")

# -----------------------------
# USER INPUT
# -----------------------------

sleep_time = input("Sleep Time (HH:MM): ")
wake_time = input("Wake Time (HH:MM): ")

# Tasks
tasks = []

num_tasks = int(input("\nHow many daily tasks? "))

for i in range(num_tasks):
    print(f"\nTask {i+1}")

    name = input("Task Name: ")
    duration = int(input("Duration (minutes): "))
    priority = int(input("Priority (1 = Highest): "))

    tasks.append({
        "name": name,
        "duration": duration,
        "priority": priority
    })

# Special Events
events = []

num_events = int(input("\nHow many special events? "))

for i in range(num_events):
    print(f"\nEvent {i+1}")

    name = input("Event Name: ")
    start = input("Start Time (HH:MM): ")
    end = input("End Time (HH:MM): ")

    events.append({
        "name": name,
        "start": start,
        "end": end
    })

# -----------------------------
# FIXED MEAL BREAKS
# -----------------------------

events.extend([
    {
        "name": "Breakfast 🍳",
        "start": "07:30",
        "end": "08:00"
    },
    {
        "name": "Lunch 🍱",
        "start": "13:00",
        "end": "14:00"
    },
    {
        "name": "Dinner 🍽️",
        "start": "20:00",
        "end": "20:45"
    }
])

# -----------------------------
# SORT EVENTS
# -----------------------------

events.sort(key=lambda x: x["start"])

# -----------------------------
# BUILD SCHEDULE
# -----------------------------

schedule = []

# Add fixed events first
for event in events:
    schedule.append({
        "start": event["start"],
        "end": event["end"],
        "activity": event["name"]
    })

# Sort tasks by priority
tasks.sort(key=lambda x: x["priority"])

current_time = to_time(wake_time)

for task in tasks:

    duration = timedelta(minutes=task["duration"])

    while True:

        conflict = False

        for item in schedule:

            event_start = to_time(item["start"])
            event_end = to_time(item["end"])

            proposed_end = current_time + duration

            if (
                current_time < event_end
                and proposed_end > event_start
            ):
                current_time = event_end
                conflict = True
                break

        if not conflict:
            break

    task_end = current_time + duration

    schedule.append({
        "start": format_time(current_time),
        "end": format_time(task_end),
        "activity": task["name"]
    })

    current_time = task_end

    # Tea break after each task
    tea_end = current_time + timedelta(minutes=15)

    schedule.append({
        "start": format_time(current_time),
        "end": format_time(tea_end),
        "activity": "Tea Break ☕"
    })

    current_time = tea_end

# Sleep block
schedule.append({
    "start": sleep_time,
    "end": wake_time,
    "activity": "Sleep 😴"
})

# -----------------------------
# DISPLAY TABLE
# -----------------------------

schedule.sort(key=lambda x: x["start"])

print("\n" + "=" * 60)
print("OPTIMIZED DAILY SCHEDULE")
print("=" * 60)

print(f"{'TIME':<20} {'ACTIVITY'}")
print("-" * 60)

for item in schedule:
    time_slot = f"{item['start']} - {item['end']}"
    print(f"{time_slot:<20} {item['activity']}")
