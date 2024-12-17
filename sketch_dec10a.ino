#include <LiquidCrystal.h>
int ledPin = 9; 
int LDR = A0;    
LiquidCrystal lcd(1, 2, 3, 4, 5, 6);
byte happyFace[8] = {
  B00000,
  B01010,
  B00000,
  B00100,
  B01010,
  B10001,
  B11111,
  B00000
};
byte sadFace[8] = {
  B00000,
  B01010,
  B00000,
  B00100,
  B10001,
  B01010,
  B11111,
  B00000
};
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
  lcd.begin(16, 2);
  lcd.clear();
  lcd.createChar(0, happyFace);
  lcd.createChar(1, sadFace);
  lcd.createChar(2, heart);
  lcd.createChar(3, brokenHeart);
  pinMode(ledPin, OUTPUT);
  pinMode(LDR, INPUT);
}
void loop() {
  int value = analogRead(LDR);

  if (value < 400) {  
    digitalWrite(ledPin, HIGH);  
    for (int pos = 0; pos < 16; pos++) {
      lcd.clear();
      lcd.setCursor(pos, 0);
      lcd.print("The LED is ON");
      lcd.setCursor(0, 1);
      lcd.write(byte(1));  
      lcd.setCursor(15, 1);
      lcd.write(byte(2));  
      delay(200);
    }
  } else {  
    digitalWrite(ledPin, LOW);  
    for (int pos = 0; pos < 16; pos++) {
      lcd.clear();
      lcd.setCursor(pos, 0);
      lcd.print("The LED is OFF");
      lcd.setCursor(0, 1);
      lcd.write(byte(0));  
      lcd.setCursor(15, 1);
      lcd.write(byte(3));  
      delay(200);
    }
  }
}
