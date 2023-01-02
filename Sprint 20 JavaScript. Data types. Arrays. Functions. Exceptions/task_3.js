// Implement the longestLogin(loginList) function, which takes an array of user logins loginList
// and returns the longest login. If the logins of the same length are the longest in the array,
// the login element with the largest index is returned. Tip: You can use the reduce() method to solve the task.

// Function examples:

// longestLogin(["serg22", "tester_2", "Prokopenko", "guest"]);   //  Prokopenko
// longestLogin(["user1", "user2", "333", "user4", "aa"]);   //  user4

// https://developer.mozilla.org/ru/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce


function longestLogin(loginList) {
    return loginList.reduce(function (previousValue, currentValue) {
        if (currentValue.length >= previousValue.length ) { return currentValue }
        else { return previousValue }
    })

}

function longestLogin2(loginList) {

    maxLogin =  loginList.reduce(function (previousValue, currentValue) {
        if (currentValue.length >= previousValue.length ) { return currentValue }
        else { return previousValue }
    })
    return maxLogin

}



console.log(longestLogin2(["serg22", 2, "tester_2", "Prokopenko", "guest"]))
// Prokopenko
console.log(longestLogin(["maxxx", "NewUser", "admin111" , "Administrator"]));
// Administrator
console.log(longestLogin(["User123", "Steven Dobson", "qwerty12345"]));
// Steven Dobson
console.log(longestLogin(["Carl1999", "ivan@gmail.com", "nick-name"]));
// ivan@gmail.com
console.log(longestLogin(["user1", "user2", "333", "user4", "aa"]));
// user4
console.log(longestLogin(["larian", "questttt", "longest_user_name", "Nick Nickson"]));
// longest_user_name
