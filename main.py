from matrix import Matrix
from typing import Union


def print_matrix(matrix: Matrix) -> None:
    matrix_list = matrix.get_matrix()
    for i in range(matrix.size()[0]):
        print(*matrix_list[i])


def get_operand(input_str: str) -> Union[Matrix, float]:
    try:
        return float(input_str)
    except:
        size = tuple(map(int, input_str.split()))

    matrix_list = []
    for _ in range(size[0]):
        matrix_list.append(list(map(float, input().split())))

    return Matrix(matrix_list)


def main():
    print("SIMPLE MATRIX CALCULATOR\n\n"
          "You need to write data in format:\n<operand>\n<operation>\n<operand>\n"
          "Operand must include size in format '<rows> <columns>' (i.e '3 2')\n"
          "You can type a number instead\n"
          "Supported operations: + | - | * | ^-1 | det | transpose\n"
          "If inverse matrix operation (^-1) is entered, 2nd operand is not required\n"
          "To quit type /q\n")

    while True:
        input_str_1 = input("Number or matrix size > ").strip()

        if input_str_1 == '/q':
            break

        operand_1 = get_operand(input_str_1)
        operation = input("Operation > ").strip()

        if operation in ['^-1', 'det', 'transpose']:
            if operation == '^-1':
                print_matrix(operand_1.inverse())
            elif operation == 'det':
                print_matrix(operand_1.determinant())
            elif operation == 'transpose':
                print_matrix(operand_1.transpose())
            continue

        operand_2 = get_operand(input("Number or matrix size > ").strip())
        print()

        if operation == '+':
            print_matrix(operand_1 + operand_2)
        elif operation == '-':
            print_matrix(operand_1 - operand_2)
        elif operation == '*':
            print_matrix(operand_1 * operand_2)
        else:
            print('Unknown operation')

        print()


if __name__ == '__main__':
    main()
