H = [[1,1,1,0,1,1,1,0, 1,0,0,0],
     [1,1,0,1,1,0,0,1, 0,1,0,0],
     [1,0,1,1,0,1,0,0, 0,0,1,0],
     [0,1,1,1,0,0,1,1, 0,0,0,1]]

def parse(s):
    return [int(ch) for ch in s]

def count_cbit(message, row):
    return sum(message[i] * H[row][i] for i in range(len(message))) % 2

def flip(bit):
    return 1 - bit

def correct(message, error):
    for column in range(len(message)):
        err_check = all(error[row] == H[row][column] for row in range(len(H)))
        if err_check:
            message[column] = flip(message[column])
            break

def check_message(message):
    if len(message) != len(H[0]):
        print("WRONG")
        return

    verification = True
    err = []

    for i in range(len(H)):
        row_sum = count_cbit(message, i)
        err.append(row_sum)
        if row_sum == 1:
            verification = False

    if not verification:
        correct(message, err)

def encode(message):
    if not message:
        return
    for row in range(len(H)):
        cbit = count_cbit(message, row)
        message.append(cbit)

if __name__ == "__main__":
    message_text = input("Podaj wiadomość:\n")
    message = parse(message_text)

    encode(message)

    print("\nZakodowana wiadomość:")
    print("".join(map(str, message)))

    message_text = input("\nPodaj błędną wiadomość:\n")
    wrong_message = parse(message_text)

    check_message(wrong_message)

    print("\nPoprawiona wiadomość:")
    print("".join(map(str, wrong_message)))
