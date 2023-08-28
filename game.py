import json
import random
import html
import time

if __name__ == "__main__":
    MAX_PLAYERS = 8
    MAX_ROUNDS = 50

    with open("questions.json", "r") as file:
        questions = json.load(file)

    num_players = int(input("How many players are there: "))
    if num_players > MAX_PLAYERS:
        raise ValueError(f"Max number of players is {MAX_PLAYERS}.")

    num_rounds = int(input("How many rounds would you like to play: "))
    if num_rounds > MAX_ROUNDS:
        raise ValueError(f"Max number of rounds is {MAX_ROUNDS}.")

    round = 1
    scores = [0 for _ in range(num_players)]

    while round <= num_rounds:
        print(f"\n\nROUND {round}")
        for player in range(num_players):
            question = random.choice(questions)
            print(f"Player {player + 1}'s turn.")
            print(f"\tCategory - {question['category']}")
            print(f"\tDifficulty - {question['difficulty']}")
            print(f"\t{html.unescape(question['question'])}")
            selections = question["incorrect_answers"] + [question["correct_answer"]]
            random.shuffle(selections)
            for i in range(len(selections)):
                print(f"\t{i + 1}. {html.unescape(selections[i])}")
            selection = (
                int(input("\tPlease enter the number corresponding to your answer: "))
                - 1
            )
            if selections[selection] == question["correct_answer"]:
                scores[selection] += 1
                print(f"\tCorrect!")
            else:
                print(
                    f"\tIncorrect! The correct answer was {html.unescape(question['correct_answer'])}."
                )
            questions.remove(question)
            time.sleep(0.5)
        print("SCOREBOARD")
        for player in range(num_players):
            print(f"\tPlayer {player + 1}: {scores[player]}")
        time.sleep(3)
        round += 1
