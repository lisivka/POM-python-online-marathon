// The user enters as arguments the number of seconds, minutes, hours, days, weeks, months, years.
//     Output how many seconds are in all this.
//     All parameters are optional. Consider 30 days in a month
//
// Example:
// howMuchSec(12, 3); //192
// howMuchSec(1, 33, 22); //81181
// howMuchSec(); //0


const howMuchSec = (seconds=0, minutes=0, hours=0, days=0, weeks=0, months=0, years=0) => {
    amountSec =
        seconds
        +60*minutes
        +60*60*hours
        +60*60*24*days
        +60*60*24*7*weeks
        +60*60*24*30*months
        +60*60*24*30*365*years
    return amountSec
}


console.log(howMuchSec(12, 3));
// 192

console.log(howMuchSec(1, 33, 22));
// 81181

console.log(howMuchSec());
// 0

console.log(howMuchSec(12, 3, 3, 3));
// 270192

console.log(howMuchSec(33, 33, 11));
// 41613
