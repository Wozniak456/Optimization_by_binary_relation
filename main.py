import re
import graphviz


def make_connections_out_of_matrix(mx):
    mx = re.sub(r'\s+', '', mx)  # delete the spaces
    substrings = [mx[i:i + dimension] for i in range(0, len(mx), dimension)]  # divide into 15 elements
    x, y = 0, 0
    edges_array = []  # connections array
    for i in substrings:
        for char in i:
            if char == '1':
                edges_array.append(f'{letters[x]}{letters[y]}')
            y = 0 if y == dimension - 1 else y + 1
        x += 1
    return edges_array


def checking_for_loop(arr):
    pattern = r'(\w)\1'
    for i in arr:
        if bool(re.search(pattern, i)):  # searching for connections like xRx
            return True
    return False


def checking_for_acyclicity(arr, dimens, letters_array):
    if checking_for_loop(arr):  # if matrix has loops then immediately not acyclic
        return False

    filtered_edges = {}
    for k in range(dimens):  # sorting the connections due to first element
        row_edges = [edge for edge in edges if edge[0] == letters_array[k]]
        filtered_edges[letters_array[k]] = row_edges
    print(filtered_edges)

    for key, value in filtered_edges.items():  # implementation of transitive closure
        for letter in value:
            middle = letter[1]
            for key2, value2 in filtered_edges.items():
                if key2 == middle:
                    for letter2 in value2:
                        end = letter2[1]
                        if f'{key}{end}' not in value:
                            filtered_edges[key].append(f'{key}{end}')
        if checking_for_loop(value):    # if transitive closure has connections like xRx then immediately not acyclic
            print(f'для {key} знайдено цикл: {value}')
            return False
    return True


if __name__ == '__main__':
    # our matrix: 0 and 1 with spaces
    dimension = 15
    matrix = """
 0  0  0  0  1  0  1  0  1  0  1  1  1  0  1 
 1  0  1  1  1  0  0  1  1  0  1  1  1  0  0 
 1  0  0  0  0  0  1  0  1  1  0  0  0  1  1 
 0  0  0  0  0  0  1  1  0  1  1  1  0  1  1 
 0  0  0  1  0  0  1  0  1  0  0  0  0  1  0 
 1  0  0  0  0  0  1  0  1  1  0  0  1  1  0 
 0  0  0  0  0  0  0  1  1  1  0  0  1  0  0 
 0  0  0  0  0  0  0  0  0  1  0  0  0  0  0 
 0  0  0  0  0  0  0  1  0  1  1  1  1  1  1 
 0  0  0  0  0  0  0  0  0  0  0  1  1  0  0 
 0  0  0  0  0  0  0  1  0  1  0  1  0  1  0 
 0  0  0  0  0  0  0  0  0  0  0  0  1  1  1 
 0  0  0  0  0  0  0  0  0  0  0  0  0  0  0 
 0  0  0  0  0  0  0  0  0  0  0  0  1  0  1 
 0  0  0  0  0  0  0  0  0  0  0  0  1  0  0 
"""
    # using the library Digraph to visualize the graph
    dot = graphviz.Digraph(comment='Graph')

    # the titles of rows and columns
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']

    # interpret matrix into connections
    edges = make_connections_out_of_matrix(matrix)

    # add connections into the graph
    dot.edges(edges)

    # creation pdf file with graph
    dot.render('graph-output/graph.gv', view=True)  # створений граф

    # checking for acyclicity
    if not checking_for_acyclicity(edges, dimension, letters):
        print('не ациклічний. є цикл')
    else:
        print('цикл не знайшовся. БВ ациклічне')




