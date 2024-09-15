n = int(input('input number (3 - 20): '))
result = []
for i in range(1, 21):
    for j in range(1, 21):
        a = [i, j]
        if n % (i + j) != 0 or a[::-1] in result or i == j:
            continue
        else:
            result.append(a)
result_1 = []
for i in result:
    result_1.extend(i)
print(*result_1)
