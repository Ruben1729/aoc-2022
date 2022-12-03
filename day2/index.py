totalScore = 0

ROCK_S = 1
PAPER_S = 2
SCISSORS_S = 3

with open('./input.txt', 'r') as strategyGuideFile:
    for line in strategyGuideFile:
        moveChoice = line.split(" ")

        # Rock
        if moveChoice[1].strip() == "X":
            totalScore += 1

            if moveChoice[0].strip() == "A": # Rock
                totalScore += 3
            elif moveChoice[0].strip() == "B": # Paper
                totalScore += 0
            elif moveChoice[0].strip() == "C": # Scissors
                totalScore += 6

        # Paper
        elif moveChoice[1].strip() == "Y":
            totalScore += 2

            if moveChoice[0].strip() == "A": # Rock
                totalScore += 6
            elif moveChoice[0].strip() == "B": # Paper
                totalScore += 3
            elif moveChoice[0].strip() == "C": # Scissors
                totalScore += 0

        # Scissors
        elif moveChoice[1].strip() == "Z":
            totalScore += 3

            if moveChoice[0].strip() == "A": # Rock
                totalScore += 0
            elif moveChoice[0].strip() == "B": # Paper
                totalScore += 6
            elif moveChoice[0].strip() == "C": # Scissors
                totalScore += 3

print("Solution 1: " + str(totalScore))

totalScore = 0
with open('./input.txt', 'r') as strategyGuideFile:
    for line in strategyGuideFile:
        moveChoice = line.split(" ")

        # Rock
        if moveChoice[0].strip() == "A":
            if moveChoice[1].strip() == "X":  # Lose
                totalScore += 0
                totalScore += SCISSORS_S
            elif moveChoice[1].strip() == "Y":  # Draw
                totalScore += 3
                totalScore += ROCK_S
            elif moveChoice[1].strip() == "Z":  # Win
                totalScore += 6
                totalScore += PAPER_S

        # Paper
        elif moveChoice[0].strip() == "B":
            if moveChoice[1].strip() == "X":  # Lose
                totalScore += 0
                totalScore += ROCK_S
            elif moveChoice[1].strip() == "Y":  # Draw
                totalScore += 3
                totalScore += PAPER_S
            elif moveChoice[1].strip() == "Z":  # Win
                totalScore += 6
                totalScore += SCISSORS_S

        # Scissors
        elif moveChoice[0].strip() == "C":
            if moveChoice[1].strip() == "X":  # Lose
                totalScore += 0
                totalScore += PAPER_S
            elif moveChoice[1].strip() == "Y":  # Draw
                totalScore += 3
                totalScore += SCISSORS_S
            elif moveChoice[1].strip() == "Z":  # Win
                totalScore += 6
                totalScore += ROCK_S


    print("Solution 2: " + str(totalScore))