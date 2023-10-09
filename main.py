import graphviz
from graph_functions import *


if __name__ == '__main__':
    # our matrix: 0 and 1 with spaces
    matrix = """
0 0 1 0
0 0 1 1
0 0 0 1
1 0 0 0
"""
    # using the library Digraph to visualize the graph
    dot = graphviz.Digraph(comment='Graph')

    dimension = get_dimension(matrix)

    # the titles of rows and columns
    letters = []
    for i in range(dimension):
        letter = chr(ord('A') + i)  # ord('A') повертає числовий код літери 'A', chr перетворює числовий код у літеру
        letters.append(letter)

    # interpret matrix into connections
    edges = make_connections_out_of_matrix(matrix, letters, dimension)

    # add connections into the graph
    dot.edges(edges)

    # checking for acyclicity
    if not checking_for_acyclicity(edges, dimension, letters):
        print('не ациклічний. є цикл')
    else:
        print('цикл не знайшовся. БВ ациклічне')

    # creation pdf file with graph
    dot.render('graph-output/graph.gv', view=True)




