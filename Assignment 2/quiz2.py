import random
import datetime
class Question:
    def __init__(self, line, answer):
        self.line = line
        self.answer = answer
#====================================================================
with open('quiz.txt','r') as f:
    question_line = f.readlines()

name = input("Please enter your name: ")

questions = [
    Question(question_line[0], "1955"),
    Question(question_line[1], "Jupiter"),
    Question(question_line[2], "Pod"),
    Question(question_line[3], "Alexander Fleming"),
    Question(question_line[4], "12"),
    Question(question_line[5], "Real"),
    Question(question_line[6], "Copper and tin"),
    Question(question_line[7], "Fungi"),
    Question(question_line[8], "No charge"),
    Question(question_line[9], "Nitrogen"),
                ]
#=====================================================================
def quiz(questions):
    score = 0
    random.shuffle(questions)

    for question in questions:
        question.line = question.line[:-2]
        answer = input(question.line)
        answer_strip = answer.strip()
        print("")
#=====================================================================
        if answer_strip == question.answer.lower():
            score += 1
            print("That is the correct answer! ")
            print("")

        elif answer_strip != question.answer.lower():
            print("Incorrect! The correct answer is.",question.answer)
            print("")
#=====================================================================
    date = datetime.datetime.now()
    results = open("results.txt", "a+")
    results.write("{0} : {1} : {2}\n".format(name, score, date))
    results.close()
#=====================================================================
#def leaderboard(questions, run_quiz):
    #file = open("results.txt","r")
    #print("The Current Leaderboard for This Quiz: \n")
    #for line in file:
        #data = line.split(":")
        #username = data[0]
        #score = data[1]           
        #print("")
        #print(username,"=",score)
        #file.close()
        #SystemExit()

quiz(questions)
#leaderboard(questions, quiz)

#display leaderboard displaying other users that did the quiz - another read file - descending order - append
#create own set of questions for new quiz of my making. Give user choice of which quiz to takel
