import pyttsx3, os, time, pickle
from tkinter import *
from tkinter import ttk
from functools import partial
from tkinter import filedialog


file_path = filedialog.askopenfilename()
print("done")
engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


with open(file_path, "rb") as f:
    loaded_obj = pickle.load(f)
    questions = loaded_obj[0]
    answers = loaded_obj[1]
    scores = loaded_obj[2]

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

def normal():
    global type, root
    type = "1"
    root.destroy()
def aver():
    global type, root
    type = "2"
    root.destroy()


print("type :")
ttk.Button(frm, text="normal", command=normal).grid(column=0, row=0)
ttk.Button(frm, text="ask questiona with score below your average", command=aver).grid(column=0, row=1)
root.mainloop()

averege = sum(scores)/len(scores)
i = input("what question to start at: ")


if i == "l":
    i = loaded_obj[3]
else:
    i = int(i)


HALT1 = False
HALT2 = False


def understood():
    global HALT2, scores, i
    if HALT2:
        HALT2 = False
        scores[i] += 1

def not_understood():
    global HALT2, scores, i
    if HALT2:
        HALT2 = False
        scores[i] -= 1

def see_answer():
    global HALT1
    HALT1 = False

def exit():
    global RUN
    with open(file_path, 'wb') as f:
        pickle.dump([questions, answers, scores], f)
    RUN = False

def repeat():
    global question
    speak(question)

def back():
    global i
    i -= 4

def foward():
    global i
    i += 2



root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Button(frm, text="understood", command=understood).grid(column=1, row=0)
ttk.Button(frm, text="not understood", command=not_understood).grid(column=1, row=1)
ttk.Button(frm, text="see answer", command=see_answer).grid(column=0, row=0)
ttk.Button(frm, text=">", command=foward).grid(column=0, row=1)
ttk.Button(frm, text="<", command=back).grid(column=0, row=2)
ttk.Button(frm, text="repeat", command=repeat).grid(column=0, row=3)
ttk.Button(frm, text="exit", command=exit).grid(column=0, row=4)


RUN = True
root.update()
while i < len(questions) and RUN:
    os.system('cls')
    if type == "2":
        try:
            while scores[i] > averege:
                i += 1
        except:
            break
    answer = answers[i]
    question = questions[i]
    print("question number "+str(i))
    print(question)
    speak(question)
    HALT1 = True
    while HALT1 and RUN:
        root.update()
    if RUN:
        print(answer)
        speak(answer)
        time.sleep(2)
        HALT2 = True
        while HALT2 and RUN:
            root.update()
        i += 1


with open(file_path, 'wb') as f:
    pickle.dump([questions, answers, scores, 0], f)