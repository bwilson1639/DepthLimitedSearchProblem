
initialTuple = [3,3,1,0,0,0]


def depthLimitedSearch(limit):
    return recursiveDLS(initialTuple, limit)

def recursiveDLS(inheritedNode, limit):

    if inheritedNode == [0,0,0,3,3,1]:
        return 1   #return 1 indicates that the goal has been reached
    elif (limit == 0):
        return 2  #return 2 indicates that there is a limit break

    else:
        cutoffOccured = False

        for nodeAction in possibleActions(inheritedNode):

            child = childAction(inheritedNode, nodeAction) # list
            result = recursiveDLS(child, limit - 1)

            if result == 2:
                cutoffOccured = True

            elif result != 0:

                print('At the current ' + inheritedNode + ' you will take the action ' + actionExplain(nodeAction) \
                      + ' and then, your new state is ' + child)
                return result

            if cutoffOccured:
                return 2
            else:
                return 0

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
        node[0] = node[0] - 1
        node[2] = 0
        node[3] = node[3] + 1
        node[5] = 1
        return  node
    if inputedActionString == '2MsideB':
        node[0] = node[0] - 2
        node[2] = 0
        node[3] = node[3] + 2
        node[5] = 1
        return node
    if inputedActionString == '1M1CsideB':
        node[0] = node[0] - 1
        node[1] = node[1] - 1
        node[2] = 0
        node[3] = node[3] + 1
        node[4] = node[4] + 1
        node[5] = 1
        return node
    if inputedActionString == '1CsideB':
        node[1] = node[1] - 1
        node[2] = 0
        node[4] = node[4] + 1
        node[5] = 1
        return node
    if inputedActionString == '2CsideB':
        node[1] = node[1] - 2
        node[2] = 0
        node[4] = node[4] + 2
        node[5] = 1
        return node
    if inputedActionString == '1MsideA':
        node[0] = node[0] + 1
        node[2] = 1
        node[3] + node[3] - 1
        node[5] = 0
        return node
    if inputedActionString == '2MsideA':
        node[0] = node[0] + 2
        node[2] = 1
        node[3] = node[3] - 2
        node[5] = 0
        return node
    if inputedActionString == '1M1CsideA':
        node[0] = node[0] + 1
        node[1] = node[1] + 1
        node[2] = 1
        node[3] = node[3] - 1
        node[4] = node[4] - 1
        node[5] = 0
        return node
    if inputedActionString == '1CsideA':
        node[1] = node[1] + 1
        node[2] = 1
        node[4] = node[4] - 1
        node[5] = 0
        return node
    if inputedActionString == '2CsideA':
        node[1] = node[1] + 2
        node[2] = 1
        node[4] = node[4] + 2
        node[5] = 0
        return node

#takes in a string, returns the string in proper english
def actionExplain(inputString):

    actions = {
        '1MsideB' : '<Move 1 missionary from sideA to sideB>',
        '2MsideB' : '<Move 2 missionaries from sideA to sideB>',
        '1M1CsideB' : '<Move 1 missionary and 1 cannibal from sideA to sideB>',
        '1CsideB' : '<Move 1 cannibal from sideA to sideB>',
        '2CsideB' : '<Move 2 cannibals from sideA to sideB>',
        '1MsideA' : '<Move 1 missionary from sideB to sideA>',
        '2MsideA' : '<Move 2 missionaries from sideB to sideA>',
        '1M1CsideA' : '<Move 1 missionary and 1 cannibal from sideB to sideA>',
        '1CsideA' : '<Move 1 cannibal from sideB to sideA>',
        '2CsideA' : '<Move 2 cannibals from sideB to sideA>'}

    return actions[inputString]

depthLimitedSearch(15)