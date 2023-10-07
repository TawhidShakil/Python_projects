import sys
import os
def clear_screen():
     os.system('cls')
from Person import Person
class Student(Person):
    def __init__(self, name:str, id:str, email:str, phone:str, BG:str, department:str, batch:str, monthlyFee:float)->None:
        self.department = department
        self.batch = batch
        self.monthlyFee = monthlyFee
        super().__init__(name, id, email, phone, BG)
    
    def __repr__(self) ->str:
        info = '========= Information for the Student ===========\n'
        info += f'Name: {self.name}\n'
        info += f'ID: {self.id}\n'
        info += f'E-mail: {self.email}\n'
        info += f'Phone: {self.phone}\n'
        info += f'Blood Group: {self.BG}\n'
        info += f'Department: {self.department}\n'
        info += f'Batch: {self.batch}\n'
        info += f'Monthly Fee {self.monthlyFee}\n'
        return info
    def display_std_info(self):
        print(self)
    
    # Update Methods
    #1. name change Method
    def changeName(self, newName:str):
         self.name = newName
    
    #2. E-mail change Method
    def changeEmail(self, newMail:str):
         self.email = newMail

    #3. Phone number change Method
    def changePhone(self, newPhone:str):
         self.phone = newPhone
    # End the Update Methods   
    # Main menu
s1 = None
while True:
    print('========== MENU ==========')
    print('1. Add Student')
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
            batch = str(input('Enter Batch: '))
            monthlyFee = float(input('Enter Monthly Fee: '))

            # create an object
            s1 = Student(name, id, email, phone, BG, department, batch, monthlyFee)
            print('You have successfully added !!')
    elif option == 2:
            if s1 is not None:
                clear_screen()
                s1.display_std_info()
                input('Press Enter to continue...')
                clear_screen()
            else:
                print('No Records Found\n')
    elif option == 3:
         print('====== Update Menu ======')
         print('1. Change Name')
         print('2. Change E-mail')
         print('3. Change Phone')
         print('==========================')
        
         select = int(input('Enter the Menu: '))
         clear_screen()
         if select == 1:
              newName = str(input('Enter new Name: '))
              s1.changeName(newName)
              print('Name change successfully !!')
         elif select == 2:
              newMail = str(input('Enter new E-mail: '))
              s1.changeEmail(newMail)
              print('E-mail Change Successfully !!')
         elif select == 3:
              newPhone = str(input('Enter new Phone: '))
              s1.changePhone(newPhone)
              print('Name change successfully !!')

    elif option == 4:
         pass

    elif option == 5:
         break