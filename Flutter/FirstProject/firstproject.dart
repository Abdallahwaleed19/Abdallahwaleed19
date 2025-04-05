import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("The Arab Of Palestin", style: TextStyle(color: Colors.green)), 
          backgroundColor: Colors.black,
        ),
        body: Container(
          color: Colors.green,
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Image.network("https://cdn.pixabay.com/photo/2013/07/13/14/16/palestine-162385_1280.png"),
                Text("Free Palestine", style: TextStyle(
                  fontSize: 30.0,
                  color: Colors.red,
                  fontWeight: FontWeight.bold,
                )),
              ],
            ),
          ),
        ),
      ),
    );
  }
}