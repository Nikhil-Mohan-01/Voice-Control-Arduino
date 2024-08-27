import speech_recognition as sr

def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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
    
if __name__ == "__main__":
    while True:
        command = get_voice_command()
        if command:
            if "exit" in command:
                break
