'''
랜덤숫자 10개를 뽑아서
사용자가 검색하는 숫자의 배수만 출력하는
프로그램을 개발해주세요
예) [12, 23,48,....]
사용자의 input값이 12인 경우
출력값이 12,48만 되도록 한다.
'''
from randomlist import Randomlist
class Searchnumber(object):
    def __init__(self, num) -> None:
        self.num = num

    def print(self):
        rl = Randomlist().get_random(10,100,10)
        print(rl)
        for i in rl:
            if i % self.num == 0:
                print(f"{i}")

    @staticmethod
    def main():
        num = int(input("input : "))
        searchnumber = Searchnumber(num)
        searchnumber.print()
Searchnumber.main()