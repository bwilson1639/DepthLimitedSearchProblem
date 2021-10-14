
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

        for nodeAction in possibleActions(inheritedNode):

            child = childAction(inheritedNode, nodeAction)


#takes in a list, returns a list of strings with possible actions
def possibleActions(inheritedNode):

    actionList = []

    if inheritedNode[2] == 1:

        #check if one missionary can move across to sideB
        if (((inheritedNode[0] - 1) >= inheritedNode[1]) or (inheritedNode[0] == 0)) and ((inheritedNode[3] + 1) >= inheritedNode[4]):
            actionList.append('1MsideB')

        #check if two missionaries can move across to sideB
        if (((inheritedNode[0] - 2) >= inheritedNode[1]) or (inheritedNode[0] == 0)) and ((inheritedNode[3] + 2) >= inheritedNode[4]):
            actionList.append('2MsideB')

        #check if one missionary one cannibal can move across to sideB
        if (((inheritedNode[0] - 1) >= ( inheritedNode[1] - 1)) or (inheritedNode[0] == 0)) and ((inheritedNode[3] + 1) >=(inheritedNode[4] + 1)):
            actionList.append('1M1CsideB')

        #check if one cannibal can move across to sideB
        if (inheritedNode[0] >= (inheritedNode[1] - 1)) and (inheritedNode[3] >= (inheritedNode[4] + 1)):
            actionList.append('1CsideB')

        #check if two cannibals can move across to sideB
        if (inheritedNode[0] >= (inheritedNode[1] -2)) and (inheritedNode[3] >= (inheritedNode[4] +2)):
            actionList.append('2CsideB')

    else:

        #check if one missionary can move across to sideA
        if (((inheritedNode[3] - 1) >= inheritedNode[4]) or (inheritedNode[3] == 0)) and ((inheritedNode[0] + 1) >= inheritedNode[1]):
            actionList.append('1MsideA')

        #check if two missionaries can move across to sideA
        if (((inheritedNode[3] - 2) >= inheritedNode[4]) or (inheritedNode[3] == 0)) and ((inheritedNode[0] +2) >= inheritedNode[1]):
            actionList.append('2MsideA')

        #check if one missionary and one cannibal can move across to sideA
        if((inheritedNode[3] - 1) >= (inheritedNode[4] - 1)) and ((inheritedNode[0] + 2) >= (inheritedNode[1] + 1)):
            actionList.append('1M1CsideA')

        #check if one cannibal can move across to sideA
        if(inheritedNode[3] >= (inheritedNode[4] - 1)) and (inheritedNode[0] >= (inheritedNode[1] + 1)):
            actionList.append('1CsideA')

        #check if two cannibals can move across to sideA
        if (inheritedNode[3] >= (inheritedNode[4] - 2)) and (inheritedNode[0] >= (inheritedNode[1] + 2)):
            actionList.append('2CsideA')

#takes in a string and the parent node, returns a list of the finished action
def childAction(node, inputedActionString):

    if inputedActionString == '1MsideB':
        
