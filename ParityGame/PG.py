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

    def get_priority(self):
        return self.priority


class ParityGame:
    def __init__(self):
        self.V = []         # all nodes of the game
        self.V0 = []        # all nodes belonging to player 0
        self.V1 = []        # all nodes belonging to player 1
        self.E = []         # all edges between the nodes
        self.omega = {}     # maps the priority of a node to the ID of the node

    def add_node(self, id, priority, owner, successors, name=None):
        node = ParityNode(id, priority, owner, successors, name)
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

    def get_node(self, id):
        for node in self.V:
            if node.get_id() == id:
                return node

    def get_edges_v0(self):
        v_ids = [node.get_id() for node in self.V0]
        edges = []
        for edge in self.E:
            if edge[0] in v_ids:
                edges.append(edge)
        return edges

    def get_edges_v1(self):
        v_ids = [node.get_id() for node in self.V1]
        edges = []
        for edge in self.E:
            if edge[0] in v_ids:
                edges.append(edge)
        return edges

    def min_priority(self):
        prio = self.V[0].get_priority()
        for node in self.V:
            n_prio = node.get_priority()
            if n_prio < prio:
                prio = n_prio
        return prio

    def get_nodes_min_priority(self):
        min_prio = self.min_priority()
        nodes = []
        for node in self.V:
            if node.get_priority() == min_prio:
                nodes.append(node)
        return nodes

    def attr(self, i, k, T):
        if k == 0:
            return T
        else:
            attrk = self.attr(i, k - 1, T)
            attrk_ids = [node.get_id() for node in attrk]
            edges0 = self.get_edges_v0()
            edges1 = self.get_edges_v1()
            nodes0 = []
            nodes1 = []
            if i == 0:
                # Follow procedure for player 0
                edges11 = [e[1] for e in edges1]
                for e in edges0:
                    if e[1] in attrk_ids:
                        nodes0.append(self.get_node(e[1]))
                if edges11 in attrk_ids:
                    for e in edges11:
                        nodes1.append(self.get_node(e))
            elif i == 1:
                # Follow procedure for player 1
                edges01 = [e[1] for e in edges0]
                for e in edges1:
                    if e[1] in attrk_ids:
                        nodes1.append(self.get_node(e[1]))
                if edges01 in attrk_ids:
                    for e in edges01:
                        nodes0.append(self.get_node(e))
            attrs = attrk
            for node in nodes0:
                if node not in attrs:
                    attrs.append(node)
            for node in nodes1:
                if node not in attrs:
                    attrs.append(node)
            return attrs

    def remove_nodes(self, nodes):
        self.V = [node for node in self.V if node not in nodes]

    def zielonka(self, p):
        print("length of V: ", len(self.V))
        if len(self.V) == 0:
            return [], []
        else:
            m = self.min_priority()
            M = self.get_nodes_min_priority()
            i = m%2
            print("i: ", i)
            R = self.attr(i, len(self.V), M)
            print("R: ", R)
            self.remove_nodes(R)
            Wi, Wj = self.zielonka(p)
            print("Wi, Wj: ", Wi, Wj)
            if Wj == []:
                Wk = Wi+R
                Wl = []
            else:
                print("i-1: ", i-1)
                print("Wj: ", Wj)
                S = self.attr(i-1, len(self.V), Wj)
                print("S: ", S)
                self.remove_nodes(S)
                Wm, Wn = self.zielonka(p)
                Wk = Wm
                Wl = Wn+S
            return Wk, Wl

    def print_game_result(self, result, p):
        print("Solution for parity {0}:\n".format(p))
        print("\t Wk:\n")
        X = result[0]
        for x in X:
            print("\t\t {0}".format(str(x)))
        print("\t Wl:\n")
        Y = result[1]
        for y in Y:
            print("\t\t {0}".format(str(y)))


def main(PGFile):
    game = ParityGame()
    f= open(PGFile)
    lines = f.readlines()
    if len(lines[0].split(' ')) == 2:
        print("Optional header found:", lines[0])
    for i in range(1, len(lines)):
        parts = lines[i].split(' ')
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
    result = game.zielonka(0)
    game.print_game_result(result, 0)
    result = game.zielonka(1)
    game.print_game_result(result, 1)


if __name__== "__main__":
    PGFile = str(sys.argv[1])
    main(PGFile)
