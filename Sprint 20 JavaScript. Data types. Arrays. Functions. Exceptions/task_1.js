//Implement the modifyArray(array) function, which takes an arbitrary array, changes the value of the
//first element of the array to “Start”, the last element of the array to “End” and returns the modified array.
//
//Function example:
//
//modifyArray([12, 6, 22, 0, -8])); // [‘Start’, 6, 22, 0, ‘End’]

//const expected = ['Start', 6, 22, 0, 'End'];
//const actual = modifyArray([12, 6, 22, 0, -8]);
//console.log(actual.length === expected.length &&
//  actual.every((value, key) => value === expected[key]));
//console.log(modifyArray([12, 6, 22, 0, -8]));


function modifyArray(array) {
   array[0] = "Start"
   array[array.length-1] = "End"

   return array

}


modifyArray([12, 6, 22, 0, -8]);
console.log(modifyArray);
console.log(modifyArray([12, 6, 22, 0, -8]));

console.log("Len", modifyArray.length);
//log o