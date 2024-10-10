import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os

# Initialize the speech engine
engine = pyttsx3.init()

# Set voice rate (Optional)
engine.setProperty('rate', 150)

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen and recognize voice input
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio)
            print(f"User said: {command}\n")
            return command.lower()
        except sr.UnknownValueError:
            speak("Sorry, I did not catch that.")
            return None
        except sr.RequestError:
            speak("Could not request results, please check your internet connection.")
            return None

# Function to respond to basic commands
def perform_task(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%B %d, %Y")
        speak(f"Today's date is {current_date}")

    elif "search" in command:
        speak("What do you want to search for?")
        search_query = listen()
        if search_query:
            webbrowser.open(f"https://www.google.com/search?q={search_query}")
            speak(f"Here are the results for {search_query}")
    
    elif "chatgpt" in command:
        speak("What do you want to gpt for?")
        chatgpt_query = listen()
        if chatgpt_query:
            webbrowser.open(f"https://www.chatgpt.com/chat?q={chatgpt_query}")
            speak(f"Here are the results for {chatgpt_query}")
    
    elif "youtube" in command:
        speak("What do you want search in youtube?")
        youtube_query = listen()
        if youtube_query:
            webbrowser.open(f"https://www.youtube.com/search?q={youtube_query}")
            speak(f"Here are the results for {youtube_query}")
    
    

    elif "open" in command:
        speak("Which system app would you like to open?")
        open_query = listen()
        if open_query:
            if "notepad" in open_query:
                os.system("notepad.exe")
                speak("Opening Notepad")
            elif "calculator" in open_query:
                os.system("calc.exe")
                speak("Opening Calculator")
            elif "paint" in open_query:
                os.system("mspaint.exe")
                speak("Opening Paint")
            # elif "word" in open_query:
            #     os.system("winword.exe")
            #     speak("Opening Microsoft Word")
            # elif "powerpoint" in open_query:
            #     os.system("powerpnt.exe")
            #     speak("Opening Microsoft PowerPoint")


        
        else:
            speak("I couldn't understand the search query.")

    else:
        speak("I'm sorry, I can't help with that yet.")

# Main function to run the voice assistant
def main():
    speak("Voice assistant activated. How can I help you?")
    
    while True:
        command = listen()
        if command:
            if "exit" in command or "stop" in command:
                speak("Goodbye!, have nice day")
                break
            perform_task(command)

if __name__ == "__main__":
    main()
