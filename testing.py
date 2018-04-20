from __future__ import division

import networkx as nx
import matplotlib.pyplot as plt

#Must comment out import below when doing plots due to circular dependencies
import centrality

import correlation
import robustness
import randomNetworks


#--------------------------------------------------------------------------------
# Datasets

# Dolphins Network
G = nx.read_gml('dolphins.gml');

#G = randomNetworks.erdos_renyi(100,0.3)

# Football network
#G = nx.read_gml('football.gml');


# Karate Club Network
#G = nx.read_gml('karate.gml',label='id');
# For this data-set, need to use the functions which end in 2 as defined in centrality.py


#Celegans Neural Network
#G = nx.read_gml('celegansneural.gml')
#G = nx.Graph(G)


#Pollitical Blogs Network
#G = nx.read_gml('polblogs.gml')
#G = nx.Graph(G)
#G = max(nx.connected_component_subgraphs(G), key=len)



#--------------------------------------------------------------------------------

#List of all graph nodes
graphNodeList = G.nodes();

#diamater of the graph
diameter = nx.diameter(G)

ballRadius = diameter * 0.3
# ball of distance 'minimum'
# funtion of the graphs diamater- maximum eccentricity

#total number of nodes in the network
N = nx.number_of_nodes(G);

#total number of edges
m = nx.number_of_edges(G)

#--------------------------------------------------------------------------------
#Gather all nodes to set C that are within the reach of Node i (one hop)
# I.e connected / neighbour nodes

def getNeighbours(node):
    neighbors = list(G.neighbors(node));
    return neighbors

#--------------------------------------------------------------------------------

def nodesInBall(v):
    nodesWithinDistance = []
    for node in graphNodeList:
        #ignore if considering same node
        if node == v:
            continue
        if(nx.shortest_path_length(G, source=node, target=v) <= ballRadius):
            nodesWithinDistance.append(node)
    return nodesWithinDistance


# Procedure Seperation

def seperation(v, ballNodes):

    seperation = 0.0;

    scale1 = 6;
    totalInteractions = 0.0;

    for node in ballNodes:
        totalInteractions += G.degree(node)

    seperation  = totalInteractions / len(ballNodes)
    seperation = seperation / scale1;
    return seperation;


#--------------------------------------------------------------------------------

# Procedure 'Average' Interaction

def interaction(node, neighbours):

    interaction = 0.0;
    averageInteraction = 0.0;

    scale2 = 5; # scaling factor

    # sum of degrees of neighbouring nodes
    for neighbourNode in neighbours:
            interaction += G.degree(neighbourNode)

    # Division by number of neighbours
    averageInteraction = interaction / len(neighbours)

    interaction = averageInteraction / G.degree(node)

    #reflect the degree of a node
    interaction += G.degree(node)

    # This value is divided by a scaling factor
    interaction = interaction / scale2
    return interaction

#--------------------------------------------------------------------------------

#Procedure Relative Vector(Node Jj, set of neighbours C

def relative(v, ballNodes):

    relative = 0.0;

    #make a copy of the graph
    Gcopy = G.copy()

    for node in ballNodes:
        if(Gcopy.has_edge(node,v)):
            relative += Gcopy.degree(node)
            continue
            #add an edge, edge from v to every node in ballRadius
        Gcopy.add_edge(node, v);
        relative += Gcopy.degree(node)
            
    relative = relative / len(ballNodes)

    relative = relative / Gcopy.degree(v)

    relative = relative + Gcopy.degree(v)

    #print relative
    return relative

#--------------------------------------------------------------------------------

#Flocking Algorithm
def fbcm(G):

    nodes = G.nodes();

    centralityNetwork = 0.0;
    testCentrality = 0.0;
    networkNode = None;

    newDictionary = {}

    for node in nodes:
        neighbourNodes = getNeighbours(node);
        nodesinBall = nodesInBall(node);
        vr = relative(node, nodesinBall);
        vi = interaction(node, neighbourNodes);
        vs = seperation(node, nodesinBall);

        testCentrality = vr + vi + vs;

        newDictionary[node] = testCentrality;

        if testCentrality > centralityNetwork:
            centralityNetwork = testCentrality;
            networkNode = node;

    # print networkNode
    # print centralityNetwork


    # Returns a sorted dictionary of FBCS centrality VALUES
    for key, value in sorted(newDictionary.iteritems(), key=lambda (k,v): (v,k), reverse=True):
        print key,  value


    # Returns a sorted list by NAME for statistical analysis
    _list = []
    for key, value in sorted(newDictionary.iteritems()):
        #print "%s: %s" % (key, value)
        temp = [value]
        _list.append(temp)

    return _list

import time
t0 = time.time()

fbcm(G)
t1 = time.time()
print t1-t0
