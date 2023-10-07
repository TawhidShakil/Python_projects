class Person:
    def __init__(self, name:str, id:str, email:str, phone:str, BG:str)->None:
        self.name = name
        self.id = id
        self.email = email
        self.phone = phone
        self.BG = BG
    def __repr__(self)->str:
        return f'Person(Name: {self.name}, Id: {self.id}, E-mail: {self.email}, Phone: {self.phone}, BG: {self.BG})'