import math
import re


def get_dimension(mx):
    mx = re.sub(r'\s+', '', mx)  # delete the spaces
    mx_elements_count = len(mx)
    dim = int(math.sqrt(mx_elements_count))
    return dim


def make_connections_out_of_matrix(mx, letters, dim):
    mx = re.sub(r'\s+', '', mx)  # delete the spaces
    substrings = [mx[i:i + dim] for i in range(0, len(mx), dim)]  # divide into 15 elements
    x, y = 0, 0
    edges_array = []  # connections array
    for i in substrings:
        for char in i:
            if char == '1':
                edges_array.append(f'{letters[x]}{letters[y]}')
            y = 0 if y == dim - 1 else y + 1
        x += 1
    return edges_array


def checking_for_loop(arr):
    pattern = r'(\w)\1'
    for i in arr:
        if bool(re.search(pattern, i)):  # searching for connections like xRx
            return True
    return False


def checking_for_acyclicity(edges, dim, letters_array):
    if checking_for_loop(edges):  # if matrix has loops then immediately not acyclic
        return False

    filtered_edges = {}
    for k in range(dim):  # sorting the connections due to first element
        row_edges = [edge for edge in edges if edge[0] == letters_array[k]]
        filtered_edges[letters_array[k]] = row_edges

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
            print(f'For {key}-node cycle found: {value}')
            return False
    return True


# нижній переріз
def lower_section(edges, letters):
    l_section = {}
    for letter in letters:
        l_edges = []
        for edge in edges:
            if edge[0] == letter:
                l_edges.append(edge[1])
        l_section[letter] = l_edges
    return l_section


# верхній переріз
def upper_section(edges, letters):
    u_section = {}
    for letter in letters:
        l_edges = []
        for edge in edges:
            if edge[1] == letter:
                l_edges.append(edge[0])
        u_section[letter] = l_edges
    return u_section



