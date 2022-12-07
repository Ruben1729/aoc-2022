from textwrap import wrap

crateMap = [[], [], [], [], [], [], [], [], []]

with open('./input.txt', 'r') as cratesFile:
    for line in cratesFile:
        if "move" in line:
            instructions = line.split()

            print(instructions)

            for i in range(int(instructions[1])):
                crateMap[int(instructions[5]) - 1].append(crateMap[int(instructions[3]) - 1].pop())
        else:
            crateCol = wrap(
                line,
                4,
                drop_whitespace=False,
                break_on_hyphens=False
            )

            if len(crateCol) == 1 or crateCol[0].strip() == "1":
                continue

            for i in range(len(crateCol)):
                if crateCol[i].strip() != "":
                    crateMap[i].insert(0, crateCol[i].strip())

print("Solution 1")
for i in range(len(crateMap)):
    print(crateMap[i].pop())


crateMap = [[], [], [], [], [], [], [], [], []]

with open('./input.txt', 'r') as cratesFile:
    for line in cratesFile:
        if "move" in line:
            instructions = line.split()
            popIndex = len(crateMap[int(instructions[3]) - 1]) - int(instructions[1])

            for i in range(int(instructions[1])):
                crateMap[int(instructions[5]) - 1].append(crateMap[int(instructions[3]) - 1].pop(popIndex))
        else:
            crateCol = wrap(
                line,
                4,
                drop_whitespace=False,
                break_on_hyphens=False
            )

            if len(crateCol) == 1 or crateCol[0].strip() == "1":
                continue

            for i in range(len(crateCol)):
                if crateCol[i].strip() != "":
                    crateMap[i].insert(0, crateCol[i].strip())

print("Solution 2")
for i in range(len(crateMap)):
    print(crateMap[i].pop())