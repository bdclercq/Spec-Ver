import sys
import math

class TransitionSystem:
    def __init__(self):
        self.variables = 0
        self.inputs = []
        self.latches = []
        self.outputs = []
        self.gates = []
        self.states = []

    def readFile(self, file=sys.argv[1]):
        with open(file) as f:
            line = f.readline()
            header = line.splitlines()[0].split(' ')
            print(header)
            self.variables = int(header[1])
            self.inputs = [0 for i in range(int(header[2]))]
            self.latches = [0 for i in range(int(header[3]))]
            self.outputs = [0 for i in range(int(header[4]))]
            self.gates = [0 for i in range(int(header[5]))]
            for i in range(int(header[2])):
                line = f.readline()
                self.inputs[i] = line.splitlines()[0]
            print(self.gates)
            for i in range(int(header[3])):
                line = f.readline()
                self.latches[i] = line.splitlines()[0]
            print(self.latches)
            for i in range(int(header[4])):
                line = f.readline()
                self.outputs[i] = line.splitlines()[0]
            print(self.outputs)
            for i in range(int(header[5])):
                line = f.readline()
                self.gates[i] = line.splitlines()[0]
            print(self.gates)
            assert len(self.inputs)+len(self.latches)+len(self.gates) == self.variables

    def createStates(self):
        states = int(math.pow(2,(len(self.inputs)+len(self.latches))))
        print(states)
        style = "{0:0"
        style += str(len(self.inputs))
        style += "b}"
        for i in range(states):
            # Add bits for inputs to the states
            state = []
            inputs = [int(i) for i in style.format(i)]
            # Add result for gates
            for gate in self.gates:
                gate_parts = gate.split(' ')
                part0 = int(gate_parts[0])
                part1 = math.floor(int(gate_parts[1])/2-1)
                part2 = math.floor(int(gate_parts[2])/2-1)
                if part0%2 == 0:
                    result = int(inputs[part1])&int(inputs[part2])
                else:
                    result = int(not int(inputs[part1])&int(inputs[part2]))
                inputs.append(result)
            state.append(inputs)
            print(inputs)
            self.states.append(inputs)
        print(self.states)

TS = TransitionSystem()
TS.readFile()
TS.createStates()