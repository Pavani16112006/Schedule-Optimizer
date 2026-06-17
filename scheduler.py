from datetime import datetime, timedelta

# -----------------------------
# USER INPUT
# -----------------------------

sleep_time = "23:00"
wake_time = "07:00"

tasks = [
    {"name": "Project Work", "duration": 120, "priority": 1},
    {"name": "DSA Practice", "duration": 90, "priority": 2},
    {"name": "Gym", "duration": 60, "priority": 3},
]

special_events = [
    {
        "name": "College",
        "start": "09:00",
        "end": "16:00"
    }
]

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------

def to_datetime(time_string):
    return datetime.strptime(time_string, "%H:%M")


def format_time(dt):
    return dt.strftime("%H:%M")


# -----------------------------
# SCHEDULER
# -----------------------------

def generate_schedule():

    schedule = []

    # Sort tasks by priority
    sorted_tasks = sorted(
        tasks,
        key=lambda x: x["priority"]
    )

    current_time = to_datetime(wake_time)

    # Morning free slot before events
    first_event = special_events[0]
    event_start = to_datetime(first_event["start"])

    for task in sorted_tasks:

        duration = timedelta(minutes=task["duration"])

        if current_time + duration <= event_start:

            schedule.append({
                "task": task["name"],
                "start": format_time(current_time),
                "end": format_time(current_time + duration)
            })

            current_time += duration

            # Add tea break
            schedule.append({
                "task": "Tea Break ☕",
                "start": format_time(current_time),
                "end": format_time(
                    current_time + timedelta(minutes=15)
                )
            })

            current_time += timedelta(minutes=15)

    # Add fixed events
    for event in special_events:

        schedule.append({
            "task": event["name"],
            "start": event["start"],
            "end": event["end"]
        })

    # Continue after last event
    current_time = to_datetime(
        special_events[-1]["end"]
    )

    for task in sorted_tasks:

        already_scheduled = any(
            item["task"] == task["name"]
            for item in schedule
        )

        if not already_scheduled:

            duration = timedelta(
                minutes=task["duration"]
            )

            schedule.append({
                "task": task["name"],
                "start": format_time(current_time),
                "end": format_time(current_time + duration)
            })

            current_time += duration

            # Break after each task
            schedule.append({
                "task": "Tea Break ☕",
                "start": format_time(current_time),
                "end": format_time(
                    current_time + timedelta(minutes=15)
                )
            })

            current_time += timedelta(minutes=15)

    # Sleep block
    schedule.append({
        "task": "Sleep 😴",
        "start": sleep_time,
        "end": wake_time
    })

    return sorted(
        schedule,
        key=lambda x: x["start"]
    )


# -----------------------------
# RUN
# -----------------------------

daily_schedule = generate_schedule()

print("\nOPTIMIZED DAILY SCHEDULE\n")

for item in daily_schedule:
    print(
        f"{item['start']} - "
        f"{item['end']} | "
        f"{item['task']}"
    )
