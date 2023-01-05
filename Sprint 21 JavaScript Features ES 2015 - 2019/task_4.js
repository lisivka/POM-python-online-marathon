// The function takes any number of strings and returns the sum of their lengths.
//
//     Example:
//
//
// console.log(sumOfLen('hello', 'hi')); //7
// console.log(sumOfLen('hi')); //2
// console.log(sumOfLen()); //0
// console.log(sumOfLen('hello', 'hi', 'my name', 'is')); //16


const sumOfLen = (...args) => {
    // code
    lenSting =args.join('').length

    return lenSting;
}


console.log(sumOfLen('hello', 'hi'));
// 7
console.log(sumOfLen('hi'));
// 2
// console.log(sumOfLen());
// 0
// console.log(sumOfLen('hello', 'hi', 'my name', 'is'));
// 16
// console.log(sumOfLen('hello', 'hi', 'my name', 'is2'));
// 17
// console.log(sumOfLen('hello', 'my name', 'is'));
// 14
// console.log(sumOfLen('hello', 'my name'));
// 12