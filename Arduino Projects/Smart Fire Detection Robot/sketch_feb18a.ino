#include <Servo.h>

// Pin Definitions
#define speedL 3
#define IN1 9
#define IN2 8
#define IN3 7
#define IN4 6
#define speedR 5
#define flame 2
#define buzzer 10

// Global Variables
char Reading;
int pos, flame_detected = 0;
Servo myservo;

// Function Declarations
void forword();
void backword();
void left();
void right();
void stopp();
void sweepServoAndCheckFlames();
void triggerAlarm();

void setup() {
  Serial.begin(9600);
  myservo.attach(11);
  myservo.write(90); // Center the servo

  // Set motor control pins as OUTPUT
  for (int i = 3; i <= 9; i++) {
    pinMode(i, OUTPUT);
  }

  // Set flame sensor as INPUT
  pinMode(flame, INPUT);

  // Set buzzer and LED as OUTPUT
  pinMode(buzzer, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    Reading = Serial.read();
    switch (Reading) {
      case 'F': forword(); break;
      case 'B': backword(); break;
      case 'R': right(); break;
      case 'L': left(); break;
      case 'S': stopp(); break;
      case 'Q':
        sweepServoAndCheckFlames();
        if (flame_detected > 0) {
          triggerAlarm();
        }
        break;
      default:
        Serial.println("Invalid command");
        break;
    }
  }
}

// Movement Functions
void forword() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(speedL, 150);
  analogWrite(speedR, 150);
}

void backword() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  analogWrite(speedL, 150);
  analogWrite(speedR, 150);
}

void left() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  analogWrite(speedL, 0);
  analogWrite(speedR, 150);
}

void right() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(speedL, 150);
  analogWrite(speedR, 0);
}

void stopp() {
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, LOW);
  analogWrite(speedL, 0);
  analogWrite(speedR, 0);
}

// Flame Detection and Alarm Functions
void sweepServoAndCheckFlames() {
  // Sweep from 90 to 180 degrees
  for (pos = 90; pos <= 180; pos += 1) {
    if (digitalRead(flame) == LOW) { // Flame detected
      flame_detected++;
    }
    myservo.write(pos);
    delay(10); // Reduced delay for faster sweep
  }

  // Sweep from 180 to 0 degrees
  for (pos = 180; pos >= 0; pos -= 1) {
    if (digitalRead(flame) == LOW) { // Flame detected
      flame_detected++;
    }
    myservo.write(pos);
    delay(10); // Reduced delay for faster sweep
  }

  // Return servo to center position
  myservo.write(90);
}

void triggerAlarm() {
  // Blink buzzer and LED 10 times
  for (int i = 0; i < 10; i++) {
    digitalWrite(buzzer, HIGH);
    delay(100);
    digitalWrite(buzzer, LOW);
    delay(100);
  }

  // Reset flame detection counter
  flame_detected = 0;
}