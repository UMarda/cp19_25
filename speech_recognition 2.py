import speech_recognition as sr

recording = sr.Recognizer()

with sr.Microphone() as source: recording.adjust_for_ambient_noise(source)
    print("Kindly please say something :")
    audio = recording.listen(source)
    try:
        print("You have said: \n" + recording.recognize_google(audio))
except Exception as e:
        print(e)
