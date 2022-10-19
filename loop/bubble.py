import random

from numpy import extract
class Bubble(object):
    def __init__(self) -> None:
        pass

    def extract(self):
        return random.sample(range(1,100), 50)

    def sort(self):
        for i in range(extract()):
            for j in range(extract()):

    def set(self):
        if self.extract() % 2 == 0:
            return self.extract()
        else:                            # 해결x 
            return self.extract()

    def print_bubble(self):
        for i in self.extract():
            print(f'{i}')

    @staticmethod
    def main():
        bubble = Bubble()
        bubble.print_bubble()
Bubble.main()        