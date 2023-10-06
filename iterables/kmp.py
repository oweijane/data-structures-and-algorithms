def lps(pattern):
    M = len(pattern)
    res = [0] * M
    for i in range(1, M):
        j = res[i - 1]
        while j and pattern[i] != pattern[j]:
            j = res[j - 1]
        if pattern[i] == pattern[j]:
            res[i] = j + 1
    return res


def kmp(string, pattern):
    N, M = len(string), len(pattern)
    if N < M:
        return False
    lps_array = lps(pattern)
    res = []
    j = 0
    for i, c in enumerate(string):
        while j and (j == M or pattern[j] != c):
            j = lps_array[j - 1]
        if pattern[j] == c:
            j += 1
            if j == M:
                res.append(i - M + 1)
    return res

if __name__ == '__main__':
    string = 'abaabaa'
    pattern = 'abaa'
    print(kmp(string, pattern))
