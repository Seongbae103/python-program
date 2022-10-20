'''
###성적표###
********************************
이름 국어 영어 수학 총점 평균 학점
********************************
홍길동 90 90 92 272 90.6 A
이순신 90 90 92 272 90.6 A
유관순 90 90 92 272 90.6 A
********************************
'''

class Grade(object):
    def __init__(self, name, ko, en, ma) -> None:
        self.name = name
        self.ko = ko
        self.en = en
        self.ma = ma
        self.set_total()
        self.set_avg()
        self.set_grade()

    def set_total(self):
        self.total = self.ko + self.en + self.ma

    def set_avg(self):
        self.avg = self.total /3

    def set_grade(self):
        avg = self.avg
        if avg >= 90:
            self.grade = "A"
        elif avg >= 80:
            self.grade = "B"
        elif avg >= 70:
            self.grade = "C"
        elif avg >= 60:
            self.grade = "D"
        elif avg >= 50:
            self.grade = "E"
        else:
            self.grade = "F"
        grade = self.grade
        return grade

    def print_grade(self):
        print("{self.name} {self.ko} {self.en} {self.ma} {self.total} {self.avg} {self.grade}")

    @staticmethod
    def new_grade():
        return Grade(input("이름 : "), 
                    int(input("국어 : ")),
                    int(input("영어 : ")),
                    int(input("수학 : ")))

    @staticmethod
    def print_table(ls):
            print("###성적표###" 
            "\n ********************************"
            "\n 이름 국어 영어 수학 총점 평균 학점"
            "\n ********************************")
            for i in ls:
                i.print_grade()
            print("********************************")

    @staticmethod
    def print_menu():
        print("1. 성적등록")
        print("2. 성적출력")
        print("3. 성적삭제")
        print("4. 종료")
        return print("메뉴선택")

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Grade.print_menu()
            if menu == 1:
                print("### 성적등록 ###")
                ls.append(Grade.new_grade())
            elif menu == 2:
                print("### 성적출력 ###")
                Grade.print_grade(ls)
            elif menu == 3:
                print("### 성적삭제 ###")
            elif menu == 4:
                print("###종료###")
                break
            grade = Grade("", 0, 0, 0)
            grade.print_table()
Grade.main()