






let lateConnections = document.getElementsByClassName("turn-schedule__flight-time-estimated late");
let lateScheduledTime = document.getElementsByClassName("turn-schedule__flight-time-scheduled late");
let lateFlights = [];
let lateSched = [];


for (var i = 0; i < 5; i++) {
    lateFlights.push(lateConnections[i].innerText)
    lateSched.push(lateScheduledTime[i].innerText)
}
console.table(lateFlights)
console.table(lateSched)


// let lateConnections = document.querySelectorAll("div.turn-schedule__flight-time-estimated late");
// const lateConnections = turn-schedule__flight-time-estimated.querySelectorAll("div");
// let lateConnectionsScheduled = document.getElementsByClassName("turn-schedule__flight-time-scheduled late");
// let lateFlightInfo = document.getElementsByClassName("turn-schedule__flight-number");
// let lateFlights = [];
// let lateFlightNumber = [];
// let newArray = [];

// function LateFlightList(lateArrivalTime, schedArrivalTime) {
//     this.lateArrivalTime = lateArrivalTime;
//     this.schedArrivalTime = schedArrivalTime;
// }

// for (var i = 0; i < 5; i++) {
        // lateFlights.push(lateConnections[i])
        // lateFlightNumber.push(lateConnectionsScheduled[i])
        // console.log(lateFlights)
// console.log(lateFlightNumber)
        // const late = new LateFlightList(lateConnections[i], lateConnectionsScheduled[i])
// }
// const all = [...lateFlights, ...lateFlightNumber];
// console.log(lateFlights)
// console.log(lateFlightNumber)
// console.log(all)

// function LateFlightList(lateArrivalTime, schedArrivalTime) {
//     this.lateArrivalTime = lateArrivalTime;
//     this.schedArrivalTime = schedArrivalTime;
// }


// turn-schedule__row-cell turn-schedule__column__flight turn-schedule__flight turn-schedule__flight--arrival