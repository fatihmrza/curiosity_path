__author__ = "8500551, Mirza"
import optimisation
import Graph
""" 
This module contains a graph structure and two other algorithms that calculates a path 
on the graph from 2 points namely start, end.
"""


def greedy_algo(graph, path1, path2):
    """
        This function defines the algorithm named greedy by using 2
        parameters namely path1 and path2. The algorithm going to compare
        2 parameters that called by path1, path2 from dictionary. Where the prize
        bigger is, comes out. path1, path2 are edges in tuple for ex. ("start", "C")
    >>> g = Graph.Graph()
    >>> greedy_algo(g,("B","D"),("B","E"))
    'D'
    >>> greedy_algo(g,None,("B","E"))
    'E'
    >>> greedy_algo(g,("C","E"),("B","end")) # Node is not defined
    Traceback (most recent call last):
    ...
    KeyError: ('C', 'E')
    """
    if path1 is None:
        return path2[1]
    if path2 is None:
        return path1[1]
    # x2,x1 are costs y,y1 are prizes
    x2, y = graph.edges[path1]
    x1, y1 = graph.edges[path2]
    if y1 > y:
        return path2[1]
    else:
        return path1[1]


def greedy_progress(graph):
    """
    This function executes the greedy algorithm on a graph which is defined with class.
    It compares throughout greedy_algo() in every branching two paths and finds the best path
    from start to end.
    >>> graph1 = Graph.Graph()
    >>> graph2 = Graph.Graph()
    >>> graph2.add_edge("C", "D", 3, 6) # We are changing the prize of the path C to D
    True
    >>> graph2.add_edge("D", "C", 3, 6)
    True
    >>> greedy_progress(graph1)
    (['start', 'B', 'D', 'end'], 10, 11)
    >>> greedy_progress(graph2)
    (['start', 'B', 'D', 'C'], 10, 13)
    >>> greedy_progress()
    Traceback (most recent call last):
    ...
    TypeError: greedy_progress() missing 1 required positional argument: 'graph'
    """
    current_node = "start"
    # We defined visited with set() instead of list, because in a set() can be added a parameter only one times.
    visited = set()
    path = [current_node]  # our path, that shows the Nodes in the best path.
    total_cost = 0
    total_prize = 0
    while current_node != "end":
        comparison = []  # We created a list to add two sub path to be easily callable later.

        for i in graph.edges:
            if current_node == i[0] and i[1] not in visited:  # "i" is here a path like ("start", "C")
                comparison.append(i)

        if not comparison:  # If there is no way to go.
            break

        visited.add(current_node)

        if len(comparison) == 1:
            current_node = comparison[0][1]  # If we have only one way to go. (no branching)
        else:
            next_node = greedy_algo(graph, comparison[0], comparison[1])  # it will be chosen by greedy_algo()
            edge = (current_node, next_node)
            cost, prize = graph.edges[edge]
            total_cost += cost
            total_prize += prize
            current_node = next_node

        path.append(current_node)

    return path, total_cost, total_prize


def recursive_progress(graph, current_node, end_node,
                       visited=None, cost=0, prize=0, paths=None):
    """
        This recursive program provides us to find the best path from start to end
        by using recursion. It finds the possible paths with a recursive progress and
        compares the paths with an algorithm named ratio_value() afterward returns the best path.
    >>> graph1 = Graph.Graph()
    >>> graph2 = Graph.Graph()
    >>> graph2.add_node("K")
    True
    >>> graph2.add_node("Y")
    True
    >>> graph2.add_edge("K", "Y", 3, 6)
    True
    >>> graph2.add_edge("Y", "K", 3, 6)
    True
    >>> graph2.add_edge("K", "end", 1, 5)
    True
    >>> graph2.add_edge("B", "Y", 8, 7)
    True
    >>> graph2.add_edge("Y", "B", 8, 7)
    True
    >>> recursive_progress(graph1, "start", "end")
    (['start', 'C', 'D', 'end'], 6, 7)
    >>> recursive_progress(graph2, "start", "end")
    (['start', 'C', 'D', 'B', 'Y', 'K', 'end'], 19, 26)
    >>> recursive_progress(graph1)
    Traceback (most recent call last):
    ...
    TypeError: recursive_progress() missing 2 required positional arguments: 'current_node' and 'end_node'
    """
    # Because of the recursion have to add this for starting. Afterward there will be already a visited and path sets
    if visited is None:
        visited = set()
    if paths is None:
        paths = []

    visited.add(current_node)
    paths.append(current_node)

    if current_node == end_node:
        return paths.copy(), cost, prize  # it stops the recursion

    optimised_path = None
    for (i, j) in graph.edges:
        if current_node == i and j not in visited:
            sub_cost, sub_prize = graph.edges[(i, j)]  # the cost of the part of the whole path. (sub path)
            # now starts the recursion, it finds the all possible path from start to end with loop.
            alternative_path = recursive_progress(graph, j, end_node, visited.copy(),
                                                  cost + sub_cost, prize + sub_prize, paths.copy())
            # The best path will be chosen throughout our algorithm ratio_value() from optimisation modul
            optimised_path = optimisation.ratio_value(optimised_path, alternative_path)

    return optimised_path


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
