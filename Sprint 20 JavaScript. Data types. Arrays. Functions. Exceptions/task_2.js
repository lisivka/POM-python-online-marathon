//Write a function combineArray(arr1, arr2), which takes 2 arrays,
//and returns a new array consisting only of numeric elements of arrays arr1 and arr2.

//Function example:
//combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]));  // [12, 22, -8, 6, 15]

function combineArray(arr1, arr2) {
    arr3 = arr1.concat(arr2);
    copy1 = []
    arr3.forEach(function(entry) {if (Number.isInteger(entry)){copy1.push(entry)} });
    return copy1
    // copy = []
    // for (let i = 0; i < arr3.length; i++) {
    //     if (Number.isInteger(arr3[i])){
    //         console.log(arr3[i]);
    //         copy.push(arr3[i]);
    //     }
    //     // copy.push(arr3[i])
    // }
    // console.log(arr3);
    // console.log(copy)
    // console.log(copy1)
}

combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]);
console.log(combineArray([12, "User01", 22, true, -8], ["Index", 6, null, 15]))