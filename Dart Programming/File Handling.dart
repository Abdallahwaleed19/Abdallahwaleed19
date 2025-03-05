// import 'dart:io';
// void main (){
//   File file = File("test.txt");
//   file.writeAsStringSync("Hello, this is a text file created using Dart!");
//   print("File created successfully!");
// }

// import 'dart:io';
// void main() {
//   File file = File("test.txt");
//   print('File Path: ${file.path}');
//   print('File absolute path: ${file.absolute.path}');
//   print('File Size: ${file.lengthSync()} bytes');
//   print('File Exists: ${file.existsSync()}');
//   print('Last Modified: ${file.lastModifiedSync()}');
// }

// import 'dart:io';
// void main(){
//   File file  = File("test.txt");
//   file.writeAsStringSync("Hello, this is a text file created using Dart!");
//   print("File created successfully!");
// }

// import 'dart:io';
// void main() {
//   File file = File("test.txt");
//   file.writeAsStringSync("\nHello my name is abdallah waleed", mode: FileMode.append);
//   print("File created/modified successfully!");
// }

// import 'dart:io';
// void main(){
//   File file  = File("test.csv");
//   String content = file.readAsStringSync();
//   List <String> lines = content.split('\n');
//   for (String line in lines){
//     print(line);
//   }
// }

// import 'dart:io';
// void main() {
//   final file = File("Student.csv");
//   file.writeAsStringSync("Name, Phone\n");
//   for (int i = 0; i < 3; i++) {
//     stdout.write("Enter Name: ");
//     String? name = stdin.readLineSync();
//     stdout.write("Enter Phone: ");
//     String? phone = stdin.readLineSync();
//     file.writeAsStringSync("$name, $phone\n", mode: FileMode.append);
//   }
//   print("Data written to Student.csv successfully!");
// }

// import 'dart:io';
// void main(){
//   File file  = File("Student.csv");
//   String content = file.readAsStringSync();
//   List <String> lines = content.split('\n');
//   for (String line in lines){
//     print(line);
// }}

// import 'dart:io';
// void main (){
//   File file = File('example.txt');
//   if (file.existsSync()){
//     file.deleteSync();
//     print('File deleted successfully!');
//   }else{
//     print('File not found!');
//   }
// }

