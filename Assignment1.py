from pomegranate import DiscreteDistribution, ConditionalProbabilityTable, Node
from pomegranate.BayesianNetwork import BayesianNetwork

Prob_fn = input("Enter Probability file name (e.g. sample1.tst): ") # sample1.txt
Prob_raw = open(Prob_fn)

# IcyWeather = IW
IW0 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
IW1 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
IcyWeather = DiscreteDistribution({0: IW0, 1: IW1})

# Battery = B
B00 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
B01 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
B10 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
B11 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
Battery = ConditionalProbabilityTable([[0, 0, B00],
                                       [0, 1, B01],
                                       [1, 0, B10],
                                       [1, 1, B11]], [IcyWeather])

# StarterMotor = SM
SM00 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
SM01 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
SM10 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
SM11 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
StarterMotor = ConditionalProbabilityTable([[0, 0, SM00],
                                            [0, 1, SM01],
                                            [1, 0, SM10],
                                            [1, 1, SM11]], [IcyWeather])

# Radio = R
R00 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
R01 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
R10 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
R11 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
Radio = ConditionalProbabilityTable([[0, 0, R00],
                                     [0, 1, R01],
                                     [1, 0, R10],
                                     [1, 1, R11]], [Battery])

# Ignition = I
I00 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
I01 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
I10 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
I11 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
Ignition = ConditionalProbabilityTable([[0, 0, I00],
                                        [0, 1, I01],
                                        [1, 0, I10],
                                        [1, 1, I11]], [Battery])

# Gas = G
G0 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
G1 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
Gas = DiscreteDistribution({0: G0, 1: G1})

# Starts = S
S0000 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S0001 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S0010 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S0011 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S0100 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S0101 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S0110 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S0111 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S1000 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S1001 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S1010 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S1011 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S1100 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S1101 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S1110 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
S1111 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
Starts = ConditionalProbabilityTable([[0, 0, 0, 0, S0000],
                                      [0, 0, 0, 1, S0001],
                                      [0, 0, 1, 0, S0010],
                                      [0, 0, 1, 1, S0011],
                                      [0, 1, 0, 0, S0100],
                                      [0, 1, 0, 1, S0101],
                                      [0, 1, 1, 0, S0100],
                                      [0, 1, 1, 1, S0111],
                                      [1, 0, 0, 0, S1000],
                                      [1, 0, 0, 1, S1001],
                                      [1, 0, 1, 0, S1010],
                                      [1, 0, 1, 1, S1011],
                                      [1, 1, 0, 0, S1100],
                                      [1, 1, 0, 1, S1101],
                                      [1, 1, 1, 0, S1110],
                                      [1, 1, 1, 1, S1111]], [StarterMotor, Ignition, Gas])

# Moves = M
M00 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
M01 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
M10 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
M11 = float(Prob_raw.readline().split('\t')[-1].split('\n')[0])
Moves = ConditionalProbabilityTable([[0, 0, M00],
                                     [0, 1, M01],
                                     [1, 0, M10],
                                     [1, 1, M11]], [Starts])

s1 = Node(IcyWeather, name="IW")
s2 = Node(Battery, name="B")
s3 = Node(StarterMotor, name="SM")
s4 = Node(Radio, name="R")
s5 = Node(Ignition, name="I")
s6 = Node(Gas, name="G")
s7 = Node(Starts, name="S")
s8 = Node(Moves, name="M")

model = BayesianNetwork("CarTrouble")
model.add_nodes(s1, s2, s3, s4, s5, s6, s7, s8)
model.add_edge(s1, s2)
model.add_edge(s1, s3)
model.add_edge(s2, s4)
model.add_edge(s2, s5)
model.add_edge(s3, s7)
model.add_edge(s5, s7)
model.add_edge(s6, s7)
model.add_edge(s7, s8)
model.bake()

print('Model structure: ')
print(model.structure)

Q0 = ['IcyWeather', 'Battery', 'Radio', 'Ignition', 'StarterMotor', 'Gas', 'Starts', 'Moves']
Q1 = ['IW', 'B', 'R', 'I', 'SM', 'G', 'S', 'M']
Qu0 = [None, None, None, None, None, None, None, None]
Query_fn = input("Enter Query file name (e.g. Query.txt): ") #'Query.txt
Query_raw = open(Query_fn)
Query_line = Query_raw.readline()
Query_sample = Query_line.split(',')
index0 = -1
for i in range(len(Query_sample)):
    if Query_sample[i].split('=')[0] in Q0:
        index0 = Q0.index(Query_sample[i].split('=')[0])
    if Query_sample[i].split('=')[0] in Q1:
        index0 = Q1.index(Query_sample[i].split('=')[0])
    if index0 != -1:
        if Query_sample[i].split('=')[1] == 'false':
            Qu0[index0] = False
        elif Query_sample[i].split('=')[1] == 'true':
            Qu0[index0] = True
        else:
            Qu0[index0] = None

print(model.predict([Qu0]))
print(model.predict_proba([Qu0]))