nodeList = []
DIRECTORY_SIZE = 70000000
UPDATE_SIZE = 30000000

class Node:
    def __init__(self, prev_node, name, size=0):
        self.nextNodes = []
        self.previousNode = prev_node
        self.name = name
        self.size = size

rootNode = Node(None, ".")
currentNode = rootNode

def print_tree(current_node, depth=1):
    print(" - ", current_node.name, "(", current_node.size, ")")
    for next_node in current_node.nextNodes:
        print("    "*depth, end="")
        print_tree(next_node, depth+1)

def update_size(current_node):
    for next_node in current_node.nextNodes:
        current_node.size += update_size(next_node)

    return current_node.size

def find_nodes(current_node):
    if current_node.size <= 100000:
        nodeList.append(current_node.size)

    for next_node in current_node.nextNodes:
        find_nodes(next_node)

def find_smallest_capable_dir(current_node):
    if current_node.size >= UPDATE_SIZE- (DIRECTORY_SIZE - rootNode.size):
        nodeList.append(current_node.size)

    for next_node in current_node.nextNodes:
        find_smallest_capable_dir(next_node)

with open('./input.txt', 'r') as directoryFile:
    for line in directoryFile:
        line = line.strip().split(" ")
        if "cd" in line:
            if line[2] == "..":
                currentNode = currentNode.previousNode
            else:
                nextNode = Node(currentNode, line[2])
                currentNode.nextNodes.append(nextNode)
                currentNode = nextNode
        elif line[0].isnumeric():
            currentNode.size += int(line[0])

rootNode = rootNode.nextNodes[0]

update_size(rootNode)
print_tree(rootNode)
find_nodes(rootNode)

print("Solution 1: ", sum(nodeList))

nodeList = []
find_smallest_capable_dir(rootNode)

print("Solution 2: ", min(nodeList))
