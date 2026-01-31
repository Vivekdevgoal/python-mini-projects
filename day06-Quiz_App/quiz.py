import csv
import random
import os
import time

ques_file = "cse_dataset.csv"
questions = []

    
def load_ques():
    global questions
    try:
        if os.path.exists(ques_file):
            with open(ques_file,'r',encoding = "utf-8-sig") as qf:
                reader = csv.DictReader(qf,delimiter=';')
                questions = list(reader)

            print("question loaded.",len(questions))
    except FileNotFoundError:
        print("csv file not founds")
        questions = []

def start_quiz():
    score = 0
    total = 0

    random.shuffle(questions)

    for qf in questions:
        print("\n" + qf["Question"])

        options = [
            qf["Option A"],
            qf["Option B"],
            qf["Option C"],
            qf["Option D"]
        ]

        for i, opt in enumerate(options, 1):
            print(f"{i}. {opt}")

        ans = input("Enter option number: ")
        if ans == 'q':
            print("Exiting this quiz mode...")
            break


        letters = ["A", "B", "C", "D"]
        user_letter = letters[int(ans) - 1]

        if user_letter == qf["Answer"].strip().upper():
            print("✅ Correct")
            score += 1
        
        else:
            print("❌ Wrong")
        total += 1

    print("\nFinal Score:", score, "/", total)

def fast_quiz():
    score = 0
    attempted = 0
    start_time = time.time()
    time_limit = 2*60
    random.shuffle(questions)

    print("time available is 2 min")
    print("Questions are unlimited!!!")
    print("accept the challenge and go ahead!!!")

    for qf in questions:
        if time.time()- start_time > time_limit:
            print("\n⏰ Time Up!")
            break
        
        print("\n"+ qf["Question"])
        options = [
            qf["Option A"],
            qf["Option B"],
            qf["Option C"],
            qf["Option D"]
            ]
        for i,opt in enumerate(options,1):
             print(f"{i}. {opt}")

        ans = input("Enter Number:")
        if ans == 'q':
            print("Exiting this quiz mode...")
            break


        letters = ["A", "B", "C", "D"]
        user_letter = letters[int(ans) - 1]

        if user_letter == qf["Answer"].strip().upper():
            print("✅ Correct")
            score += 1
        else:
            print("❌ Wrong")
        attempted += 1
    print("\nFinal Score:", score, "/", attempted)       

def timed_quiz():
    score = 0
    time_limit = 30*60
    start_time = time.time()
    total_que = 30
    total = 30
    random.shuffle(questions)

    for qf in questions:
        if time.time()- start_time > time_limit:
            print("\n⏰ Time Up!")
            break
        
        if total == 0:
            print("\n 30 questions completed.")
            break
        
        print("\n"+ qf["Question"])
        options = [
            qf["Option A"],
            qf["Option B"],
            qf["Option C"],
            qf["Option D"]
            ]
        for i,opt in enumerate(options,1):
             print(f"{i}. {opt}")

        ans = input("Enter Number:")
        if ans == 'q':
            print("Exiting this quiz mode...")
            break


        letters = ["A", "B", "C", "D"]
        user_letter = letters[int(ans) - 1]

        if user_letter == qf["Answer"].strip().upper():
            print("✅ Correct")
            score += 1
        else:
            print("❌ Wrong")
        total -= 1
    print("\nFinal Score:", score, "/", total_que)  


def sudden_death_mode():
    score = 0
    total = 0
    random.shuffle(questions)

    for qf in questions:
        
        print("\n"+ qf["Question"])
        options = [
            qf["Option A"],
            qf["Option B"],
            qf["Option C"],
            qf["Option D"]
            ]
        for i,opt in enumerate(options,1):
             print(f"{i}. {opt}")

        ans = input("Enter Number:")
        if ans == 'q':
            print("Exiting this quiz mode...")
            break


        letters = ["A", "B", "C", "D"]
        user_letter = letters[int(ans) - 1]

        if user_letter == qf["Answer"].strip().upper():
            print("✅ Correct")
            score += 1
        else:
            total += 1
            print("game over!! wrong answer!!")
            break
        total += 1
    print("\nFinal Score:", score, "/", total)  
    
def progressive_mode():
    score = 0
    total_que = 15
    progress = 1
    count = 0
    total = 0
    random.shuffle(questions)
    
    for qf in questions:
        if total_que == 0:
            print("questions completed.")
            break

        print("\n"+ qf["Question"])
        options = [
            qf["Option A"],
            qf["Option B"],
            qf["Option C"],
            qf["Option D"]
            ]
        for i,opt in enumerate(options,1):
             print(f"{i}. {opt}")

        ans = input("Enter Number:")
        if ans == 'q':
            print("Exiting this quiz mode...")
            break


        letters = ["A", "B", "C", "D"]
        user_letter = letters[int(ans) - 1]

        if user_letter == qf["Answer"].strip().upper():
            print("✅ Correct")
            score += progress
            progress += 1
        else:
            print("❌ Wrong")
            score -= 1
            progress = 1
        total_que -= 1
        total += 1
    print("\nFinal Score:", score, "/", total)  
    
def quiz_menu():
    while True:
        print("******QUIZ MENU********")
        print("1. Fast Round.")
        print("2. 30 min - 30 ques ")
        print("3. Sudden Death Mode")
        print("4. progressive reward mode ")
        print("5. exit")

        choice = input("enter the task no. : ")

        if choice == '1':
            fast_quiz()

        elif choice == '2':
            timed_quiz()

        elif choice == '3':
            sudden_death_mode()

        elif choice == '4':
            progressive_mode()
            
        elif choice == '5':         
            print("exiting the Quiz App.")
            break

        else:
            print("enter the valid task No.")

def main():
    load_ques()

    while True:
        print("******MENU********")
        print("1. Start simple Quiz.")
        print("2. Try Different Modes.")
        print("3.exit")

        choice = input("enter the task no. : ")

        if choice == '1':
            start_quiz()

        elif choice == '2':
            quiz_menu()

        elif choice == '3':
            print("exiting the Quiz App.")
            break

        else:
            print("enter the valid task No.")

if __name__ == "__main__":
    main()
