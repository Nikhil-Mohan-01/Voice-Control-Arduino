const int ledPin = 31;  

void setup() {
    pinMode(ledPin, OUTPUT);
    Serial.begin(9600); 
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        command.trim();  

        if (command == "on") {
            digitalWrite(ledPin, HIGH);  
        } else if (command == "off") {
            digitalWrite(ledPin, LOW);  
        }
    }
}
