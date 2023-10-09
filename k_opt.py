import re
import copy


def make_matrix(mx, dim):
    mx = re.sub(r'\s+', '', mx)
    matrix = [[0 for _ in range(15)] for _ in range(15)]
    for i in range(dim):
        for j in range(dim):
            matrix[i][j] = int(mx[i * dim + j])
    return matrix


def make_3_parts_matrix(matrix, dim):
    mx = make_matrix(matrix, dim)
    for i in range(dim):
        for j in range(dim):
            if mx[i][j] == 1 and mx[j][i] == 1:
                mx[i][j], mx[j][i] = 'I', 'I'
            elif mx[i][j] == 1 and mx[j][i] == 0:
                mx[i][j], mx[j][i] = 'P', '.'
            elif mx[i][j] == 0 and mx[j][i] == 1:
                mx[j][i], mx[i][j] = 'P', '.'
            elif mx[i][j] == 0 and mx[j][i] == 0:
                mx[i][j], mx[j][i] = 'N', 'N'
    for row in mx:
        print(" ".join(map(str, row)))
    return mx


def k_1_opt(mx_3_parts, dim):  # I or P or N
    # mx_origin = copy.deepcopy(mx)
    for i in range(dim):
        for j in range(dim):
            if mx_3_parts[i][j] == 'I' or mx_3_parts[i][j] == 'P' or mx_3_parts[i][j] == 'N':
                mx_3_parts[i][j] = 1
    for row in mx_3_parts:
        print(" ".join(map(str, row)))
    search_k_max(lower_section_mx(mx_3_parts, dim), dim)


def k_2_opt(mx_3_parts, dim):  # P or N
    for i in range(dim):
        for j in range(dim):
            if mx_3_parts[i][j] == 'P' or mx_3_parts[i][j] == 'N':
                mx_3_parts[i][j] = 1
            elif mx_3_parts[i][j] == 'I':
                mx_3_parts[i][j] = '.'
    for row in mx_3_parts:
        print(" ".join(map(str, row)))
    search_k_max(lower_section_mx(mx_3_parts, dim), dim)


def k_3_opt(mx_3_parts, dim):  # P or I
    for i in range(dim):
        for j in range(dim):
            if mx_3_parts[i][j] == 'P' or mx_3_parts[i][j] == 'I':
                mx_3_parts[i][j] = 1
            elif mx_3_parts[i][j] == 'N':
                mx_3_parts[i][j] = '.'
    for row in mx_3_parts:
        print(" ".join(map(str, row)))
    search_k_max(lower_section_mx(mx_3_parts, dim), dim)


def k_4_opt(mx_3_parts, dim):  # P
    for i in range(dim):
        for j in range(dim):
            if mx_3_parts[i][j] == 'P':
                mx_3_parts[i][j] = 1
            elif mx_3_parts[i][j] == 'N' or mx_3_parts[i][j] == 'I':
                mx_3_parts[i][j] = '.'
    for row in mx_3_parts:
        print(" ".join(map(str, row)))
    search_k_max(lower_section_mx(mx_3_parts, dim), dim)


def lower_section_mx(mx, dim):
    r_lower = {}
    for i in range(dim):
        r_lower[i+1] = []
        for j in range(dim):
            if mx[i][j] == 1:
                r_lower[i+1].append(j+1)
    return r_lower


def search_k_max(lower_mx, dim):
    max_count = 0  # знаходження найбільшої кількості елементів у перерізу
    for key, value in lower_mx.items():
        if len(value) > max_count:
            max_count = len(value)
    rows = []  # рядки з найбільшою кількістю елементів
    for key, value in lower_mx.items():
        if len(value) == max_count:
            rows.append(key)
    print(f'Рядки з найбільшою кількістю елементів: {rows}')
    k_max = []
    for el in rows:
        el_count = 0  # для перевірки чи всі рядки входять в поточний рядок, максимальний за включенням
        for key, value in lower_mx.items():
            if set(value) <= set(lower_mx[el]):
                el_count += 1
        if el_count == dim:
            k_max.append(el)
    print(f'K-max: {k_max}')


def k_opt_output(mx, dim):
    three_parts_matrix = make_3_parts_matrix(mx, dim)
    mx_origin = copy.deepcopy(three_parts_matrix)
    print('K-1')
    k_1_opt(mx_origin, dim)
    print('K-2')
    mx_origin = copy.deepcopy(three_parts_matrix)
    k_2_opt(mx_origin, dim)
    print('K-3')
    mx_origin = copy.deepcopy(three_parts_matrix)
    k_3_opt(mx_origin, dim)
    print('K-4')
    mx_origin = copy.deepcopy(three_parts_matrix)
    k_4_opt(mx_origin, dim)