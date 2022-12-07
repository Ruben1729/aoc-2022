packetLen = 0

with open('./input.txt', 'r') as packetFile:
    for line in packetFile:
        line = line.strip()
        for i in range(len(line)):
            currentSet = set(line[i:4+i:1])
            if len(currentSet) == 4:
                packetLen = i + 4
                break
    print("Solution 1", packetLen)

with open('./input.txt', 'r') as packetFile:
    for line in packetFile:
        line = line.strip()
        for i in range(len(line)):
            currentSet = set(line[i:14+i:1])
            if len(currentSet) == 14:
                packetLen = i + 14
                break
    print("Solution 2", packetLen)