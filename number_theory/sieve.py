def sieve(N):
    res = [True] * (N + 1)
    res[0] = res[1] = False
    i = 2
    while i * i <= N:
        if res[i]:
            for j in range(i * i, N + 1, i):
                res[j] = False
        i += 1
    return res
