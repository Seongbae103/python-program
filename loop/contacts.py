'''
이름, 전화번호, 이메일, 주소를 받아서
연락처 입력, 출력, 삭제하는 프로그램을 개발하시오
'''
class Contact(object):
    def __init__(self, name, phone_num, e_mail, add) -> None:
        self.name = name
        self.phone_num = phone_num
        self.e_mail = e_mail 
        self.add = add

    def print(self):
        print(f"이름 : {self.name} \n 연락처 : {self.phone_num} \n 이메일 : {self.e_mail} \n 주소 : {self.add}")    
    
    @staticmethod
    def new_contact():
        name = input("이름 : ")
        phone_num = input("전화번호 : ")
        e_mail = input("이메일 : ")
        add = input("주소 : ")
        return Contact(name, phone_num, e_mail, add)

    def print_info(self):
        print(f"{self.name}")
        print(f"{self.phone_num}")
        print(f"{self.e_mail}") 
        print(f"{self.add}")

    @staticmethod
    def get_contacts(ls):
        for i in ls:
            i.print_info()
    
    @staticmethod
    def print_menu():
        print("1. 연락처 등록")
        print("2. 연락처 출력")
        print("3. 연락처 삭제")
        print("4. 종료")
        menu = input("메뉴 선택 : ")
        return int(menu)

    @staticmethod
    def main():
        ls = []
        while True:      
            menu = Contact.print_menu()
            if menu == 1:
                print(" ### 연락처 등록 ### ")
                contact = Contact.new_contact()
                ls.append(contact)
            elif menu == 2:
                print(" ### 연락처 출력 ### ")
                Contact.get_contacts(ls)
            elif menu == 3:
                print(" ### 연락처 삭제 ### ")
            elif menu == 4:
                print(" 주소록 어플을 종료합니다. ")
                break
Contact.main()