import graphviz
from graph_functions import *
from NM import *
from k_opt import *

if __name__ == '__main__':
    # our matrix: 0 and 1 with spaces
    matrix = """
 0  1  0  1  0  0  1  0  0  1  0  0  1  1  1 
 0  0  0  0  0  0  0  0  0  1  0  1  0  1  0 
 0  0  0  0  0  0  0  0  0  0  0  1  1  0  1 
 0  1  0  0  1  1  1  1  0  0  1  0  1  1  0 
 1  1  1  0  0  0  1  1  0  1  0  1  0  0  0 
 0  0  0  0  0  0  0  1  1  0  1  0  1  0  1 
 0  1  1  0  0  1  0  1  1  1  1  0  0  1  1 
 0  1  1  0  0  0  0  0  1  1  0  0  1  1  0 
 1  0  0  1  1  0  0  0  0  0  1  1  1  0  1 
 0  0  1  1  0  0  0  0  0  0  1  1  0  1  1 
 1  0  1  0  0  0  0  0  0  0  0  0  0  1  1 
 0  0  0  1  0  0  0  1  0  0  0  0  1  1  1 
 0  0  0  0  0  0  0  0  0  1  0  0  0  1  1 
 0  0  0  0  1  1  0  0  0  0  0  0  0  0  1 
 0  1  0  0  1  0  0  0  0  0  0  0  0  0  0 

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
    print(f'edges: {edges}')
    # add connections into the graph
    dot.edges(edges)

    # creation pdf file with graph
    dot.render('graph-output/graph.gv', view=True)

    is_acyclic = checking_for_acyclicity(edges, dimension, letters)  # нижній переріз
    if is_acyclic:
        print('The graph is acyclic. Using Neumann–Morgenstern algorithm')
        q_result = q_search(upper_section(edges, letters), dimension)
        check(edges, q_result)
    else:
        print('The graph is not acyclic. Using K algorithm')
        k_opt_output(matrix, dimension)



