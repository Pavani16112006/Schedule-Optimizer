function generateSchedule() {

```
const sleepTime =
    document.getElementById("sleepTime").value;

const wakeTime =
    document.getElementById("wakeTime").value;

const tasks =
    document.getElementById("tasks")
        .value
        .split("\n")
        .filter(task => task.trim() !== "");

const durations =
    document.getElementById("durations")
        .value
        .split("\n");

const priorities =
    document.getElementById("priorities")
        .value
        .split("\n");

const events =
    document.getElementById("events")
        .value
        .split("\n")
        .filter(event => event.trim() !== "");

const eventStarts =
    document.getElementById("eventStarts")
        .value
        .split("\n");

const eventEnds =
    document.getElementById("eventEnds")
        .value
        .split("\n");

const scheduleTable =
    document.getElementById("scheduleTable");

scheduleTable.innerHTML = "";

let schedule = [];

// Sleep
schedule.push({
    time: `${sleepTime} - ${wakeTime}`,
    activity: "Sleep 😴"
});

// Breakfast
schedule.push({
    time: "07:30 - 08:00",
    activity: "Breakfast 🍳"
});

// Lunch
schedule.push({
    time: "13:00 - 14:00",
    activity: "Lunch 🍱"
});

// Dinner
schedule.push({
    time: "20:00 - 20:45",
    activity: "Dinner 🍽️"
});

// Special Events
for (let i = 0; i < events.length; i++) {

    schedule.push({
        time: `${eventStarts[i]} - ${eventEnds[i]}`,
        activity: events[i]
    });
}

// Tasks with priorities
let taskObjects = [];

for (let i = 0; i < tasks.length; i++) {

    taskObjects.push({
        name: tasks[i],
        duration: durations[i],
        priority: parseInt(priorities[i])
    });
}

taskObjects.sort((a, b) =>
    a.priority - b.priority
);

taskObjects.forEach(task => {

    schedule.push({
        time: `${task.duration} mins`,
        activity:
            `${task.name} (Priority ${task.priority})`
    });

    schedule.push({
        time: "15 mins",
        activity: "Tea Break ☕"
    });

});

schedule.forEach(item => {

    const row =
        document.createElement("tr");

    row.innerHTML = `
        <td>${item.time}</td>
        <td>${item.activity}</td>
    `;

    scheduleTable.appendChild(row);
});
```

}
