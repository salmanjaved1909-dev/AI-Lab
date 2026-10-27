scores = [1,2,3,4,5,6,7,8]
treeDepth = 3  

leaves = 0


def minmax(currDepth, nodeIndex, isMaxTurn):
    global leaves
    if currDepth == treeDepth:
        leaves += 1
        return scores[nodeIndex]

    if isMaxTurn:
        return max(
            minmax(currDepth + 1, nodeIndex * 2, False),
            minmax(currDepth + 1, nodeIndex * 2 + 1, False)
        )
    else:
        return min(
            minmax(currDepth + 1, nodeIndex * 2, True),
            minmax(currDepth + 1, nodeIndex * 2 + 1, True)
        )

print(minmax(0, 0, True))
print("Leaves evaluated:", leaves)