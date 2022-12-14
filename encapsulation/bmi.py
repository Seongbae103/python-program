'''
키와 몸무게를 입력받아서 비만도를 측정하는 프로그램을 완성하시오.
BMI 지수를 구하는 공식은 다음과 같다.
BMI지수 = 몸무게(70kg) / (키(1.7m) * 키(1.7m))

BMI 지수에 따른 결과는 다음과 같다.
고도 비만 : 35 이상
중(重)도 비만 (2단계 비만) : 30 - 34.9
경도 비만 (1단계 비만) : 25 - 29.9
과체중 : 23 - 24.9
정상 : 18.5 - 22.9
저체중 : 18.5 미만

이름, 키, 몸무게를 입력받으면 다음과 같이 출력되도록 하시오.

***************************
이름 키(cm) 몸무게(kg) 비만도
***************************
홍길동 170 70 정상
***************************
'''

class Bmi(object):
    def __init__(self,name, h, w):
        self.name = name
        self.h = h
        self.w = w
        self.set_biman()

    def set_bmi(self):
        m = self.h/100
        w = self.w
        return w/(m ** 2)

    def set_biman(self):
        bmi = self.set_bmi()
        if bmi >= 35:
            biman = "고도 비만"
        elif bmi >= 30:
            biman = "중(重)도 비만 (2단계 비만)"
        elif bmi >= 25:
            biman = "경도 비만 (1단계 비만)"
        elif bmi >= 23:
            biman = "과체중"
        elif bmi >= 18.5:
            biman = "정상"
        else:
            biman = "저체중"
        self.biman = biman

    def print_biman(self):
        print(f"{self.name} {self.h} {self.w} {self.biman}")

    @staticmethod
    def print_menu():
        print("1. 등록")
        print("2. 출력")
        print("3. 삭제")
        return int(input("실행 : "))
    @staticmethod
    def new_user():
        return Bmi(input("이름 : "),
                   int(input("키 : ")),
                   int(input("몸무게 : ")))
    @staticmethod
    def print_result(ls):
        print("비만도 계산")
        print("****************************")
        print("이름 키(cm) 몸무게(kg) 비만도")
        print("****************************")
        for i in ls:
            i.print_biman()
        print("****************************")

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Bmi.print_menu()
            if menu == 1:
                print("### 비만도 등록 ###")
                ls.append(Bmi.new_user())
            elif menu == 2:
                print("### 비만도 출력 ###")
                print(Bmi.print_result(ls))
            else:
                print("### 비만도 삭제 ###")
                ls.remove(Bmi.new_user(ls))
                break
Bmi.main()
            
