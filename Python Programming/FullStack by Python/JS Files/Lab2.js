// function printHello(){
//     console.log("Hello from iTi");
// }
// printHello();

// function sum(num1 , num2){
//     var result = num1 + num2;
//     console.log("The sum = " + result);
// }
// sum(5, 10);

// var word = "JavaScript";
// slice = word.slice(0, 3);
// console.log(slice);

// var arr = [1,2,3,4];
// arr.push(5);
// console.log(arr);

// function sayHello(name = "Guest"){
//     console.log("Hello " + name);
// }
// sayHello("Abdallah");
// sayHello();

// function isLong(str){
//     if (str.length > 5){
//         return true;
//     }
//     else{
//         return false;
//     }
// }
// var result = isLong("Hello World");
// console.log(result);

// var arr = ["Abdallah" , "Ali" , "Mohamed" , "Ahmed" , "Saif"];
// arr.pop();
// arr.shift();
// console.log(arr);

// function addItem(arr , item){
//     if (arr.length < 4){
//         arr.push(item);
//         console.log(arr);
//     }
//     else{
//         console.log("Cannot add item ");
//     }
// }
// addItem(["RealMadrid" , "PSG" , "Alahly" , "Liverpool"] , "Barcelona");
// addItem(["RealMadrid" , "PSG" , "Alahly" ] , "Barcelona");


// function formatName(name){
//     var name = name.trim().toUpperCase();
//     return name;
// }
// var Name1 = formatName("  abdallah  ");
// console.log(Name1);


var numbers = [5, 12, 3, 9, 1, 20];
// function sort(numbers){
//     numbers.sort(function(a, b) {
//         return a - b;
//     });
// }
// sort(numbers);
// console.log("After sorting: " + numbers);


// for (var i = 0; i < numbers.length - 1; i++) {
//     for (var j = i + 1; j < numbers.length; j++) {
//         if (numbers[i] > numbers[j]) {
//             var temp = numbers[i];
//             numbers[i] = numbers[j];
//             numbers[j] = temp;
//         }
//     }
// }
// console.log(numbers);


// function loginAccount (username , password){
//     if (username === "admin" && password === "1234") {
//         console.log("Login successful");
//     } else {
//         console.log("Invalid username or password");
//     }
// }
// var username = prompt("Enter your username:").toLowerCase();
// var password = prompt("Enter your password:");
// loginAccount(username , password);
