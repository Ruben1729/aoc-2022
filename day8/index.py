from functools import reduce  # Required in Python 3
import operator

visibleTrees = 0
treeMap = []

with open('./input.txt', 'r') as treeMapFile:
    for line in treeMapFile:
        treeMap.append(list(map(int, list(line.strip()))))

visibleTrees += len(treeMap) * 2
visibleTrees += len(treeMap[0]) * 2
visibleTrees -= 4

for i in range(len(treeMap)):
    if i == 0 or i == len(treeMap) - 1:
        continue
    for j in range(len(treeMap[i])):
        if j == 0 or j == len(treeMap[i]) - 1:
            continue

        isVisible = False

        for k in range(i):
            isVisible=True
            if treeMap[i-(k+1)][j] >= treeMap[i][j]:
                isVisible = False
                break

        if isVisible:
            visibleTrees += 1
            continue

        for k in range(len(treeMap) - i - 1):
            isVisible = True
            if treeMap[i+(k+1)][j] >= treeMap[i][j]:
                isVisible = False
                break

        if isVisible:
            visibleTrees += 1
            continue

        for k in range(j):
            isVisible = True
            if treeMap[i][j-(k+1)] >= treeMap[i][j]:
                isVisible = False
                break

        if isVisible:
            visibleTrees += 1
            continue

        for k in range(len(treeMap) - j - 1):
            isVisible = True
            if treeMap[i][j+(k+1)] >= treeMap[i][j]:
                isVisible = False
                break

        if isVisible:
            visibleTrees += 1


print("Solution 1: ", visibleTrees)

scenicScores = []
currentScenicScore = [0, 0, 0, 0]

for i in range(len(treeMap)):
    if i == 0 or i == len(treeMap) - 1:
        continue

    for j in range(len(treeMap[i])):
        currentScenicScore = [0, 0, 0, 0]
        if j == 0 or j == len(treeMap[i]) - 1:
            continue

        for k in range(i):
            if treeMap[i-(k+1)][j] < treeMap[i][j]:
                currentScenicScore[0] += 1
            else:
                currentScenicScore[0] += 1
                break

        for k in range(len(treeMap) - i - 1):
            if treeMap[i+(k+1)][j] < treeMap[i][j]:
                currentScenicScore[1] += 1
            else:
                currentScenicScore[1] += 1
                break

        for k in range(j):
            if treeMap[i][j-(k+1)] < treeMap[i][j]:
                currentScenicScore[2] += 1
            else:
                currentScenicScore[2] += 1
                break

        for k in range(len(treeMap) - j - 1):
            if treeMap[i][j+(k+1)] < treeMap[i][j]:
                currentScenicScore[3] += 1
            else:
                currentScenicScore[3] += 1
                break

        if currentScenicScore[0] == i or currentScenicScore[1] + i == len(treeMap) or currentScenicScore[2] == j or currentScenicScore[3] + j == len(treeMap[i]):
            scenicScores.append(reduce(operator.mul, currentScenicScore, 1))

print("Solution 2: ", max(scenicScores))
