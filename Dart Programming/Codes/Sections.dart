// void main() {
// print("Hello World");
// }

// void main()
// var num1 = 12;
//   var num2 = 13;
//   var sum = num1 + num2;
//   var subtract = num2 - num1;
//   var multi = num1 * num2;
//   var division = num1 / num2;
//   print(sum);
//   print(subtract);
//   print(multi);
//   print(division);
// }

// import 'dart:io';

// void main() {
//   print("Enter your birth :");
//   var birth = int.parse(stdin.readLineSync()!);
//   var age = DateTime.now().year - birth;
//   print("Your age is $age");
// }

// void main() {
//   for (int i = 1; i <= 20; i++) {
//     print(i);
//   }
// }

// import 'dart:io';

// void main() {
//   for (int i = 0; i < 10; i--) {
//     try {
//       print("Enter your Birth :");
//       var birth = int.parse(stdin.readLineSync()!);
//       var age = DateTime.now().year - birth;
//       print("Now your age is $age");
//       break;
//     } on FormatException {
//       print("Oh No ! , Please Try Again ");
//     }
//   }
// }


// import 'dart:io';

// void main() {
//   stdout.write("Enter your age : ");
//   String? input = stdin.readLineSync();
//   int age = int.parse(input!);
//   if (age >= 18) {
//     print("You are a Voter.");
//   } else {
//     print("You are not a Voter.");
//   }
// }

// void main() {
//   int num1 = 50;
//   int num2 = 40;
//   int max = (num1 > num2) ? num1 : num2;
//   print(max);
// }

// void main() {
//   int num = 1;
//   switch (num) {
//     case 1 :
//       print("STR");
//       break;
//     case 2:
//       print("SUN");
//       break;
//     case 3:
//       print("MON");
//       break;
//     case 4:
//       print("THU");
//       break;
//     case 5:
//       print("WED");
//       break;
//     case 6:
//       print("THR");
//       break;
//     case 7:
//       print("FRI");
//     default:
//       print("Error Input");
//   }
// }

// void main() {
//   for (int i = 1; i <= 10; i++) {
//     print(i);
//   }
// }

// void main() {
//   List numbers = [1, 2, 3, 4, 5];
//   for (var number in numbers) {
//     print(number);
//   }
// }

// void main() {
//   List numbers = [1, 2, 3, 4, 5, 6, 7];
//   int total = 0;
//   numbers.forEach((num) => total = total + num as int);
//   print(total);
// }

// void main() {
//   int i = 1;
//   do {
//     print (i);
//     i++;
//   }
//   while (i >= 10);
// }

// void main() {
//   int num = 1;
//   while (num <= 100) {
//     if (num % 2 == 0) {
//       print(num);
//     }
//     num++;
//   }
// }

// void main (){
//   for (int i = 1 ; i <= 10 ; i++){
//     if (i == 5){
//       break;
//     }
//     print(i);
//   }
// }

// void main (){
//   for (int i = 1 ; i <= 10 ; i++){
//     if (i == 5){
//       continue;
//       }
//       print(i);
//       }
// }

// void main() {
//   String firstName = "Abdallah";
//   String lastName = "Salem";
//   print("$firstName $lastName");
//   int num1 = 23;
//   int num2 = 24;
//   int sum = num1 + num2;
//   print(sum);
//   double num3 = 5.5;
//   double num4 = 7.7;
//   double multiply = num3 * num4;
//   print(multiply);
//   bool isage = true;
//   print(isage);
//   final double pi = 3.14;
//   double circleArea = pi * 5 * 5;
//   print(circleArea);
//   final DateTime now = DateTime.now();
//   print(now);
//   final List<int> finallist = [1, 2, 3, 4];
//   finallist.add(5);
//   print(finallist);
//   const int x = 5;
//   const int y = x + 5;
//   print(y);
//   String Age = "20";
//   print(Age.runtimeType);
//   print(int.parse(Age).runtimeType);
// }

// void main() {
//   var name = "Abdallah Waleed";
//   print(name);
//   var firstName = "Mohamed";
//   var lastName = "Salah";
//   print("The Player Name is : $firstName $lastName");
//   var age = 38;
//   print("The Player name is : $firstName $lastName and he is age is : $age");
//   var num1 = 20;
//   var num2 = 30;
//   var sum = num1 + num2;
//   var subtract = num2 - num1;
//   var multiply = num1 * num2;
//   var divide = num2 / num1;
//   print("The sum is : $sum");
//   print("The subtract is : $subtract");
//   print("The multiply is : $multiply");
//   print("The divide is : $divide");
// }
