from constants import Elements


def calculate_molar_mass(formula: str) -> float:
    
    last_index: int = len(formula) - 1
    mass: float = 0

    for index, symbol in enumerate(formula):
        if not symbol.isupper():
            continue

        if index != last_index:
            bad_element = Elements.get(symbol + formula[index+1 : index+2], False)
        else:
            mass += Elements[symbol]
            continue

        step: int = 2 if bad_element else 1
        number: str = ''
        for i in range(step, len(formula[index:])):
            if formula[index+i].isdigit():
                number += formula[index+i]
            else:
                break

        element_mass = bad_element if bad_element else Elements[symbol]
        count_elements = float(number) if number.isdigit() else 1
        mass += element_mass * count_elements

    return mass


def main() -> int:
    print("\033[31mNote: Element symbols are case-sensitive "
          "(e.g., C, O, Co).\033[0m\n" + "—" * 27)

    formula = input("Enter the molecular formula: ")
    print(calculate_molar_mass(formula))
    return 0


if __name__ == "__main__":
    main()
