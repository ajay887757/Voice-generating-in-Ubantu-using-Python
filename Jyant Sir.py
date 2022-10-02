import pyttsx3

engine = pyttsx3.init("espeak")
voices = engine.getProperty("voices")
print("Available voices: ", voices[29])
# engine.setProperty('voice',voices[51].id) #English
engine.setProperty('voice',voices[29].id) #English

# count=0
# for i in voices:
#     print("name",i.name," ",count)    # for generating voice language
#     count+=1

def speak(text):
        print('Rex:' + text)
        engine.say(text)
        engine.runAndWait()

print("On")
speak("kaise hooo bhai")
print("End")












# import pyttsx3

# engine = pyttsx3.init("espeak")
# voices = engine.getProperty('voices')
# engine.setProperty('voice',voices[11].id) #English
# print("Voice ",voices)