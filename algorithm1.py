def calcRedundantBits(m):
    r = 0
    while 2 ** r < m + r + 1:
        r += 1
    return r

def calcParityBits(arr, r, matrix_h):
    for i in range(r):
        val = 0
        for j in range(len(arr)):
            if j & (2 ** i) == (2 ** i):
                val ^= int(arr[j])
        arr.append(val)

def detectError(arr, matrix_h):
    n = len(arr)
    res = 0
    for i in range(len(matrix_h)):
        val = 0
        for j in range(n):
            val ^= matrix_h[i][j] * arr[j]
        res += val * (10 ** i)
    return int(str(res), 2)

# Zadeklarowana macierz kontrolna
matrix_h = [
    [1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0],
    [1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0],
    [1, 1, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1]
]

# Dane do transmisji
data = '1011001'

# Obliczenie liczby nadmiarowych bitów
m = len(data)
r = calcRedundantBits(m)

# Określenie bitów parzystości
calcParityBits(list(map(int, data)), r, matrix_h)

# Dane do transmisji
print("Dane do transmisji:", ''.join(map(str, data)))

# Symulacja błędu w transmisji przez zmianę wartości bitu.
# 10101001110 -> 11101001110, błąd na 10. pozycji.
data = list(map(int, '11101001110'))
print("Dane z błędem:", ''.join(map(str, data)))
correction = detectError(data, matrix_h)
if correction == 0:
    print("Brak błędu w przesłanej wiadomości.")
else:
    print("Pozycja błędu:", len(data) - correction + 1, "od lewej")