
# Christian Johnston
# Program to illustrate traditional centrality measures

################################################################################
import correlation
import robustness
#import FBCS

import networkx as nx
import matplotlib.pyplot as plt
import time


import operator
# this is needed for finding max degree centrality

################################################################################
            #Data-sets

#read GML file dataset

#G = nx.read_gml('dolphins.gml');

G = nx.read_gml('football.gml');

#G = nx.read_gml('karate.gml',label='id');
# for this data-set, need to use the '2' functions...

#G = nx.read_gml('celegansneural.gml')
#G = nx.Graph(G)

#G = nx.read_gml('polblogs.gml')
#G = nx.Graph(G)

#G = nx.Graph()


#G = nx.fast_gnp_random_graph(10000, 0.1)

################################################################################
n = nx.number_of_nodes(G);
m = nx.number_of_edges(G)


#prints basic info about graph
#print nx.info(G)
################################################################################

def getMaxDegree():
    nodeList = G.nodes()
    maximum = 0.0
    for node in nodeList:
        if (G.degree(node) > maximum):
            maximum = G.degree(node)
    return maximum

################################################################################


# DEGREE CENTRALITY

# The degree centrality values are normalized by
# dividing by the maximum possible degree.

# For example.
# Highest degree of dolphins = 12 ---> the values used in paper
# Number of nodes -1 = 61
# 12/61 = 1.9672  ---> the values we get.


def getNodeDegreeCentrality(node):
    degreeDictionary = nx.degree_centrality(G)
    nodeDegree = degreeDictionary[str(node)]
    nodeDegree = nodeDegree * (nx.number_of_nodes(G)-1);
    return nodeDegree

def getAverageDegreeCentrality():
    degreeDictionary = nx.degree_centrality(G)
    averageNodeDegree = sum(degreeDictionary.values()) / len(degreeDictionary)
    averageNodeDegree = averageNodeDegree * (nx.number_of_nodes(G)-1);
    return averageNodeDegree

def largestDegreeCentralityNode():
    degreeDictionary = nx.degree_centrality(G)
    nodeName = max(degreeDictionary.iteritems(), key=operator.itemgetter(1))[0]
    nodeDegree = degreeDictionary[str(nodeName)]
    nodeDegree = nodeDegree * (nx.number_of_nodes(G)-1);
    return nodeDegree

def largestDegreeCentralityNode2():
    degreeDictionary = nx.degree_centrality(G)
    nodeKey = max(degreeDictionary.iteritems(), key=operator.itemgetter(1))[0]
    if nodeKey in degreeDictionary:
        nodeDegree = degreeDictionary[nodeKey]
    nodeDegree = nodeDegree * (nx.number_of_nodes(G)-1);
    return nodeDegree

def largestDegreeCentralityNodeName():
    degreeDictionary = nx.degree_centrality(G)
    nodeName = max(degreeDictionary.iteritems(), key=operator.itemgetter(1))[0]
    return nodeName

################################################################################

# CLOSENESS CENTRALITY

# Notice the change to 'min' as measuring 'shortest' path distances
# Thus to get their answer, 1/ans.

def getNodeClosenessCentrality(node):
    closenessDictionary = nx.closeness_centrality(G)
    nodeCloseness = closenessDictionary[str(node)]
    nodeCloseness = 1/nodeCloseness;
    return nodeCloseness

def getAverageClosenessCentrality():
    closenessDictionary = nx.closeness_centrality(G)
    averageNodeCloseness = sum(closenessDictionary.values()) / len(closenessDictionary)
    averageNodeCloseness = 1/averageNodeCloseness;
    return averageNodeCloseness

def largestClosenessCentralityNode():
    closenessDictionary = nx.closeness_centrality(G)
    nodeName = max(closenessDictionary.iteritems(), key=operator.itemgetter(1))[0]
    nodeCloseness = closenessDictionary[str(nodeName)]
    return nodeCloseness

def largestClosenessCentralityNode2():
    closenessDictionary = nx.closeness_centrality(G)
    nodeKey = max(closenessDictionary.iteritems(), key=operator.itemgetter(1))[0]
    nodeCloseness = closenessDictionary[nodeKey]
    return nodeCloseness


def largestClosenessCentralityNodeName():
    closenessDictionary = nx.closeness_centrality(G)
    nodeName = max(closenessDictionary.iteritems(), key=operator.itemgetter(1))[0]
    return nodeName

################################################################################

# BETWEENESS CENTRALITY

def getNodeBetweenessCentrality(node):
    betweenDictionary = nx.betweenness_centrality(G)
    nodeBetweeness = betweenDictionary[str(node)]
    return nodeBetweeness

def getAverageBetweenessCentrality():
    betweenDictionary = nx.betweenness_centrality(G)
    averageNodeBetweeness = sum(betweenDictionary.values()) / len(betweenDictionary)
    return averageNodeBetweeness

def largestBetwenessCentralityNode():
    # Can set this to normalised or not- implementation choice
    betweenDictionary = nx.betweenness_centrality(G, normalized=False)
    nodeName = max(betweenDictionary.iteritems(), key=operator.itemgetter(1))[0]
    nodeBetweeness = betweenDictionary[str(nodeName)]
    return nodeBetweeness

def largestBetwenessCentralityNode2():
    # Can set this to normalised or not- implementation choice
    betweenDictionary = nx.betweenness_centrality(G, normalized=False)
    nodeKey = max(betweenDictionary.iteritems(), key=operator.itemgetter(1))[0]
    if nodeKey in betweenDictionary:
        nodeBetweeness = betweenDictionary[nodeKey]
    nodeBetweeness = betweenDictionary[nodeKey]
    return nodeBetweeness

def largestBetwenessCentralityNodeName():
    betweenDictionary = nx.betweenness_centrality(G)
    nodeName = max(betweenDictionary.iteritems(), key=operator.itemgetter(1))[0]
    return nodeName

################################################################################

# EIGENVECTOR CENTRALITY

# Eigenvector centrality is such that the node of greatest centrality
# must have a value of 1.
# thus all values are / greatest centrality value


def getNodeEigenvectorCentrality(node):
     eigenvectorDictionary = nx.eigenvector_centrality(G)
     nodeEigenvector = eigenvectorDictionary[str(node)]
     return nodeEigevnector

def getAverageEigenvectorCentrality():
     eigenvectorDictionary = nx.eigenvector_centrality(G)
     averageNodeEigenvector = sum(eigenvectorDictionary.values()) / len(eigenvectorDictionary)
     return averageNodeEigenvector

def largestEigenvectorCentralityNode():
    eigenvectorDictionary = nx.eigenvector_centrality(G)
    nodeName = max(eigenvectorDictionary.iteritems(), key=operator.itemgetter(1))[0]
    nodeEigenvector = eigenvectorDictionary[str(nodeName)]
    return nodeEigenvector

def largestEigenvectorCentralityNode2():
    eigenvectorDictionary = nx.eigenvector_centrality(G)
    nodeKey = max(eigenvectorDictionary.iteritems(), key=operator.itemgetter(1))[0]
    if nodeKey in eigenvectorDictionary:
        nodeBetweeness = eigenvectorDictionary[nodeKey]
    nodeEigenvector = eigenvectorDictionary[nodeKey]
    return nodeEigenvector

def largestEigenvectorCentralityNodeName():
    eigenvectorDictionary = nx.eigenvector_centrality(G)
    nodeName = max(eigenvectorDictionary.iteritems(), key=operator.itemgetter(1))[0]
    return nodeName


################################################################################


# Colouring the node of greatest centrality red

def colourNode():
    max1 = []
    max2 = []
    max3 = []
    max4 = []
    max5 = []

    # print taken out


    labels = {}

    node = largestDegreeCentralityNodeName();
    max1.append(node)
    node = largestClosenessCentralityNodeName();
    max2.append(node)
    node = largestBetwenessCentralityNodeName();
    max3.append(node)
    node = largestEigenvectorCentralityNodeName();
    max4.append(node)
    node = FBCS.fbcmName(G)
    max5.append(node)

    pos=nx.spring_layout(G);
    nx.draw(G, pos=pos, node_color='b', node_size=8, with_labels=False)
    nx.draw_networkx_nodes(G, pos, nodelist=max1, node_color='r')
    nx.draw_networkx_nodes(G, pos, nodelist=max2, node_color='g')
    nx.draw_networkx_nodes(G, pos, nodelist=max3, node_color='y')
    nx.draw_networkx_nodes(G, pos, nodelist=max4, node_color='c')
    nx.draw_networkx_nodes(G, pos, nodelist=max5, node_color='b')


    nodeName = largestDegreeCentralityNodeName()
    nodeCentrality = str(largestDegreeCentralityNode2())

    print "Node of largest degree centrality = "  + str(nodeName) + ", value = " + nodeCentrality

    nodeName = largestClosenessCentralityNodeName()
    nodeCentrality = str(largestClosenessCentralityNode2())

    print "Node of largest closeness centrality = "  + str(nodeName) + ", value = " + nodeCentrality

    nodeName = largestBetwenessCentralityNodeName()
    nodeCentrality = str(largestBetwenessCentralityNode2())

    print "Node of largest betweeness centrality = "  + str(nodeName) + ", value = " + nodeCentrality

    
    nodeName = largestEigenvectorCentralityNodeName()
    nodeCentrality = str(largestEigenvectorCentralityNode2())

    print "Node of largest eigenvector centrality = "  + str(nodeName) + ", value = " + nodeCentrality

    nodeName = FBCS.fbcmName(G)
    nodeCentrality = str(FBCS.fbcmValue(G))

    print "Node of largest FBCS centrality = "  + str(nodeName) + ", value = " + nodeCentrality

    return None

################################################################################

# Running methods
# print "maximum degree = " + str(getMaxDegree())
# print "Centralization value using betweeness centrality: " + str(centralisation());


#colourNode();
#plt.show()


#This function gets a list of values to compare FBCS statistically to
#List is ordered by node name.
def getComparisonList(G):
    list1 = []
    dictionary = nx.eigenvector_centrality(G)
    for key, value in sorted(dictionary.iteritems()):
        #print "%s: %s" % (key, value)
        temp = [value]
        list1.append(temp)
    return list1

#--------------------------------------------------------------------------
# This section is for correlation

'''
list1 = []
dictionary = nx.closeness_centrality(G)
for key, value in sorted(dictionary.iteritems()):
    print "%s: %s" % (key, value)
    temp = [value]
    list1.append(temp)
list1 = [y for x in list1 for y in x]


list2 = []
closenessDictionary = nx.eigenvector_centrality(G)
for key, value in sorted(closenessDictionary.iteritems()):
    #print "%s: %s" % (key, value)
    temp2 = [value]
    list2.append(temp2)
list2 = [y for x in list2 for y in x]


#list = getComparisonList(G)
#print list
tau = correlation.kendallsTau(list1, list2)
print tau

'''
################################################################################

# This is for robustness tests


def robustnessAddNodes(G):
    # Adding nodes 
    # List 2 will have more elements

    dictionary1 = nx.degree_centrality(G)

    G = robustness.addNodes(G,n)

    dictionary2 = nx.degree_centrality(G)

    dictionary3 = {}
    #change this slightly for removing nodes
    for key in dictionary2:
        if key in dictionary1:
            dictionary3[key] = dictionary2[key]

    list1 = []
    for key, value in sorted(dictionary1.iteritems()):
        temp = [value]
        list1.append(temp)

    list3 = []
    for key, value in sorted(dictionary3.iteritems()):
        temp = [value]
        list3.append(temp)


    tau = correlation.kendallsTau(list1, list3)
    print tau
    return tau

def robustnessRemoveNodes(G):
    # Adding nodes 
    # List 1 will have more elements

    dictionary1 = nx.degree_centrality(G)

    G = robustness.removeNodes(G,n)

    dictionary2 = nx.degree_centrality(G)

    dictionary3 = {}
    #change this slightly for removing nodes
    for key in dictionary1:
        if key in dictionary2:
            dictionary3[key] = dictionary1[key]

    list1 = []
    for key, value in sorted(dictionary2.iteritems()):
        temp = [value]
        list1.append(temp)

    list3 = []
    for key, value in sorted(dictionary3.iteritems()):
        temp = [value]
        list3.append(temp)


    tau = correlation.kendallsTau(list1, list3)
    print tau
    return tau

#robustness.addNodes(G)
#robustness.removeNodes(G)

'''
total = 0
iterations = 10
for i in range(iterations):
    G = nx.read_gml('football.gml');
    G = nx.Graph(G)
    list1 = getComparisonList(G)
    robustness.addEdges(G,m)
    #robustness.removeEdges(G,m)
    list2 = getComparisonList(G)
    tau = correlation.kendallsTau(list1, list2)
    total += tau
total = total / iterations
print total * total
'''


#nx.eigenvector_centrality(G)


# For timing 
# time python centrality.py

################################################################################

# To draw network
#colourNode()
#nx.draw(G)
#plt.show()

# to run: python filename.py



