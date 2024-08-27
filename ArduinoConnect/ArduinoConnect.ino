const int blueLED = 31;  
const int redLED = 35;  

void setup() {
    pinMode(blueLED, OUTPUT);
    pinMode(redLED, OUTPUT);
    Serial.begin(9600); 
}

void loop() {
    if (Serial.available() > 0) {
        String command = Serial.readStringUntil('\n');
        command.trim();  

        if (command == "B1") {
            digitalWrite(blueLED, HIGH);  
        } else if (command == "B0") {
            digitalWrite(blueLED, LOW);  
        }
        if (command == "R1") {
            digitalWrite(redLED, HIGH);  
        } else if (command == "R0") {
            digitalWrite(redLED, LOW);  
        }
    }
}
