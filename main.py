from constants import Elements


def get_number(index: int, formula: str) -> int:
    number = ''
    for i in range(len(formula[index:])):
        if formula[index+i].isdigit():
            number += formula[index+i]
        else:
            break
    return int(number) if number.isdigit() else 1


def calculate_molar_mass(formula: str) -> float:

    last_index: int = len(formula) - 1
    mass: float = 0
    isinside: bool = False
    inside_formula: str = ''

    for index, symbol in enumerate(formula):
        if isinside and symbol not in {'(', ')'}:
            inside_formula += symbol
            continue
        elif symbol == '(':
            isinside = True
            continue
        elif symbol == ')':
            isinside = False
            count = get_number(index + 1, formula)
            mass += count * calculate_molar_mass(inside_formula)
            inside_formula = ''
            continue

        if not symbol.isupper():
            continue

        if index != last_index:
            bad_element = Elements.get(symbol + formula[index+1 : index+2], False)
        else:
            mass += Elements[symbol]
            continue

        step: int = 2 if bad_element else 1
        count_elements = get_number(index + step, formula)

        element_mass = bad_element if bad_element else Elements[symbol]

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
