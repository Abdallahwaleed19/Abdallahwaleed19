// class Animal {
//   String? name;
//   int? numberoflegs;
//   int? lifespan;
//   void display() {
//     print("Name: $name");
//     print("Number of legs: $numberoflegs");
//     print("Lifespan: $lifespan");
//   }
// }
// void main() {
//   Animal animal = Animal();
//   animal.name = "Dog";
//   animal.numberoflegs = 4;
//   animal.lifespan = 10;
//   animal.display();
// }

// class Person {
//   String? name;
//   int? age;
//   bool? isMarried;
//   String? phone;
//   void displayinfo() {
//     print("Name: $name");
//     print("Age: $age");
//     print("Is Married: $isMarried");
//     print("Phone: $phone");
//   }
// }
// void main() {
//   Person person = Person();
//   person.name = "Abdallah";
//   person.age = 20;
//   person.isMarried = true;
//   person.phone = "01005831772";
//   person.displayinfo();
// }

// class Rectangle {
//   double? width;
//   double? height;
//   void area() {
//     double area = width! * height!;
//     print("The area of the rectangle is: $area");
//   }
// }
// void main() {
//   Rectangle rectangle = Rectangle();
//   rectangle.width = 5.0;
//   rectangle.height = 10.0;
//   rectangle.area();
// }

// class Student {
//   String? name;
//   int? age;
//   String? grade;
//   int? numberofgrade;
//   String? courseName ;
//   void displayinfo() {
//     print("Name: $name");
//     print("Age: $age");
//     print("Course Name: $courseName , Grade: $grade, and his number of grade is: $numberofgrade");
//   }
// }
// void main() {
//   Student student = Student();
//   student.name = "Abdallah";
//   student.age = 20;
//   student.grade = "A+";
//   student.numberofgrade = 4;
//   student.courseName = "Mobile Programming";
//   student.displayinfo();
// }

// class Student {
//   String? name;
//   int? age;
//   String? grade;
//   int? numberofgrade;
//   String? courseName;
//   Student(String name, int age, String grade, int numberofgrade , String courseName){
//     this.name = name;
//     this.age = age;
//     this.grade = grade;
//     this.numberofgrade = numberofgrade;
//     this.courseName = courseName;
//   }
// }
// void main() {
//   Student student = Student("Abdallah", 20, "A+", 4, "Mobile Programming");
//   print("Name: ${student.name}");
//   print("Age: ${student.age}");
//   print("Course Name: ${student.courseName} , Grade: ${student.grade}, and his number of grade is: ${student.numberofgrade}");
// }

// class Employee{
//   String? name;
//   int? age;
//   String? job;
//   int? salary;
//   Employee(this.name, this.age, this.job, this.salary);
//   void displayinfo(){
//     print("Name: $name");
//     print("Age: $age");
//     print("Job: $job");
//     print("Salary: $salary");
// }}
// void main(){
//   Employee employee = Employee("Abdallah", 20, "IoT Developer", 10000);
//   employee.displayinfo();
// }

// class Chair {
//   String? color;
//   int? cost;
//   Chair({this.color, this.cost});
//   void display() {
//     print("color: ${this.color}");
//     print("Cost: ${this.cost}");
//   }
// }
// void main(){
//   Chair chair = Chair(color: "red", cost: 1000);
//   chair.display();
// }

// class Table {
//   String? color;
//   int? cost;
//   Table({this.color = "white", this.cost = 100});
//   void display() {
//     print("color: ${this.color} , , cost: ${this.cost}" );
// }
// }
// void main(){
//   Table table = Table();
//   table.display();
// }

// class Student {
//   String? name;
//   int? age;
//   int? rollNumber;
//   Student.namedConstructor(String name, int age, int rollNumber) {
//     this.name = name;
//     this.age = age;
//     this.rollNumber = rollNumber;
//   }
// }
// void main() {
//   Student student = Student.namedConstructor("John", 20, 1);
//   print("Name: ${student.name}");
//   print("Age: ${student.age}");
//   print("Roll Number: ${student.rollNumber}");
// }

// class Animal {
//   String? name;
//   int? numberoflegs;
//   int? lifespan;
//   Animal.FromAnimal1(String name, int numberoflegs, int lifespan) {
//     this.name = name;
//     this.numberoflegs = numberoflegs;
//     this.lifespan = lifespan;
//   }
//   Animal.FromAnimal2(String name, int numberoflegs , int lifespan) {
//     this.name = name;
//     this.numberoflegs = numberoflegs;
//     this.lifespan = lifespan;
//   }
// }
// void main() {
//   Animal animal1 = Animal.FromAnimal1("Dog", 4, 10);
//   Animal animal2 = Animal.FromAnimal2("Cat", 4, 15);
//   print("Name: ${animal1.name}");
//   print("Number of legs: ${animal1.numberoflegs}");
//   print("Lifespan: ${animal1.lifespan}");
//   print("Name: ${animal2.name}");
//   print("Number of legs: ${animal2.numberoflegs}");
//   print("Lifespan: ${animal2.lifespan}");
// }


// class Bank {
//  final String? name;
//  final int? balance;
//  const Bank (this.name, this.balance);
// }
// void main() {
//   const Bank bank = Bank("Abdallah", 1000000);
//   print("Name: ${bank.name}");
//   print("Balance: ${bank.balance}");
// }