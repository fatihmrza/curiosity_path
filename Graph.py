__author__ = "8500551, Mirza"
"""This module contains a class structure to define a graph """


class Graph:
    """
    This Class helps us to define our graph and make it easily callable.
    With the other functions can be extended the graph structure.

    """
    def __init__(self):
        self.nodes = ["start", "B", "C", "D", "E", "end"]
        # We've defined every edge two times to easily be controlled, because the graph is undirected
        self.edges = {
            ("start", "B"): (3, 2),
            ("B", "start"): (3, 2),

            ("start", "C"): (1, 0),
            ("C", "start"): (1, 0),

            ("C", "D"): (2, 3),
            ("D", "C"): (2, 3),

            ("B", "D"): (4, 5),
            ("D", "B"): (4, 5),

            ("B", "E"): (2, 1),
            ("E", "B"): (2, 1),

            ("D", "end"): (3, 4),
            ("end", "D"): (3, 4),

            ("E", "end"): (5, 0),
            ("end", "E"): (5, 0),
        }

    def add_node(self, node):
        """ The function adds a new node to the graph.
        >>> graph = Graph()
        >>> graph.add_node("try")
        True
        >>> graph.add_node("try")
        False
        >>> graph.add_node(or)
        Traceback (most recent call last):
        ...
        SyntaxError: invalid syntax
        """
        if node in self.nodes:
            return False
        else:
            self.nodes.append(node)
            return True

    def add_edge(self, node1, node2, cost, prize):
        """The Function adds edge between two nodes and adds their cost and prize values.
        >>> graph = Graph()
        >>> graph.add_edge('B','C', 10, 2)
        True
        >>> graph.add_edge('D','B', 4 if 5 == 5 else 6, 1)
        True
        >>> graph.add_edge('A','D',None)
        Traceback (most recent call last):
        ...
        TypeError: Graph.add_edge() missing 1 required positional argument: 'prize'
        """
        if node1 in self.nodes and node2 in self.nodes:
            self.edges[(node1, node2)] = (cost, prize)
            return True
        else:
            return False


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
