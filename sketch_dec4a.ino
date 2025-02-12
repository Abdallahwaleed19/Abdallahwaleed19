#include <LiquidCrystal.h>

LiquidCrystal lcd(1, 2, 3, 4, 5, 6);

const int LDR = A0;
const int LED = 9;

// Define custom characters for happy and sad faces
byte happyFace[8] = {
  0b00000,
  0b01010,
  0b00000,
  0b00100,
  0b01010,
  0b10001,
  0b11111,
  0b00000
};

byte sadFace[8] = {
  0b00000,
  0b01010,
  0b00000,
  0b00100,
  0b10001,
  0b01010,
  0b11111,
  0b00000
};

void setup() {
  pinMode(LED, OUTPUT);
  pinMode(LDR, INPUT);
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);
  lcd.print("LDR Monitoring:");

  // Create the custom characters in the LCD
  lcd.createChar(0, happyFace); // Happy face at location 0
  lcd.createChar(1, sadFace);   // Sad face at location 1
}

void loop() {
  int value = analogRead(LDR);

  lcd.setCursor(0, 1); // Move to the second row

  if (value < 400) {
    digitalWrite(LED, HIGH);
    lcd.clear(); // Clear previous display
    lcd.setCursor(0, 1); // Set cursor to second row
    lcd.write((uint8_t)0); // Display happy face when LED is ON
  } else {
    digitalWrite(LED, LOW);
    lcd.clear(); // Clear previous display
    lcd.setCursor(0, 1); // Set cursor to second row
    lcd.write((uint8_t)1); // Display sad face when LED is OFF
  }

  delay(500); // Add a delay for stability
}

