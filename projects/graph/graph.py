"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

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

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # make a queue
        q = Queue()
        #enqueue our starting node
        q.enqueue(starting_vertex)
        #make a set to track if we've been here before
        visited = set()

        # while our queue isn't empty
        while q.size() > 0:
            ## dequeue whatever's at the front of our line, this is our current_node
            current_node = q.dequeue()
            ## if we havent visited this node yet
            if current_node not in visited:
                ### mark as visited
                visited.add(current_node)
                ### print the vertex
                print(current_node)
                ### get its neighbors
                neighbors = self.get_neighbors(current_node)
                ### for each of the neighbors
                for neighbor in neighbors:
                    #### add to queue
                    q.enqueue(neighbor)

    '''    
    ------->
    q = Queue()
    visited = set(1)
    current_node = 1
    neighbors = [2]
    '''
    # 1 --> 2
    #  \
    #   \
    #    7

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
        visited = set()

        # while our stack isn't empty
        while s.size() > 0:

            ## pop off whatever's on top, this is current_node
            current_node = s.pop()
            ## if we haven't visited this vertex before
            if current_node not in visited:
                ### mark as visited  
                visited.add(current_node)
                ### print or /function to perform(added to parameters)
                print(current_node)
                ### get its neighbors
                ### for each of the neighbors
                for neighbor in self.get_neighbors(current_node):
                    #### add to our stack
                    s.push(neighbor)          
    '''
    s = Stack()
    visited = set(1)
    current_node = 1
    neighbors = [2]
    '''

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # visited = set()
        #Find base case
        '''
        if starting_vertex in self.vertices:     
            print(starting_vertex)
        else:
            for vertex in self.get_neighbors(starting_vertex):
                #print("vertex: ", vertex)
                print(vertex)
                if vertex not in visited:
                    self.dft_recursive(vertex, visited)
        '''
        visited.add(starting_vertex)
        print(starting_vertex)
        neighbors = self.get_neighbors(starting_vertex)
        for neighbor in neighbors:
            if neighbor not in visited:
                self.dft_recursive(neighbor, visited)
        

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
        """
        # Create an empty queue and enqueue A PATH TO the starting vertex ID
        q = Queue()
        q.enqueue([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        
        # While the queue is not empty..
        while q.size() > 0:
            # Dequeue the first PATH
            path = q.dequeue()
            # Grab the last vertex from the PATH
            last_node = path[-1]
            # If that vertex has not been visited...
            if last_node not in visited:
                # CHECK IF IT'S THE TARGET
                if last_node == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_node)
                # Then add A PATH TO its neighbors to the back of the queue
                for next_nbr in self.get_neighbors(last_node):
                    new_path = list(path)
                    # COPY THE PATH so we don't mutate the original path
                    new_path.append(next_nbr)
                    #print("new path:", new_path)
                    # APPEND THE NEIGHOR TO THE BACK
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # Create an empty Stack and push A PATH TO the starting vertex ID
        s = Stack()
        s.push([starting_vertex])
        # Create a Set to store visited vertices
        visited = set()
        # While the Stack is not empty...
        while s.size() > 0:
            # push the first PATH
            path = s.pop()
            # Grab the last vertex from the PATH
            last_v = path[-1]
            # If that vertex has not been visited...
            if last_v not in visited:
                # CHECK IF IT'S THE TARGET
                if last_v == destination_vertex:
                    # IF SO, RETURN PATH
                    return path
                # Mark it as visited...
                visited.add(last_v)
                    # Then add A PATH TO its neighbors to the back of the stack
                for next_nbr in self.get_neighbors(last_v):
                    # COPY THE PATH
                    new_path = list(path)
                    new_path.append(next_nbr)
                    #print("stack new path: ",new_path)
                    # APPEND THE NEIGHOR TO THE BACK
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex,path=[],visited=set() ):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
                    explore(graph) {
                visit(this_vert);
                explore(remaining_graph);
            }
        """
        #new_path = [starting_vertex]
        # Mark our node as visited
        path = path + [starting_vertex]
        visited.add(starting_vertex)
        # Check if it's our target node if so return
        if starting_vertex == destination_vertex:
            return path
        ## iterate over neighbor
        neighbors = self.get_neighbors(starting_vertex)
        ### Check if it's visited
        for neighbor in neighbors:
            if neighbor not in visited:
        ### If not, recurse with a path
                result = self.dfs_recursive(neighbor, destination_vertex, path,visited)
        #### If this recursion returns a path
                if result is not None:
        ##### Return from here
                    return result

        # new_path = path + [starting_vertex]
        # visited.add(starting_vertex)
        #find base case:
        # if starting_vertex == destination_vertex:
        #     print("path: ",new_path)
        #     return new_path

        # for neighbor in self.get_neighbors(starting_vertex):
        #     print("vertex dfs: ",starting_vertex)
        #     if neighbor not in visited:
        #         neigh_path = self.dfs_recursive(neighbor,destination_vertex, visited, new_path)
        #         print("path dfs recursive", new_path)
        #         return neigh_path
                    

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
