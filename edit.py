import pickle, os
from tkinter import ttk
from tkinter import *
from functools import partial
from tkinter import filedialog


file_path = filedialog.askopenfilename()

with open(file_path, "rb") as f:
    loaded_obj = pickle.load(f)
    questions = loaded_obj[0]
    answers = loaded_obj[1]
    scores = loaded_obj[2]

def select_q(choice):
    global type, i, root
    type = "q"
    i = choice
    root.destroy()

def select_a(choice):
    global type, i, root
    type = "a"
    i = choice
    root.destroy()

def end():
    global run, root
    run = False
    root.destroy()

def back_page():
    global page, questions, skip, root
    page -= 1
    if page < 0:
        page = len(questions)-1
    root.destroy()
def forward_page():
    global page, questions, skip, root
    page += 1
    if page > len(questions)-1:
        page = 0
    root.destroy()

run = True

type = ""

def chunks(xs, n):
    n = max(1, n)
    return [obj for obj in (xs[i:i+n] for i in range(0, len(xs), n))]

questions = chunks(questions, 10)
answers = chunks(answers, 10)



page = 0

while run:
    skip = False
    root = Tk()
    frm = ttk.Frame(root, padding=10)
    frm.grid()
    for y in range(len(questions[page])):
        ttk.Button(frm, text=questions[page][y], command=partial(select_q, y)).grid(column=0, row=y)
    for y in range(len(answers[page])):
        ttk.Button(frm, text=answers[page][y], command=partial(select_a, y)).grid(column=1, row=y)
    ttk.Button(frm, text="<", command=back_page).grid(column=2, row=0)
    ttk.Button(frm, text=">", command=forward_page).grid(column=3, row=0)
    ttk.Button(frm, text="done", command=end).grid(column=4, row=0)
    root.mainloop()
    if run and (not skip):
        if type == "q":
            questions[page][i] = input("enter new question: ")
        if type == "a":
            answers[page][i] = input("enter new answer: ")
        print("")

with open(file_path, 'wb') as f:
    pickle.dump([[j for sub in questions for j in sub], [j for sub in answers for j in sub], scores, 0], f)