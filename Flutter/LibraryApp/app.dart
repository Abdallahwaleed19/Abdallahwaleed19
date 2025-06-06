import 'package:flutter/material.dart';
import 'views/screens/splash_screen.dart';

class LibraryApp extends StatelessWidget {
  const LibraryApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Library App',
      home: const SplashScreen(),
    );
  }
}
