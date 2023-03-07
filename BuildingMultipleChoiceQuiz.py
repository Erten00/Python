from Question import Question
questionPrompts = [
    "What color are Apples?\n(a) Red/Green\n(b) Purple\n(c) Oragne \n\n"
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yeloww \n\n"
    "What color are Strwaberries?\n(a) Yellow\n(b) Red\n(c) Blue \n\n"
]

questions = [
    Question(questionPrompts[0], "a"),
    Question(questionPrompts[1], "c"),
    Question(questionPrompts[2], "b"),
]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(questionPrompts)
        if answer == questions.answer:
            score += 1
    print("You got " + str(score)+ "/" + str(len(questions))+ "correct")

run_test(questions)