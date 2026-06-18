Path Search on Graphs (Greedy & Recursive) with Runtime Measurement
Overview
This program implements two different approaches to find the best possible path on a graph from the node "start" to the node "end":

a greedy approach that always selects the most attractive next step at each decision point,
a recursive approach that considers multiple possible paths and evaluates them based on a ratio of cost and prize value.

Additionally, there is a runtime measurement module that compares both approaches using time and timeit.
Project Structure
1. Main Module (main)

This module serves as the entry point for the program. The user selects which algorithm to run. The found path as well as the total accumulated cost and prize value are then displayed. Module docstring: "This module includes a main function to execute the algorithm"
2. apply_algorithm.py

This file contains the actual algorithms for path calculation. It accesses the graph structure from Graph.py and evaluation functions from optimisation.py.

Functions included:

greedy_algo(graph, path1, path2): Compares two possible edges based on their prize value from graph.edges and decides in favor of the cheaper option.
greedy_progress(graph): Repeatedly traverses the graph from "start" to "end", making decisions using the greedy principle. Returns the path, total cost, and total prize value.
recursive_progress(graph, current_node, end_node, visited=None, cost=0, prize=0, paths=None): Builds paths using the recursive approach until the target node is reached. Uses ratio_value() from optimisation.py for multi-objective optimization.

3. Graph.py

This module provides the graph data structure. Module docstring: "This module contains a class structure to define a graph"

Core class:

Graph

nodes: initially contains the nodes ["start", "B", "C", "D", "E", "end"]
edges: Dictionary with edge data in the format ((node1, node2) → (cost, prize)). Edges are stored twice since the graph is modeled as undirected. Methods:
add_node(node): adds a new node
add_edge(node1, node2, cost, prize): adds an edge if both nodes exist



4. optimisation.py

This module handles the comparison and evaluation of different paths. Module docstring: "This module includes three algorithm functions for the optimise the specific structure"

Functions included:

ratio_value(r1, r2): Compares two paths based on the prize/cost ratio and handles edge cases such as None or division by zero.
internal_comparison(p1, p2): Prefers paths with a higher prize; in case of a tie, the lower cost decides.
score_cal(path, k1=0.35, k2=0.65): Calculates a weighted score from cost and prize value.

Doctests
Several modules contain doctest sections that are automatically tested upon execution. In the runtime measurement module, some of these tests are only present as comments, because the results vary and would otherwise cause test failures.
