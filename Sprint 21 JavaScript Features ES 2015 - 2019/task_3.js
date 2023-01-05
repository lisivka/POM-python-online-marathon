// Find the maximum interval between two consecutive numbers. Numbers are entered as arguments
//
// Example:
//
//     maxInterv(3, 5, 2, 7); //5
// maxInterv(3, 5, 2, 7, 11, 0, -2); //11
// maxInterv(3, 5); //2
// maxInterv(3); //0

const maxInterv2 = (...args) => {

    let maxx = 0
    args.reduce(function (previousValue, currentValue) {
        let interval = Math.abs(currentValue - previousValue);
        if (interval > maxx) {
            maxx = interval
        }
        console.log("prev", previousValue, "curr", currentValue,"maxx = ",  maxx,"++interv=",  interval);
        return currentValue
    })

    return maxx

}

const maxInterv = (...args) => {
    let maxx = 0
    for (let i = 1; i < args.length; i++) {
        let interval = Math.abs(args[i] - args[i - 1]);
        if (interval > maxx) {
            maxx = interval
        }
    }
    return maxx
}


// console.log(maxInterv(3, 5, 2, 7)) // 5
console.log(maxInterv(3, 5, 2, 7, 11, 0, -2)) // 11
// console.log(maxInterv(3, 5)) // 2
// console.log(maxInterv(3));  // 0
// console.log(maxInterv(3, 5, 2, 8)); // 6
// console.log(maxInterv(3, 5, 2, 37, 11, 0, -2)) // 35
// console.log(maxInterv(8)); // 0
