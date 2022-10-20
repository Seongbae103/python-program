from randomlist import Randomlist

class Bubble:
    def __init__(self) -> None:
        pass
    def print(self):
        rl = Randomlist()
        ls = rl.get_random(10, 100, 10)
        print(ls)
        for i in range(len(ls)-1):
            for j in range(len(ls)-1):
                if ls[j] > ls[j+1]:
                    ls[j], ls[j+1] = ls[j+1], ls[j]
        print("$"*40)
        print(ls)
    @staticmethod
    def main():
        bubble = Bubble()
        bubble.print()
Bubble.main()