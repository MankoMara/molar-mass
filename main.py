class Elements:
    H = 1
    He = 2
    Li = 7
    Be = 9
    B = 11
    C = 12
    N = 14
    O = 16
    F = 19
    Ne = 20

def calculate_molar_mass(formula: str) -> int:

    mass: int = 0
    number: str = ''

    for index, symbol in enumerate(formula):

        if Elements.__dict__.get(symbol, False):
            for i in range(1, len(formula[index:])):
                if formula[index+i].isdigit():
                    number += formula[index+i]
                else:
                    break

            if number.isdigit():
                mass += Elements.__dict__[symbol] * int(number)
            else:
                mass += Elements.__dict__[symbol]
            number = ''

    return mass


def main() -> int:
    formula = input("Enter the molecular formula: ").upper()
    print(calculate_molar_mass(formula))
    return 0


if __name__ == "__main__":
    main()
