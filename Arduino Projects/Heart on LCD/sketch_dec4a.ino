#include <LiquidCrystal.h>

// Pin definitions
const int ledPin = 9;  // Pin where the LED is connected
int LDR = A0;  // Pin where the LDR is connected

// Create an LCD object (adjust pin numbers as necessary)
LiquidCrystal lcd(1, 2, 3, 4, 5, 6);

// Heart shape (using 5x8 matrix)
byte heart[8] = {
  B00000,
  B01110,
  B11111,
  B11111,
  B11111,
  B01110,
  B00100,
  B00000
};

// Broken heart shape (using 5x8 matrix)
byte brokenHeart[8] = {
  B01110,
  B10001,
  B10001,
  B10001,
  B10001,
  B01110,
  B00100,
  B00000
};

void setup() {
  // Initialize the LCD
  lcd.begin(16, 2);  // 16 columns and 2 rows
  lcd.clear();

  // Create custom characters
  lcd.createChar(0, heart);       // Heart character at position 0
  lcd.createChar(1, brokenHeart); // Broken heart character at position 1

  // Set the LED pin as output
  pinMode(ledPin, OUTPUT);
  pinMode(LDR, INPUT);
}

void loop() {
  // Read the LDR value
  int value = analogRead(LDR);

  // Turn the LED on if the LDR value is below a threshold (dark)
  if (value < 400) {
    digitalWrite(ledPin, HIGH);  // LED on
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.write(byte(0));  // Display heart when LED is on
  } else {
    digitalWrite(ledPin, LOW);  // LED off
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.write(byte(1));  // Display broken heart when LED is off
  }

  // Wait for 1 second before checking again
  delay(1000);
}

