function generateSchedule() {

    const sleepTime =
        document.getElementById("sleepTime").value;

    const wakeTime =
        document.getElementById("wakeTime").value;

    const tasks =
        document.getElementById("tasks")
        .value
        .split(",");

    const priorities =
        document.getElementById("priorities")
        .value
        .split(",");

    let output =
        "<h3>Optimized Schedule</h3>";

    output += `
    Sleep: ${sleepTime}
    <br>
    Wake Up: ${wakeTime}
    <br><br>
    `;

    tasks.forEach((task, index) => {
        output += `
        ${task.trim()}
        (Priority ${priorities[index]})
        <br>
        `;
    });

    output += `
    <br>
    Tea Break: 11:00 AM
    <br>
    Lunch Break: 1:00 PM
    <br>
    Evening Break: 5:00 PM
    `;

    document.getElementById("output")
        .innerHTML = output;
}
