from constants import Elements

def calculate_molar_mass(formula: str) -> float:

    mass: float = 0
    number: str = ''

    for index, symbol in enumerate(formula):
        if symbol.isalpha():
            if symbol != formula[-1]:
                badElement = Elements.get(symbol + formula[index+1 : index+2].lower(), False)
            else:
                mass += Elements[symbol]
                continue

            step: int = 2 if badElement else 1

            for i in range(step, len(formula[index:])):
                if formula[index+i].isdigit():
                    number += formula[index+i]
                else:
                    break

            if number.isdigit() and badElement:
                mass += badElement * float(number)
            elif badElement:
                mass += badElement
            elif number.isdigit() and not badElement:
                mass += Elements[symbol] * float(number)
            else:
                mass += Elements[symbol]
 
            number = ''
            

    return mass


def main() -> int:
    formula = input("Enter the molecular formula: ").upper()
    print(calculate_molar_mass(formula))
    return 0


if __name__ == "__main__":
    main()
