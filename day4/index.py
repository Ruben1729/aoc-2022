fullyContained = 0

with open('./input.txt', 'r') as elfPairsFile:
    for line in elfPairsFile:
        elfPairs = line.strip().split(",")
        firstElf = list(map(int, elfPairs[0].split('-')))
        secondElf = list(map(int, elfPairs[1].split('-')))

        if (firstElf[0] <= secondElf[0] and firstElf[1] >= secondElf[1]) or (
                firstElf[0] >= secondElf[0] and firstElf[1] <= secondElf[1]):
            fullyContained += 1

    print("Solution 1: " + str(fullyContained))

fullyContained = 0

with open('./input.txt', 'r') as elfPairsFile:
    for line in elfPairsFile:
        elfPairs = line.strip().split(",")
        firstElf = list(map(int, elfPairs[0].split('-')))
        secondElf = list(map(int, elfPairs[1].split('-')))

        if (firstElf[0] <= secondElf[0] <= firstElf[1]) or (
                secondElf[0] <= firstElf[0] <= secondElf[1]):
            fullyContained += 1

    print("Solution 2: " + str(fullyContained))