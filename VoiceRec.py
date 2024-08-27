import speech_recognition as sr
import serial
import time


arduino = serial.Serial('COM3', 9600, timeout=1)  
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
    if command:
        arduino.write((command + '\n').encode()) 

if __name__ == "__main__":
    while True:
        command = get_voice_command()
        if command:
            send_command_to_arduino(command)
            if "exit" in command:
                print("Exiting...")
                arduino.close() 
                break
            else:
                print(f"Command recognized: {command}")
