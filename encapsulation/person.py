"""
이름, 주민번호 (950101-1), 주소를 입력받아서
회원명부를 관리하는 어플을 제작하고자 한다.
출력되는 결과는 다음과 같다.
### 자기소개서 ###
*******************************  *
이름 :
성별 :
나이 :
주소 : 
********************************
"""
from audioop import add


class Person:
    def __inti__(self,name, ssn, add):
        self.name = name
        self.ssn = ssn
        self.add = add
        self.age = 0
        self.gender = ""
        self.add = add

    def gender_checker(self):
        year = int(self.ssn[:2]) # 0:2는 출생년도 판별 인덱스
        gender_checker = int(self.ssn[7]) #7은 성별판별 인덱스
        if gender_checker == 1 or gender_checker == 2:
            self.birth = year + 1900
            if gender_checker == 1:
                self.gender = "남성"
            elif gender_checker == 2:
                self.gender = "여성"
        elif gender_checker == 3 or gender_checker == 4:
            self.birth = year + 2000
            if gender_checker == 3:
                self.gender = "남성"
            elif gender_checker == 4:
                self.gender = "여성"
        else:
            self.gender = "잘못된 생년월일"

    def set_age(self):
        current = 2022
        self.age = current - self.birth + 1
    
    def print_person(self):
        print( f"### 자기소개서 ###"
            "\n ********************************"
            f"\n 이름 : {self.name}"
            f"\n 성별 : {self.gender}"
            f"\n 나이 : {self.age}"
            f"\n 주소 : {self.add}" 
            |"\n ********************************")

    @staticmethod
    def main():
        name = input("이름 : ")
        ssn = input("주민번호 : ")
        add = input(" 주소 : ")
        person = Person(name, ssn, add)
        person.gender_checker()
        person.set_age()
        person.print_person()     
Person.main()

     

      

