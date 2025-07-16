import pickle


questions = []
answers = []
scores = []

name = input("name of file: ")
print("")

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

with open('compiled/'+name, 'wb') as f:
    pickle.dump([questions, answers, scores, 0], f)