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
from unicodedata import category
from unittest import result


class Bmi(object):
    def __init__(self,name, h, w):
        self.name = name
        self.h = h
        self.w = w
        self.biman = ""

    def execute(self):
        self.biman = self.get_biman()
        self.get_biman()
        self.print_biman()

    def get_bmi(self):
        m = self.h/100
        w = self.w
        return w/m ** 2

    def get_biman(self):
        biman = ""
        bmi = self.get_bmi()
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
        name = self.name
        h = self.h
        w = self.w
        title = "### 비만도 계산 ###"
        tag = "이름 키(cm) 몸무게(kg) 비만도"
        biman = self.biman
        ast = "*"*30
        result = f"{name} {h} {w} {biman}"
        print(f'{title} \n {ast} \n {tag} \n {ast} \n {result} \n {ast}')

    @staticmethod
    def main():
        name = input("이름 : ")
        h = int(input("키(cm) : "))
        w = int(input("체중(kg) : "))
        bmi = Bmi(name, h, w)
        bmi.execute()
Bmi.main()
            
