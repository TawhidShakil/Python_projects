import sys
import os
def clear_screen():
     os.system('cls')
from Person import Person
class Teacher(Person):
    def __init__ (self, name:str, id:str, email:str, phone:str, BG:str, department:str, salary:float)->None:
        self.department = department
        self.salary = salary
        super().__init__(name, id, email, phone, BG)
    def __repr__(self) ->str:
        info = '========= Information for the Teacher ===========\n'
        info += f'Name: {self.name}\n'
        info += f'ID: {self.id}\n'
        info += f'E-mail: {self.email}\n'
        info += f'Phone: {self.phone}\n'
        info += f'Blood Group: {self.BG}\n'
        info += f'Department: {self.department}\n'
        info += f'Salary {self.salary}\n'
        return info
    def display_teacher_info(self):
         print(self)

    # Update Methods
    #1. Name change Method
    def changeName(self, newName:str):
         self.name = newName
    #2. E-mail change method
    def changeEmail(self, newEmail:str):
         self.email = newEmail
    #3. Phone Number change Method
    def changePhone(self, newPhone:str):
         self.phone = newPhone
    # End the Update Methods

t1 = None
while True:
    print('========== MENU ==========')
    print('1. Add Teacher')
    print('2. Display')
    print('3. Update Info')
    print('4. Delete')
    print('5. Exit')
    print('===========================')
    option = int(input('Enter your MENU: '))
    clear_screen()
    if option == 1:
            name = str(input('Enter name: '))
            id = str(input('Enter ID: '))
            email = str(input('Enter E-mail: '))
            phone = str(input('Enter Phone: '))
            BG = str(input('Enter Blood group: '))
            department = str(input('Enter Department: '))
            salary = float(input('Enter Salary: '))

            # create an object
            t1 = Teacher(name, id, email, phone, BG, department, salary)
            clear_screen()
            print('You have successfully added !!') 
    elif option == 2:
            if t1 is not None:
                 t1.display_teacher_info()
                 str(input('Press Enter to continue...'))
                 clear_screen()
            else:
                 print('No records Found')
    elif option == 3:
         print('========== Update Menu =========')
         print('1. Change Name')
         print('2. Change E-mail')
         print('3. Change Phone')
         print('=================================')
         select = int(input('Enter Your Menu: '))
         clear_screen()
         if select == 1:
            newName = str(input('Enter New Name: '))
            t1.changeName(newName)
            clear_screen()
            print('Name Change Successfully !!')
            
         elif select == 2:
              newEmail = str(input('Enter New E-mail: '))
              t1.changeEmail(newEmail)
              clear_screen()
              print('E-mail Change successully !!')
         elif select == 3:
              newPhone = str(input('Enter New Phone: '))
              t1.changePhone(newPhone)
              clear_screen()
              print('Phone Change Successfully !!')
    elif option == 4:
         pass
    elif option == 5:
         break