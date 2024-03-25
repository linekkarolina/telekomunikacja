H = [[1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
     [1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0],
     [0, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1]]

def txt_to_int(text):
    return [int(char) for char in text]

def get_c(msg, r):
    return sum(H[r][j] * msg[j] for j in range(len(msg))) % 2

def encoding(msg):
    if not msg:
        return []
    encoded_msg = msg[:]
    for r in range(len(H)):
        C = get_c(msg, r)
        encoded_msg.append(C)
    return encoded_msg

def flip_bit(bit):
    return 1 if bit == 0 else 0

def correct(msg, error):
    for k in range(len(H[0])):
        error_check = True
        for r in range(len(H)):
            if error[r] != H[r][k]:
                error_check = False
                break
        if error_check:
            msg[k] = flip_bit(msg[k])
            break

def check(msg):
    if len(msg) != len(H[0]):
        print("Liczba bitów nie jest równa")
        return

    errors = [get_c(msg, i) for i in range(len(H))]
    if any(error != 0 for error in errors):
        correct(msg, errors)

def main():
    print("Wybierz 1 aby zakodować, wybierz 2 żeby zdekodować.")
    wybor = int(input())
    if wybor == 1:
        # kodowanie
        with open("wiadomosc.txt", "r") as wejscie, open("zakodowane.txt", "w") as wyjscie:
            for line in wejscie:
                if len(line.strip()) == 8:
                    wiadomosc = txt_to_int(line.strip())
                    wiadomosc_encoded = encoding(wiadomosc)
                    wyjscie.write(''.join(map(str, wiadomosc_encoded)) + '\n')
    elif wybor == 2:
        # dekodowanie
        with open("zakodowane.txt", "r") as wejscie, open("wiadomosc.txt", "w") as wyjscie:
            for line in wejscie:
                if len(line.strip()) == 12:
                    wiadomosc = txt_to_int(line.strip())
                    check(wiadomosc)
                    wyjscie.write(''.join(map(str, wiadomosc[:8])) + '\n')
    else:
        print("Nie wybrałeś 1 ani 2")

if __name__ == "__main__":
    main()
