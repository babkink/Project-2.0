numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in numbers:
    if i == 1:
        continue
    not_pr = False
    for j in numbers:
        if j > i - 1: break
        if i % j == 0 and j != 1:
           not_pr = True
    if not_pr:
        not_primes.append(i)
    else:
        primes.append(i)

print('Primes: ', primes)
print('Not Primes: ', not_primes)



