import speech_recognition as sp

def recognizer():
    rec = sp.Recognizer()
    with sp.Microphone() as source:
        print("say sth")
        audio = rec.listen(source)
    
    try: 
        return rec.recognize_google(audio)
    except sp.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sp.RequestError as SR:
        print("Could not request results from Google Speech Recognition service; {}".format(SR))


if __name__ == "__main__":
    while recognizer() != "close":
        print(recognizer())