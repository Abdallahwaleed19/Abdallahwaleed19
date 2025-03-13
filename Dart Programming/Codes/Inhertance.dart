// class Person {
//   String? name;
//   int? age;

//   void display() {
//     print("The person name is : $name , and his age is : $age ");
//   }
// }

// class Employee extends Person {
//   int? employeeId;
//   String? companyName;
//   String? departmentName;

//   void displayInfo() {
//     print("The Employee Name : $name , and his Age : $age");
//     print(
//       "The Employee Id : $employeeId , and his Company Name : $companyName , and his Department is : $departmentName ",
//     );
//   }
// }

// void main() {
//   var employee = Employee();
//   employee.name = "Abdallah";
//   employee.age = 20;
//   employee.employeeId = 20230192;
//   employee.companyName = "Menoufia National University";
//   employee.departmentName = "IoT Teaching Assistant";
//   employee.display();
//   employee.displayInfo();
// }

// Inhertance of Constructor

// class Laptop {
//   Laptop() {
//     print("laptop constructor");
//   }
// }

// class Dell extends Laptop {
//   Dell(){
//     print("Dell constructor");
//   }
// }

// void main() {
//   var dell = Dell();
// }

// class Laptop {
//   Laptop(String name, String color) {
//     print("Laptop constructor");
//     print("Name : $name");
//     print("Color: $color");
//   }
// }

// class Dell extends Laptop {
//   Dell(String name, String color) : super(name, color) {
//     print("Dell constructor");
//   }
// }

// void main() {
//   var dell = Dell("Dell Inspiron", "Black");
// }

// class laptop {
//   void show() {
//     print("Laptop show method");
//   }
// }

// class Dell extends laptop {
//   void show() {
//     super.show();
//     print("Dell show method");
//   }
// }
// void main(){
//   Dell dell = Dell();
//   dell.show();
// }

// Overriding

// class Car {
//   String? brand;
//   int? speed;

//   Car({this.brand, this.speed});

//   void power() {
//     print("The power is petrol");
//   }
// }

// class Tesla extends Car {
//   Tesla(String brand, int speed) : super(brand: brand, speed: speed);

//   @override
//   void power() {
//     print("The power is Electricity"); // override the power method
//   }
// }

// void main() {
//   Car car = Car(brand: "Toyota", speed: 120);
//   car.power();
//   print('Brand: ' + car.brand.toString() + ', Speed: ' + car.speed.toString());
//   Tesla tesla = Tesla("V1", 220);
//   print('Brand: ' + tesla.brand.toString() + ', Speed: ' + tesla.speed.toString());
//   tesla.power();
// }

// Abstract

// abstract class Shape {
//   int dim1;
//   int dim2;
//   Shape(this.dim1, this.dim2);
//   void area(); // Abstract method
// }

// class Rectangle extends Shape {
//   Rectangle(int dim1, int dim2) : super(dim1, dim2);
//   @override
//   void area() {
//     print("The Rectangle area is: ${dim1 * dim2}");
//   }
// }

// class Triangle extends Shape {
//   Triangle(int dim1, int dim2) : super(dim1, dim2);
//   @override
//   void area() {
//     print("The Triangle area is: ${0.5 * dim1 * dim2}");
//   }
// }

// void main() {
//   Rectangle rectangle = Rectangle(10, 20);
//   rectangle.area();

//   Triangle triangle = Triangle(10, 20);
//   triangle.area();
// }

// interface

// abstract class Area {
//   void area(); // Abstract method
// }

// abstract class Perimeter {
//   void perimeter(); // Abstract method
// }

// class Rectangle implements Area, Perimeter {
//   int length;
//   int width;

//   Rectangle(this.length, this.width);

//   @override
//   void area() {
//     print("The area of the Rectangle is: ${length * width}");
//   }

//   @override
//   void perimeter() {
//     print("The perimeter of the Rectangle is: ${2 * (length + width)}");
//   }
// }

// void main() {
//   Rectangle rectangle = Rectangle(10, 20);
//   rectangle.area();
//   rectangle.perimeter();
// }

// Mixin

// mixin canFly {
//   void fly() {
//     print(" I can fly ");
//   }
// }
// mixin canWalk {
//   void walk() {
//     print("I can walk");
//   }
// }

// class Bird with canFly, canWalk {}

// class Human with canWalk {}

// void main() {
//   Bird bird = Bird();
//   bird.fly();
//   bird.walk();
//   Human human = Human();
//   human.walk();
// }

// abstract class Animal {
//   String? name;
//   double? speed;
//   Animal(this.name, this.speed);
//   void run();
// }

// mixin canRun on Animal {
//   @override
//   void run() {
//     print("${this.name} is running at ${this.speed} km/h");
//   }
// }

// class Dog extends Animal with canRun {
//   Dog(String name, double speed) : super(name, speed);
// }

// void main() {
//   Dog dog = Dog("Buddy", 30);
//   dog.run();
// }
