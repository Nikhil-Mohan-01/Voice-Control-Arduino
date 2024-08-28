import speech_recognition as sr
import serial
import time
import keyboard  

arduino = serial.Serial('COM7', 9600, timeout=1)  
time.sleep(2)  

def get_voice_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)  
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"You Said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
        except sr.RequestError:
            print("Sorry, the service is down.")
        return None

def send_command_to_arduino(command):
    arduino.write((command + '\n').encode())  
    print(f"Sent to Arduino: {command}")

if __name__ == "__main__":
    while True:
        if keyboard.is_pressed('q'):
            print("Exiting...")
            arduino.close()
            break

        print("Hold the spacebar to give a command...")
        keyboard.wait('space') 
        
        command = get_voice_command()
        
        if command:
            if  "exit" in command:
                print("Exiting...")
                arduino.close()
                break
            
            send_command_to_arduino(command)
