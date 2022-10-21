from randomlist import Randomlist

class OddEven(object):

    def __init__(self) -> None:
        pass

    def print(self):
        rl = Randomlist()
        print(rl.get_random(10, 100, 10))
        print([f"even : {i}" if i % 2 ==0 else f"odd : {i}" for i in rl.get_random(10, 100, 10)])

    @staticmethod
    def main():
        oe = OddEven()
        oe.print()
OddEven.main()        