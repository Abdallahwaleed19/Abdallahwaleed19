// grade = Number(prompt("Enter your grade: "));
// if (grade >= 85 && grade <= 100) {
//     console.log("You got an A");
// }
// else if (grade >= 75 && grade <= 84) {
//     console.log("You got a B");
// }
// else if (grade >= 65 && grade <= 74) {
//     console.log("You got a C");
// }
// else if (grade >= 50 && grade <= 64) {
//     console.log("You got a D");
// }
// else {
//     console.log("You got an F");
// }


// number = Number(prompt("Enter a number: "));
// if (number % 2 === 0) {
//     console.log("The number is even");
// }
// else {
//     console.log("The number is odd");
// }


// var day  = Number (prompt("Enter the number of your day:"));
// switch (day) {
//     case "1":
//         console.log("STR")
//         break;
//     case "2":
//         console.log("SUN")
//         break;
//     case "3":
//         console.log("MON")
//         break;
//     case "4":
//         console.log("TUE")
//         break;
//     case "5":
//         console.log("WED")
//         break;
//     case "6":
//         console.log("THU")
//         break;
//     case "7":
//         console.log("FRI")
//         break;
//     default:
//         console.log("Error"); 
// }


// var num = 1 ; 
// for (num ; num <= 10 ; num++) {
//     console.log(num);
// }


// var name = prompt("Enter your name: ");
// var sure = confirm("Are you sure you want to log in?");
// if (sure) {
//     console.log("Welcome " + name);
// } else {
//     console.log("Login cancelled");
// }


// fisrtNumber = Number(prompt("Enter the first number: "));
// operator = prompt("Enter the operator: ");
// secondNumber = Number(prompt("Enter the second number: "));
// if (operator === "+") {
//     console.log("Answer:"+(fisrtNumber + secondNumber));
// }
// else if (operator === "-") {
//     console.log("Answer:"+(fisrtNumber - secondNumber));
// }
// else if (operator === "*") {
//     console.log("Answer:"+(fisrtNumber * secondNumber));
// }
// else if (operator === "/" && secondNumber !== 0) {
//     console.log("Answer:"+(fisrtNumber / secondNumber));
// }
// else {
//     console.log("Error");
// }

// secretNumber = Math.floor(Math.random() * 10) + 1;
// var start = 0 ;
// var end = 3 ;
// while (start < end ){
// gussingNumber = prompt("Enter a number : ");
// if (gussingNumber > secretNumber) {
//     console.log("Too high");
// }
// else if (gussingNumber < secretNumber) {
//     console.log("Too small");
// }
// else {
//     console.log("Correct!");
// }
// start++ ;
// }
// if (start === end) {
//     console.log("Game Over");
// }


numberOfStudents = Number(prompt("Enter the number of students: "));
students = [];
grades = [];
for (i = 0 ; i < numberOfStudents ; i++) {
    students[i] = prompt("Enter the name of student " + (i+1) + ": ");
    grades[i] = Number(prompt("Enter the grade of " + students[i] + ": "));
    if (grades[i] >= 85 && grades[i] <= 100) {
        console.log(students[i] + " grade = A");
    } else if (grades[i] >= 75 && grades[i] <= 84) {
        console.log(students[i] + " grade = B");
    } else if (grades[i] >= 65 && grades[i] <= 74) {
        console.log(students[i] + " grade = C");
    } else if (grades[i] >= 50 && grades[i] <= 64) {
        console.log(students[i] + " grade = D");
    } else {
        console.log(students[i] + " grade =  F");
    }
}
document.write("<h1>Students Names</h1>");
for (i = 0 ; i < numberOfStudents ; i++) {
    document.write("<p>" + students[i] + "</p>");
}
document.write("<h1>Students Grades</h1>");
for (i = 0 ; i < numberOfStudents ; i++) {
    document.write("<p>" + grades[i] + "</p>");
}
var Avg = 0;
for (i = 0 ; i < numberOfStudents ; i++) {
    Avg += grades[i];
}
Avg /= numberOfStudents;
document.write("<h1>Average Grade</h1>");
document.write("<p>" + Avg + "</p>");
var passed = 0;
for (i = 0 ; i < numberOfStudents ; i++) {
    if (grades[i] >= 50) {
        passed++;
    }
}
document.write("<h1>Number of passed students</h1>");
document.write("<p>" + passed + "</p>");

