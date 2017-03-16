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
 
 
flag = True
while flag:
    if recognizer() == "quit":
        flag = False
    elif recognizer() == "open file":
        file = open("test.txt", "a")
        new_flag = True
        while new_flag: 
            if recognizer() == "close file":
                file.close()
                new_flag = False 
            else:
                file.write(recognizer() + "\n")
