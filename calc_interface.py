import add



def main():

    kalkulacka = add.Kalkulacka()

    while True:

        operace_str = input("Zadej operaci")


        if operace_str == "+": operace = kalkulacka.secti
        elif operace_str == "-": operace = kalkulacka.odecti
        elif operace_str == "*": operace = kalkulacka.vynasob
        elif operace_str == "/": operace = kalkulacka.divide
        else: continue

        a = float(input("Zadejte A: "))
        b = float(input("Zadejte B: "))

        print(f"Výsledek rovnice ({a} {operace_str} {b}) je: {operace(a,b)}")

        vyber = input("Přeješ si počítat i nadále? [Y/N]")

        if vyber == "Y":
            break
    


if __name__ == "__main__":
    main()
