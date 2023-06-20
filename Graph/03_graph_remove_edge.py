class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ':', self.adj_list[vertex])
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def add_edge(self,v1,v2):
        if v1 in  self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False

    def remove_edge(self,v1,v2):
        if v1 in  self.adj_list.keys() and v2 in self.adj_list.keys():
            try:
                self.adj_list[v1].remove(v2)    
                self.adj_list[v2].remove(v1)    
            except ValueError:
                pass
            return True
        return False
    
g1 = Graph()

g1.add_vertex('A')
g1.add_vertex('B')
g1.add_vertex('C')
g1.add_vertex('D')

g1.add_edge('A','B')
g1.add_edge('B','C')
g1.add_edge('C','A')
g1.remove_edge('D','B')
g1.print_graph()