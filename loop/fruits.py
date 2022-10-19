"""
과일 판매상에서 메뉴를 진열하는 어플을 제작하고자 한다.
입력되는 값은 없다.
출력되는 결과는 다음과 같다.
### 과일번호표 ###
*******************************  *
 1번과일 : 바나나
 2번과일 : 사과
 3번과일 : 망고
********************************
구매할 과일: 바
"""
class Fruits:
    def __init__(self,purchase) -> None:
        self.menu = ["바나나", "사과", "망고"]
        self.purchase = purchase
    def menu(self):
        print("### 과일번호표 ###")
        print("********************************")
        j = 0
        for i in self.menu:
           print(f"(j+1)번과일: {i}")
           j += 1
        print("********************************")
        fw = self.purchase[:2] #구매할 과일 첫글자

    @staticmethod
    def main():
        purchase = input("구매할 과일 : ")
        fruits = Fruits(purchase)
        fruits.menu()
Fruits.main()