H = [[1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
     [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
     [1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
     [1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1]]

def encode(message):
    for i in range(9):
        checksum = 0
        for j in range(8):
            checksum ^= H[i][j] & message[j]
        message[i+8] = checksum

def get_error(message):
    error = [0] * 9
    for i in range(9):
        e = 0
        for j in range(17):
            e ^= H[i][j] & message[j]
        error[i] = e
    return error

def correct_error(message, error):
    # pojedyncza kolumna
    for i in range(17):
        for j in range(9):
            if H[j][i] != error[j]:
                break
            if j == 8:
                # zmień i-ty bit
                message[i] ^= 1
                return
    # suma kolumn
    for i in range(17):
        for j in range(i, 17):
            for k in range(9):
                if (H[k][i] ^ H[k][j]) != error[k]:
                    break
                if k == 8:
                    # zmień i-ty i j-ty bit
                    message[i] ^= 1
                    message[j] ^= 1
                    return

if __name__ == "__main__":
    message = [0] * 17

    print("Podaj 8-bitow widomosci")
    user_input = input().strip()[:8]
    for i in range(8):
        message[i] = int(user_input[i])

    encode(message)
    print("Zakodowana wiadomosc")
    print(''.join(map(str, message)))

    print("Podaj >zepsuta< wiadomosc")
    user_input = input().strip()[:17]
    for i in range(17):
        message[i] = int(user_input[i])

    error = get_error(message)
    print("Wektor bledu")
    print(''.join(map(str, error)))

    correct_error(message, error)
    print("Poprawiona wiadomosc")
    print(''.join(map(str, message)))
