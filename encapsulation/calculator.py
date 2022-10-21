class Calculator(object):
    def __init__(self, num1, op, num2):
        self.num1 = num1
        self.op = op
        self.num2 = num2

    @staticmethod
    def input_number():
        int(input("1번째 수 : " ))
        input("연산자 : ")
        int(input("2번째 수 : "))

    def print_result(self):
        op = self.op
        num1 = self.num1
        num2 = self.num2
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        elif op == "%":
            result = num1 % num2
        else:
            print("잘못된 연산자")
        print(f"{self.num1} {self.op} {self.num2} = {result}")


    @staticmethod
    def main():
        ls = []
        while True:
            print("결과")
            ls.append(Calculator.input_number())
            print(Calculator.print_result())

Calculator.main()   