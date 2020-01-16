import sys


class ParityNode:
    def __init__(self, id, priority, owner, successors, name=None):
        self.id = id
        self.priority = priority
        self.owner = owner
        self.successors = successors
        self.name = name

    def __str__(self):
        return "ParityNode: id {0}, priority {1}, owner {2}, successors {3}, name {4}".format(self.id, self.priority,
                                                                                              self.owner,
                                                                                              self.successors,
                                                                                              self.name)

    def get_successors(self):
        return self.successors

    def get_id(self):
        return self.id


class ParityGame:
    def __init__(self):
        self.V = []         # all nodes of the game
        self.V0 = []        # all nodes belonging to player 0
        self.V1 = []        # all nodes belonging to player 1
        self.E = []         # all edges between the nodes
        self.omega = {}     # maps the priority of a node to the ID of the node

    def add_node(self, id, priority, owner, successors, name=None):
        node = ParityNode(id, priority, owner, successors, name)
        print(node)
        self.V.append(node)
        self.omega[str(id)] = priority
        if owner == 1:
            # add to V1
            self.V1.append(node)
        elif owner == 0:
            # add to V0
            self.V0.append(node)

    def add_edges(self):
        # Loop over all nodes, add edge between a node and its successors
        for node in self.V:
            successors = node.get_successors()
            for succ in successors:
                edge = node.get_id(), succ
                self.E.append(edge)

    def get_states_player_1(self):
        return self.V1

    def get_states_player_0(self):
        return self.V0

    def get_states(self):
        return self.V

    def get_edges(self):
        return self.E


def main(PGFile):
    game = ParityGame()
    f= open(PGFile)
    lines = f.readlines()
    if len(lines[0].split(' ')) == 2:
        print("Optional header found:", lines[0])
    for i in range(1, len(lines)):
        parts = lines[i].split(' ')
        print(parts)
        id = int(parts[0])
        priority = int(parts[1])
        owner = int(parts[2])
        successors = []
        s = parts[3].split(',')
        for succ in s:
            successors.append(int(succ))
        if len(parts) == 5:
            game.add_node(id, priority, owner, successors, parts[4])
        else:
            game.add_node(id, priority, owner, successors)
    game.add_edges()


if __name__== "__main__":
    PGFile = str(sys.argv[1])
    main(PGFile)
