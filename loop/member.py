'''아이디, 비밀번호, 이름을 받아서
회원가입, 목록, 탈퇴하는 프로그램을 개발
'''
class Member(object):
    def __init__(self, id, pw, name):
        self.id = id
        self.pw = pw
        self.name = name
    def print_result(self):
        print(f"{self.id} {self.pw} {self.name}")

    @staticmethod
    def print_menu():
        print("1. 회원가입")
        print("2. 목록")
        print("3. 삭제")
        return int(input("실행 : "))

    @staticmethod
    def new_user():
        return Member(input("아이디 : "),
                      int(input("비밀번호 : ")),
                      input("이름 : "))

    @staticmethod
    def user_list(ls):
        print("###목록###")
        print("*********************")
        print("아이디 비밀번호 이름")
        print("*********************")
        for i in ls:
            i.print_result()
        print("*********************")

    @staticmethod
    def main():
        ls = []
        while True:
            menu = Member.print_menu()
            if menu == 1:
                print("### 회원가입 ###")
                ls.append(Member.new_user())
            elif menu == 2:
                print("### 목록 ###")
                print(Member.user_list(ls))
            elif menu == 3:
                print("### 삭제 ###")
            else: print("잘못된 입력입니다.")
Member.main()
