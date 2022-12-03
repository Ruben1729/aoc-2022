i_Elf = 0
caloriesList = [0]

with open('./input.txt', 'r') as caloryFile:
    for line in caloryFile:
        if line == "\n":
            i_Elf += 1
            caloriesList.append(0)
        else :
            caloriesList[i_Elf] += int(line)

caloriesList.sort(reverse=True)

print("Solution 1: " + str(max(caloriesList)))
print("Solution 2: " + str(caloriesList[0] + caloriesList[1] + caloriesList[2]))
