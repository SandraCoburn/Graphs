 

'''
Write a function that, given the dataset and the ID of an individual in the dataset,
 returns their earliest known ancestor – the one at the farthest distance 
 from the input individual. If there is more than one ancestor tied for "earliest",
  return the one with the lowest numeric ID. If the input individual has no parents,
   the function should return -1.
'''
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2) 
        else:
            raise IndexError("nonexisten vertex")

    def get_parents(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return -1
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # make a stack
        s = Stack()
        ## push on our starting node
        s.push(starting_vertex)

        # make a set to track if we've been here before
        visited = []

        # while our stack isn't empty
        while s.size() > 0:

            ## pop off whatever's on top, this is current_node
            current_node = s.pop()
            ## if we haven't visited this vertex before
            if current_node not in visited:
                ### mark as visited  
                visited.append(current_node)
                ### print or /function to perform(added to parameters)
                print(current_node)
                ### get its neighbors
                ### for each of the neighbors
                if len(self.get_parents(current_node)) > 0:
                    for neighbor in self.get_parents(current_node):
                        #### add to our stack
                        s.push(neighbor) 
                else:
                    visited.append(None) 
        return visited

def earliest_ancestor(ancestors, starting_node):
    g = Graph()
    # Ancestors is an array of sets
    # Traverse the tree till there is no more ancestors
    # if more than one ancestor have dead ends, return the last value of the longer path
    # check dictionary for vertexes
    # create a graph of vertices and edges using ancestors array
    for ancestor in ancestors:
        #use the second element of each set as the key
        if ancestor[0] not in g.vertices:
            g.add_vertex(ancestor[0])
        if ancestors[1] not in g.vertices:
            g.add_vertex(ancestor[1])
        g.add_edge(ancestor[1], ancestor[0])

    parents = g.dft(starting_node)
    indexes = []

    for i in range(len(parents)-1, -1, -1):
        # If the visited list returns None, save the index in array
        if parents[i] == None:
            indexes.append(i-1)
    max_l = [parents[indexes[0]]]
    for i in range(len(indexes) -1):
        if indexes[i+1] - indexes[i] == -2:
            max_l.append(parents[indexes[i*1]])
    result = min(max_l)
    if result == starting_node:
        return -1
    else:
        print("result is: ",result)
        return result
    



#earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6),], 2)
earliest_ancestor([(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)], 5)