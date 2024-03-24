"""
1. Opracować kod korygujący pojedynczy błąd bitowy dla wiadomości ośmiobitowych (1 bajt)
2. Opracować kod korygujący podwójny błąd bitowy dla wiadomości ośmiobitowych (1 bajt)
3. Napisać program przekodowujący dowolny plik do postaci zakodowanej jednym z
opracowanych kodów (przygotowanie do transmisji) i odkodowywujący do postaci
pierwotnej (odtworzenie danych po transmisji) z korekcją powstałych błędów. Dla
ułatwienia zadania można kodować dane z upakowaniem na granicy 1 bajtu, czyli słowa o
długości od 9 do 16 bitów jako 2 bajty, 17-24 bity jako 3 bajty itd. Operacje
kodowania/odkodowania powinny być uruchamiane niezależnie od siebie, tak by można
było poprzez ręczną modyfikację pliku zasymulować powstanie błędów transmisji.
"""
from funkcja1 import funkcja1
from funkcja2 import funkcja2


def main():
    print("Wybierz, który program chcesz uruchomić: ")
    print("1. Program korygujący pojedyńczy błąd bitowy dla wiadomości ośmiobitowych.")
    print("2. Program korygujący podwójny błąd bitowy dla wiadomości ośmiobitowych.")
    print(
        "3. Program przekodowujący dowolny plik do postaci zakodowanej i odkodowujący do postaci pierwotnej z korekcją powstałych błędów.")
    print("Twój wybór: ")

    choice1 = input()

    if choice1 == '1':
        print("Tu kiedyś będzie działający program xD")
    elif choice1 == '2':
        print("Tu kiedyś będzie działający program xD")
    elif choice1 == '3':
        print("Wybierz, czy chcesz zakodować czy odkodować plik.")
        print("a) zakodować")
        print("b) zakodować")
        print("Twój wybór: ")

        choice2 = input()

        if choice2 == 'a':
            print("Tu kiedyś będzie działający program xD")
        elif choice2 == 'b':
            print("Tu kiedyś będzie działający program xD")
        else:
            print("Nieprawidłowy wybór")
            exit()

    else:
        print("Nieprawidłowy wybór")
        exit()


'''
    wynik1 = funkcja1(5)
    wynik2 = funkcja2(3)

    print("Wynik funkcji 1:", wynik1)
    print("Wynik funkcji 2:", wynik2)
'''

if __name__ == "__main__":
    main()

