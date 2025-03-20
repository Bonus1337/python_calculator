
def add_number(a, b):
	return a + b
def sub_number(a, b):
	return a - b
def mul_number(a, b):
	return a * b
def div_number(a, b):
	return a / b

if __name__ == "__main__":
    print("Kalkulator")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    choice = input("Wybierz działanie: ")
    a = float(input("Podaj pierwszą liczbę: "))
    b = float(input("Podaj drugą liczbę: "))
    if choice == "1":
        print(add_number(a, b))
    elif choice == "2":
        print(sub_number(a, b))
    elif choice == "3":
        print(mul_number(a, b))
    elif choice == "4":
        print(div_number(a, b))
    else:
        print("Nieprawidłowy wybór")
