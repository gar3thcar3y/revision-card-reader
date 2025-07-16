from PyPDF2 import PdfFileReader
import os, pickle, time
from tkinter import filedialog




file_path = filedialog.askopenfilename()
pdf = PdfFileReader(file_path)

name = input("new name: ")

def remove_rubbish(string, answer=False):
    new = ""
    if not answer:
        for char in string:
            if char == "?" or char == ".":
                break
            else:
                new = new + char
        return new
    else:
        add = False
        for char in string:
            if char == "?" or char == ".":
                if add == True:
                    break
                else:
                    add = True
            else:
                if add == True:
                    new = new + char
        return new

#def remove_rubbish(string,  answer=False):
#    if answer:
#        for i in range(len(string)):
#            if i 
#        string = list(string)
#        del string[len(string)-47: len(string)-1]
#        return "".join(string)

i = 2

questions = []
answers = []
scores = []
print("[", end="")
while i < pdf.numPages:
    page_obj = pdf.getPage(i)
    answers.append(remove_rubbish(page_obj.extract_text(), answer=True))
    page_obj = pdf.getPage(i-1)
    questions.append(remove_rubbish(page_obj.extract_text()))
    scores.append(0)
    i += 2
    print("-", end="")
print("]")

with open('compiled/'+name, 'wb') as f:
    pickle.dump([questions, answers, scores, 0], f)

print("[Proccess Complete]")
time.sleep(2)