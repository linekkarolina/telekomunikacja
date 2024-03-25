H_ROWS = 4
H_COLUMNS = 12

H = [[1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
     [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]]

def parse(s):
    return [int(ch) for ch in s]

def count_cbit(message, row):
    return sum(message[i] * H[row][i] for i in range(len(message))) % 2

def flip(bit):
    return 1 if bit == 0 else 0

def correct(message, error):
    for column in range(H_COLUMNS):
        err_check = all(error[row] == H[row][column] for row in range(H_ROWS))
        if err_check:
            message[column] = flip(message[column])
            break

def check_message(message):
    if len(message) != H_COLUMNS:
        print("WRONG")
        return

    verification = True
    err = []

    for i in range(H_ROWS):
        row_sum = count_cbit(message, i)
        err.append(row_sum)
        if row_sum == 1:
            verification = False

    if not verification:
        correct(message, err)

def encode(message):
    for row in range(H_ROWS):
        cbit = count_cbit(message, row)
        message.append(cbit)

def decode(message):
    check_message(message)
    for i in range(H_ROWS):
        message.pop()

def main():
    wybor = int(input("Kodowanie: 1\nDekodowanie: 2\n"))

    if wybor == '1':
        with open("wiad.txt", "r") as input_file, open("zakodowane.txt", "w") as encoded_file:
            message_text = ""
            counter = 0

            for line in input_file:
                for ch in line.strip():
                    message_text += ch
                    counter += 1

                    if counter == 8:
                        message = parse(message_text)
                        encode(message)
                        encoded_file.write("".join(map(str, message)) + "\n")
                        message_text = ""
                        counter = 0

            if counter != 0:
                message_text += "0" * (8 - counter)
                message = parse(message_text)
                encode(message)
                encoded_file.write("".join(map(str, message)) + "\n")

    elif wybor == '2':
        with open("zakodowane.txt", "r") as encoded_file, open("wiad1.txt", "w") as decoded_file:
            message_text = ""
            counter = 0

            for line in encoded_file:
                for ch in line.strip():
                    message_text += ch
                    counter += 1

                    if counter == 12:
                        message = parse(message_text)
                        decode(message)
                        decoded_file.write("".join(map(str, message)) + "\n")
                        message_text = ""
                        counter = 0

main()
