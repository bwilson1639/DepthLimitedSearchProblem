class Node:

    def __init__(self):

        self.node = [3, 3, 1, 0, 0, 0]

    def move(self, missionary, cannibal):

        if self.node[2] == 1:  # if the boat is on the left side

            if missionary > 0:
                self.node[0] = self.node[0] - missionary

                self.node[3] = self.node[3] + missionary

            if cannibal > 0:
                self.node[1] = self.node[1] - cannibal

                self.node[4] = self.node[4] - cannibal

            self.node[2] = 0
            self.node[5] = 1

        else:  # if the boat is on the right side

            if missionary > 0:
                self.node[3] = self.node[3] - missionary

                self.node[0] = self.node[0] + missionary

            if cannibal > 0:
                self.node[4] = self.node[4] - cannibal

                self.node[1] = self.node[1] - cannibal

            self.node[5] = 0
            self.node[2] = 1

