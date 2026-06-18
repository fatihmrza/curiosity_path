__author__ = "8500551, Mirza"
from apply_algorithm import greedy_progress
from apply_algorithm import recursive_progress
import Graph
""" This module includes a main function to execute the algorithm """


def main():
    """ The main function executes according to user input greedy algorithm or recursive algorithm
    P.s: We put any doctest in main function.
    """
    graph = Graph.Graph()
    while True:

        choice = input(
            "Which algorithm would you like to execute? "
            "(1: Greedy algorithm 2: Recursive algorithm q: quit): "
            )

        if choice == "q":
            break
        try:
            test = int(choice)
            if test not in [1, 2]:
                print("Please enter (1,2)")
                continue
            if test == 1:
                path, cost, prize = greedy_progress(graph)
                print("According to greedy algorithm: ")
                print(f"The best path is: {path} ", f"The total cost: {cost}", f"The prize: {prize}", sep="\n")
            if test == 2:
                path, cost, prize = recursive_progress(graph, "start", "end")
                print("According to recursive algorithm: ")
                print(f"The best path is: {path} ", f"The total cost: {cost}", f"The prize: {prize}", sep="\n")
        except ValueError:
            print("Please enter (1,2)")


if __name__ == "__main__":
    main()
