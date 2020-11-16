class Graph:
    """Representation of a simple graph using an adjacency map."""

    #------------------------- nested Vertex class -------------------------
    class Vertex:
        """Lightweight vertex structure for a graph."""
        __slots__ = '_element'
    
        def __init__(self, x):
            """Do not call constructor directly. Use Graph's insert_vertex(x)."""
            self._element = x
    
        def element(self):
            """Return element associated with this vertex."""
            return self._element
    
        def __hash__(self):         # will allow vertex to be a map/set key
            return hash(id(self))

        def __str__(self):
            return str(self._element)

        def __repr__(self):
            return str(self._element)
        
    #------------------------- nested Edge class -------------------------
    class Edge:
        """Lightweight edge structure for a graph."""
        __slots__ = '_origin', '_destination', '_element'
    
        def __init__(self, u, v, x):
            """Do not call constructor directly. Use Graph's insert_edge(u,v,x)."""
            self._origin = u
            self._destination = v
            self._element = x
    
        def endpoints(self):
            """Return (u,v) tuple for vertices u and v."""
            return (self._origin, self._destination)
    
        def opposite(self, v):
            """Return the vertex that is opposite v on this edge."""
            if not isinstance(v, Graph.Vertex):
                raise TypeError('v must be a Vertex')
            return self._destination if v is self._origin else self._origin
            raise ValueError('v not incident to edge')
    
        def element(self):
            """Return element associated with this edge."""
            return self._element
    
        def __hash__(self):         # will allow edge to be a map/set key
            return hash( (self._origin, self._destination) )

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin,self._destination,self._element)

        def __repr__(self):
            return '({0},{1},{2})'.format(self._origin,self._destination,self._element)
        
    #------------------------- Graph methods -------------------------
    def __init__(self, directed=False):
        """Create an empty graph (undirected, by default).

        Graph is directed if optional paramter is set to True.
        """
        self._outgoing = {}
        # only create second map for directed graph; use alias for undirected
        self._incoming = {} if directed else self._outgoing

    def _validate_vertex(self, v):
        """Verify that v is a Vertex of this graph."""
        if not isinstance(v, self.Vertex):
            raise TypeError('Vertex expected')
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')
        
    def is_directed(self):
        """Return True if this is a directed graph; False if undirected.

        Property is based on the original declaration of the graph, not its contents.
        """
        return self._incoming is not self._outgoing # directed if maps are distinct

    def vertex_count(self):
        """Return the number of vertices in the graph."""
        return len(self._outgoing)

    def vertices(self):
        """Return an iteration of all vertices of the graph."""
        return self._outgoing.keys()

    def edge_count(self):
        """Return the number of edges in the graph."""
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges
        return total if self.is_directed() else total // 2

    def edges(self):
        """Return a set of all edges of the graph."""
        result = set()       # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())    # add edges to resulting set
        return result

    def get_edge(self, u, v):
        """Return the edge from u to v, or None if not adjacent."""
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)        # returns None if v not adjacent

    def degree(self, v, outgoing=True):   
        """Return number of (outgoing) edges incident to vertex v in the graph.

        If graph is directed, optional parameter used to count incoming edges.
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):   
        """Return all (outgoing) edges incident to vertex v in the graph.

        If graph is directed, optional parameter used to request incoming edges.
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, x=None):
        """Insert and return a new Vertex with element x."""
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}        # need distinct map for incoming edges
        return v
            
    def insert_edge(self, u, v, x=None):
        """Insert and return a new Edge from u to v with auxiliary element x.

        Raise a ValueError if u and v are not vertices of the graph.
        Raise a ValueError if u and v are already adjacent.
        """
        if self.get_edge(u, v) is not None:      # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e


    def __str__(self):
        result = []
        for each in self.edges():
            result.append(str(each) + "\n")
        return "".join(result)


def main():
    print("------------------ Task 3 --------------------")
    ''' Build two graphs given in the recitation document '''
    g1 = Graph()
    g2 = Graph(True)
    # Your code ........
    #build g1
    A = g1.insert_vertex('A')
    B = g1.insert_vertex('B')
    C = g1.insert_vertex('C')
    D = g1.insert_vertex('D')
    E = g1.insert_vertex('E')
    g1.insert_edge(A, B, 'b')
    g1.insert_edge(A, D, 'a')
    g1.insert_edge(B, D, 'c')
    g1.insert_edge(B, C, 'd')
    g1.insert_edge(D, C, 'e')
    g1.insert_edge(C, E, 'f')
    #build g2
    A1 = g2.insert_vertex('A')
    B1 = g2.insert_vertex('B')
    C1 = g2.insert_vertex('C')
    D1 = g2.insert_vertex('D')
    E1 = g2.insert_vertex('E')
    g2.insert_edge(A1, B1,('b',20))
    g2.insert_edge(A1, D1,('a',5))
    g2.insert_edge(B1, D1,('c',12))
    g2.insert_edge(B1, C1,('d',7))
    g2.insert_edge(C1, E1,('f',9))
    g2.insert_edge(D1, C1,('e',11))
    g2.insert_edge(D1, A1,('a',5))
    
    print(g1)
    print(g2)

    print("------------------ Task 4 --------------------")
    ''' Call Graph.degree(v, outgoing=True). Try to understand this function '''
    # Your code ........
    print(g1.degree(C,True))
    print(g2.degree(C1,True))
    print("------------------ Task 5 --------------------")
    ''' Call Graph.incident_edges(v, outgoing=True). Try to understand this function '''
    # Your code ........
    for edge in g1.incident_edges(C,True):
        print(edge)
    for edge in g2.incident_edges(C1,True):
        print(edge)

if __name__ == '__main__':
    main()




