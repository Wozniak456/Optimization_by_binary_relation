def s_search(u_section, dim):
    s0 = {key for key, value in u_section.items() if not value}
    elements = 0
    step = 0
    s = {0: s0}
    s_unique = {0: s0}
    elements += len(s0)

    while elements < dim:
        s_i = set()
        for key, value in u_section.items():
            is_subset = set(value).issubset(s[step])
            if is_subset:
                s_i.add(key)
        step += 1
        s[step] = s_i
        s_unique[step] = s[step] - s[step-1]
        s_i = s[step]-s[step-1]
        elements += len(s_i)
    return s_unique


def q_search(u_section, dim):
    s_unique = s_search(u_section, dim)
    print(f's: {s_unique}')
    q = {0: s_unique[0]}
    step = 1
    for key, value in s_unique.items():
        for element in value:
            if not set(u_section[element]).intersection(q[step-1]):
                q[step] = set(q[step-1])
                q[step].add(element)
                step += 1
    print(f'q: {q}')
    print(f'The result: {q[step-1]}')




