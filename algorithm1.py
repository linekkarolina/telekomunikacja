def detectSingleError(arr, matrix_h):
    n = len(arr)
    res = [0] * len(matrix_h)
    for i in range(len(matrix_h)):
        val = 0
        for j in range(n):
            val ^= matrix_h[i][j] * arr[j]
        res[i] = val

    for i in range(len(matrix_h)):
        if res[i] == 1:
            # Korekcja pojedynczego błędu bitowego.
            for j in range(n):
                arr[j] ^= matrix_h[i][j]
            return True
    return False


def detectDoubleError(arr, matrix_h):
    n = len(arr)
    res = [0] * n
    for i in range(len(matrix_h)):
        val = 0
        for j in range(n):
            val ^= matrix_h[i][j] * arr[j]
        res[i] = val

    for i in range(len(matrix_h)):
        for j in range(i + 1, len(matrix_h)):
            is_error = True
            for k in range(n):
                if matrix_h[i][k] != matrix_h[j][k] != res[k]:
                    is_error = False
                    break
            if is_error:
                # Korekcja podwójnego błędu bitowego.
                for k in range(n):
                    arr[k] ^= matrix_h[i][k]
                return True
    return False


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

# Symulacja błędu w transmisji przez zmianę wartości bitu.
# 10101001110 -> 11101001110, błąd na 10. pozycji.
error_data = list(map(int, '11001001110'))
print("Dane z błędem:", ''.join(map(str, error_data)))

# Korekcja podwójnego błędu bitowego
if detectDoubleError(error_data, matrix_h):
    print("Znaleziono i skorygowano podwójny błąd bitowy.")
else:
    # Korekcja pojedynczego błędu bitowego
    if detectSingleError(error_data, matrix_h):
        print("Znaleziono i skorygowano pojedynczy błąd bitowy.")
    else:
        print("Nie udało się skorygować błędów.")
