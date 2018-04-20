import networkx as nx
import matplotlib.pyplot as plt
import random
from random import choice
from random import randint

#G = nx.read_gml('polblogs.gml')
#G = nx.Graph(G)
################################################################################
#n = nx.number_of_nodes(G);
#m = nx.number_of_edges(G)

# defines the rate of failure
probabilityOfFailure = 0.05


# Function that removes nodes radomly from graph 
# Removes the node and all adjacent edges.
def removeNodes(G,n):
	removedNodes = 0;
	while removedNodes < probabilityOfFailure*n:
		nodes = list(nx.nodes(G))
		node = choice(nodes)
		G.remove_node(node)
		removedNodes += 1
	print removedNodes
	return G

# Function to add a node to the graph 
# degree is equal to a random nodes degree
# ties were also randomly added from the node to other random nodes in the network. 
# Node addition: the insertion of a certain proportion of extra nodes into the network.
def addNodes(G,n):
	nodes = list(nx.nodes(G))
	addedNodes = 0;

	while addedNodes < probabilityOfFailure*n:
		node = choice(nodes)
		degreeScore = G.degree(node)
		_id = randint(0, n)
		G.add_node(_id)
		for i in range (0, degreeScore):
			node = choice(nodes)
			G.add_edge(node, _id)
		addedNodes += 1
	return G


# function which removes random edges depending on a failure frequency
def removeEdges(G,m):
	numberRemoved = 0;
	while numberRemoved < probabilityOfFailure*m:
		edges = nx.edges(G)
		edge = choice(list(edges))
		G.remove_edge(edge[0], edge[1])
		numberRemoved += 1
	return G


# function which adds random edges between node pairs
# each node is randomly selected with probability proportional to the nodes degree.
def addEdges(G,m):

	numberAdded = 0;

	nodes = nx.nodes(G)
	edges = nx.edges(G)

	while numberAdded < probabilityOfFailure*m:
		#pick a random node
		first_node = choice(list(nodes))

		edge = choice(list(edges))
		#Choose a random edge, then choose randomly one of the nodes it connects
		# Probability is proportional to the vertices degree
		randomNo = random.randint(1,2)
		second_node = edge[randomNo-1]

		# stops the same node from being picked twice 
		if(second_node == first_node):
				second_node = edge[(randomNo+1)%2]
		#checks if there is a link between 2 nodes already 
		if(G.has_edge(first_node, second_node)):
			continue;

		G.add_edge(first_node, second_node)

		numberAdded += 1
	return G



