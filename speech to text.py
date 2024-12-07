import speech_recognition as sr

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source,timeout = 1,phrase_time_limit = 5)

    try:
        print("Recognizing....")
        query = sr.recognize_google(audio,language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("can't hear properly..")
        return "none"
    return query
