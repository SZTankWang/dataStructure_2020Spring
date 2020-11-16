from graph import Graph
from linked_queue import LinkedQueue
def BFS(g, s, discovered_list):
    """
    :param g: Graph -- the graph
    :param s: Vertex -- the starting vertex for BFS
    :param discovered_list: List[Vertex] -- use this to mark discovered vertices

    Perform BFS of the undiscovered portion of Graph g starting at Vertex s.
    
    :return: Nothing, discovered_list will contain BFS order as you mark.
    """
    # To do task 4
    curr_level = LinkedQueue()
    next_level = LinkedQueue()
    curr_level.enqueue(s)
    discovered_list[s] = 'Marked'
    while curr_level.is_empty() == False:
        currNode = curr_level._head
        while currNode != None:
            Vertex = currNode._element
            #check every adjacent nodes with current Vertex
            for edge in g.incident_edges(Vertex):
                dst = edge.opposite(Vertex) #opposite vertex
                #check if dst already checked
                if discovered_list.get(dst) is not None:
                    continue
                discovered_list[dst] = 'Marked'
                next_level.enqueue(dst) #enqueue newly discovered node
            currNode = currNode._next
        #second while loop quit, clearing curr_level queue
        while curr_level.is_empty() != True:
            curr_level.dequeue()
        #transferring all next_level vertex to curr_level
        while next_level.is_empty() != True:
            memo = next_level.dequeue()
            curr_level.enqueue(memo)
    

def DFS(g, s, discovered_list):
    """
    :param g: Graph -- the graph
    :param s: Vertex -- the starting vertex for DFS
    :param discovered_list: List[Vertex] -- use this to mark discovered vertices

    Perform DFS of the undiscovered portion of Graph g starting at Vertex s.
    
    :return: Nothing, discovered_list will contain DFS order as you mark.
    """
    # To do task 5
    if discovered_list.get(s) == 'Marked':
        return discovered_list
    else:
        if discovered_list.get(s) != 'Marked':
            discovered_list[s] = 'Marked'
        for edge in g.incident_edges(s):
            dst = edge.opposite(s)
            discovered_list = DFS(g,dst,discovered_list)
        return discovered_list
''' Draws the graph shown in recitation. '''
a = Graph()
# Add vertices
va = a.insert_vertex("A")
vb = a.insert_vertex("B")
vc = a.insert_vertex("C")
vd = a.insert_vertex("D")
ve = a.insert_vertex("E")
vf = a.insert_vertex("F")
vg = a.insert_vertex("G")
# Add edges
a.insert_edge(va, vc)
a.insert_edge(va, vd)
a.insert_edge(vc, vb)
a.insert_edge(vc, vd)
a.insert_edge(vc, ve)
a.insert_edge(ve, vf)
a.insert_edge(vf, vg)
a.insert_edge(vd, vg)
a.insert_edge(vb, vf)

print("------------------ Task 6 --------------------")
print("Your BFS result:")
discovered_list = {}
BFS(a, va, discovered_list)
print(discovered_list)

print("------------------ Task 7 --------------------")
print("Your DFS result:")
discovered_list = {}
DFS(a, va, discovered_list)
print(discovered_list)


