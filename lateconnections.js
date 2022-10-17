let lateConnections = document.getElementsByClassName("turn-schedule__flight-time-estimated late");
let lateConnectionsScheduled = document.getElementsByClassName("turn-schedule__flight-time-scheduled late");
let lateFlightInfo = document.getElementsByClassName("turn-schedule__flight-number");
let lateFlights = [];
let lateFlightNumber = [];
let newArray = [];

function LateFlightList(lateArrivalTime, schedArrivalTime) {
    this.lateArrivalTime = lateArrivalTime;
    this.schedArrivalTime = schedArrivalTime;
}

for (var i = 0; i < 20; i++) {
        lateFlights.push(lateConnections[i].innerText)
        lateFlightNumber.push(lateConnectionsScheduled[i].innerText)
        const late = new LateFlightList(lateConnections[i].innerText, lateConnectionsScheduled[i].innerText)
}
// const all = [...lateFlights, ...lateFlightNumber];
console.log(lateFlights)
console.log(lateFlightNumber)

function LateFlightList(lateArrivalTime, schedArrivalTime) {
    this.lateArrivalTime = lateArrivalTime;
    this.schedArrivalTime = schedArrivalTime;
}

// const late = new LateFlightList(late)
// let lateFlights = [];

// throw new Error();

// turn-schedule__row-cell turn-schedule__column__flight turn-schedule__flight turn-schedule__flight--arrival