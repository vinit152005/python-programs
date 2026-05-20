questions = (" What is the largest ocean on Earth?",
            "Which planet in our solar system is closest to the Sun?",
            "What is the hardest natural substance available on Earth?",
            "Which country is famously known as the Land of the Rising Sun?",
            "How many bones does an adult human body typically have?")

options = (("A. Atlantic Ocean","B. Pacific Ocean","C. Indian Ocean","D. Arctic Ocean"),
          ("A. Mercury","B. Venus","C. Earth","D. Mars"),
          ("A. Gold","B. Iron","C. Diamond","D. Quartz"),
          ("A. China","B. Japan","C. South Korea","D. Thailand"),
          ("A. 156","B. 206","C. 256","D. 306"))

question_no = 0
guess = []
answer = ["B" , "A" , "C" ,"B" ,"B"]
score = 0


for question in questions:
    print("---------------------------------------")
    print(question)
    for option in options[question_no]:
         print(option)

    user_answer = input("choose the correct option: ").upper()
    guess.append(user_answer)
    if user_answer == answer[question_no]:
        print("you choose correct option")
        score +=1
    else:
        print(f"incorrect , option {answer[question_no]} is correct")
    question_no +=1

print("-----------RESULT-----------")
print(f"Correct answer: {answer}")
print(f"Selected answers: {guess}")
print(f"you score {score} out 5")





