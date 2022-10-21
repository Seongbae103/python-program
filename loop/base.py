class Base(object):
    def __init__(self):
        pass
    def print(self):
        pass
    @staticmethod
    def print_menu():
        pass

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Base.print_menu()
            if menu == 1:
                print("목록1")
                Base.base1()
            elif menu == 2:
                print("목록2")
                Base.base2()
            elif menu == 3:
                print("목록3")
                Base.base3()
            elif menu == 0:
                print("종료")
            else: print("다시 입력")

MemoryError.main()