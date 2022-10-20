import random

class Randomlist(object):

    def __init__(self) -> None:
        pass

    def get_random(self, start, end, count):
        return random.sample(range(start, end), k=count) 

    def print(self):
        print(self.get_random(1, 100, 10))
'''
    @staticmethod
    def main():
        rl = Randomlist()
        .print()
OddEven.main()   '''
if __name__=="__main__":
    rl = Randomlist()
    rl.print()
     