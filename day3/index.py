totalScore = 0

with open('./input.txt', 'r') as rucksackFile:
    for line in rucksackFile:
        compartment = line.strip()
        firstItem = compartment[:len(compartment)//2]
        secondItem = compartment[len(compartment)//2:]

        commonItem = ''.join(set(firstItem).intersection(secondItem))
        if commonItem.islower():
            totalScore += ord(commonItem) - 96
        else:
            totalScore += ord(commonItem) - 64 + 26

    print("Solution 1: " + str(totalScore))

totalScore = 0
elfBags = []

with open('./input.txt', 'r') as rucksackFile:
    for line in rucksackFile:
        elfBags.append(line.strip())

        if len(elfBags) == 3:
            commonItem = ''.join(set(elfBags[0]).intersection(elfBags[1]).intersection(elfBags[2]))

            if commonItem.islower():
                totalScore += ord(commonItem) - 96
            else:
                totalScore += ord(commonItem) - 64 + 26

            elfBags = []

    print("Solution 2: " + str(totalScore))