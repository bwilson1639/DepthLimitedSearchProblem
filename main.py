
initialTuple = [3,3,1,0,0,0]

def depthLimitedSearch(limit):
    return recursiveDLS(initialTuple,None, limit)

def recursiveDLS(inheritedNode, action, limit):

    if inheritedNode == [0,0,0,3,3,1]:
        return 1   #return 1 indicates that the goal has been reached
    elif (limit == 0):
        return 2  #return 2 indicates that there is a limit break

    else:
        cutoffOccured = False

        for node in possibleActions(inheritedNode):





def possibleActions(inheritedNode):

    actionList = []

    if inheritedNode[2] == 1:

        if