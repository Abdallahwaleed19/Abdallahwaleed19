#include <LiquidCrystal.h>
LiquidCrystal Lcd(1,2,3,4,5,6);
int LDR = A0 ; 
int LED = 9 ; 
double value ;
void setup() {
  // put your setup code here, to run once:
  pinMode(LED , OUTPUT);
  pinMode(LDR , INPUT);
  Lcd.begin(16,2);

}

void loop() {
  // put your main code here, to run repeatedly:
  value = analogRead(LDR);
  if (value < 400){
    digitalWrite(LED , HIGH);
    Lcd.setCursor(0,1);
    Lcd.print("The LED is ON ");
    Lcd.scrollDisplayRight();
    delay(500);
  }
  else{
    digitalWrite(LED , LOW);
    Lcd.setCursor(0,1);
    Lcd.print("The LED is OFF ");
    Lcd.scrollDisplayRight();
    delay(500);

  }

}
