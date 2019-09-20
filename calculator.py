class OperationNotValid(Exception):
    pass


# function for printing information
def print_operations():
    print("The following operations are available:\n"
          "1. Addition (+)\n"
          "2. Subtraction (-)\n"
          "3. Division (/)\n"
          "4. Multiplication (*)\n"
          "5. Exponentiation (^)\n")


# function handling the input
def select_operation():
    # infinite loop until the input is valid
    while True:
        try:

            choice = input('Operation: ')
            choice_ = [char for char in choice.split()]
            if choice_[1] not in ['+', '-', '/', '*', '^']:
                raise OperationNotValid
            else:
                # return a list, ex: ['2, '+', '1']
                return choice_

        except OperationNotValid:
            print('\nThe operation is not valid.'
                  'Enter an operation similar to the following example:'
                  ' 25 * 4\n'
                  '(make sure to enter a whitespace between each char)\n')
        except IndexError:
            print('Try again.\nMake sure to insert a whitespace between each '
                  'character (ex.: 25 * 4)\n')


class Calculator:
    def __init__(self):
        op_ = select_operation()
        self.num1 = op_[0]
        self.symbol = op_[1]
        self.num2 = op_[2]

    # function handling addition
    def add(self):
        return float(self.num1) + float(self.num2)

    # function handling subtraction
    def sub(self):
        return float(self.num1) - float(self.num2)

    # function handling division
    def div(self):
        return float(self.num1) / float(self.num2)

    # function handling multiplication
    def multipl(self):
        return float(self.num1) * float(self.num2)

    # function handling Exponentiation
    def exp(self):
        return float(self.num1) ** float(self.num2)

    def calc(self):
        if self.symbol == '+':
            result = Calculator.add(self)
            print(self.num1, self.symbol, self.num2, '=', result)
        elif self.symbol == '-':
            result = Calculator.sub(self)
            print(self.num1, self.symbol, self.num2, '=', result)
        elif self.symbol == '/':
            result = Calculator.div(self)
            print(self.num1, self.symbol, self.num2, '=', result)
        elif self.symbol == '*':
            result = Calculator.multipl(self)
            print(self.num1, self.symbol, self.num2, '=', result)
        elif self.symbol == '^':
            result = Calculator.exp(self)
            print(self.num1, self.symbol, self.num2, '=', result)


def main():
    print_operations()
    Calculator().calc()
    input()


if __name__ == '__main__':
    main()

