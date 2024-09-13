def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

for i in range(3):
    if i == 0:
        n = 2
        m = 2
        value = 10
        a = get_matrix(n, m, value)
        print(a)
    elif i == 1:
        n = 3
        m = 5
        value = 42
        a = get_matrix(n, m, value)
        print(a)
    else: #if i == 2:
        n = 4
        m = 2
        value = 13
        a = get_matrix(n, m, value)
        print(a)