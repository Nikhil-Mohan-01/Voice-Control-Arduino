#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int blueLED = 31;
const int redLED = 35;
const int fan = 37;

void setup() {
    pinMode(blueLED, OUTPUT);
    pinMode(redLED, OUTPUT);
    pinMode(fan, OUTPUT);
    Serial.begin(9600);

    lcd.begin(16, 2);
    lcd.print("Ready");
    delay(2000);
    lcd.clear();
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        command.trim();  

        lcd.clear();
        lcd.setCursor(0, 0);
        lcd.print("Command:");

        if (command == "blue led on") {
            digitalWrite(blueLED, HIGH);
            lcd.setCursor(0, 1);
            lcd.print("Blue LED On");
        } else if (command == "blue led off") {
            digitalWrite(blueLED, LOW);
            lcd.setCursor(0, 1);
            lcd.print("Blue LED Off");
        } else if (command == "red led on") {
            digitalWrite(redLED, HIGH);
            lcd.setCursor(0, 1);
            lcd.print("Red LED On");
        } else if (command == "red led off") {
            digitalWrite(redLED, LOW);
            lcd.setCursor(0, 1);
            lcd.print("Red LED Off");
        } else {
            lcd.setCursor(0, 1);
            lcd.print("Unknown Command");
        }
    }
}
