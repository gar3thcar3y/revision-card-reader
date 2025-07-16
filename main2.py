import pyttsx3, os, time, pickle
from tkinter import filedialog



file_path = filedialog.askopenfilename()

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

with open(file_path, "rb") as f:
    loaded_obj = pickle.load(f)
    questions = loaded_obj[0]
    answers = loaded_obj[1]
    scores = loaded_obj[2]


def ask(string, valid=[]):
    inp = input(string)
    if inp in valid:
        return inp
    else:
        return ask(string, valid=valid)
    
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

RUN = True

i = int(input("question to start at: "))
while i < len(questions) and RUN:
    print(questions[i])
    speak(questions[i].strip("\n"))
    input("next > ")
    print(answers[i])
    speak(answers[i].strip("\n"))
    if ask("understood > ", valid=["y", "n"]) == "y":
        scores[i] += 1
    else:
        scores[i] -= 1

    print("\n")
    i += 1