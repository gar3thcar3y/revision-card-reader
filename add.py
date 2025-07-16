import pickle, os
from tkinter import ttk
from tkinter import *
from functools import partial
from tkinter import filedialog


print("select file")
directories = os.listdir("compiled")

file_path = filedialog.askopenfilename()

with open(file_path, "rb") as f:
    loaded_obj = pickle.load(f)
    questions = loaded_obj[0]
    answers = loaded_obj[1]
    scores = loaded_obj[2]


run = True

while run:
    question = input("enter question: ")
    if question == "finish":
        run = False
    else:
        questions.append(question)
        answers.append(input("enter answer: "))
        scores.append(0)
        print("")

with open(file_path, 'wb') as f:
    pickle.dump([questions, answers, scores, 0], f)