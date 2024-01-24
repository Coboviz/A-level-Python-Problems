class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def copy(self):
        newPerson = Person(self.name, self.surname, self.age)
        return newPerson
        

    def __str__(self): #overwriting python's str method
        return f"Name : {self.name}, Surname : {self.surname}, Age : {self.age}"
    
    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname
    
    def get_age(self):
        return self.age
    
    def set_name(self, newName):
        self.name = newName

    def set_surname(self, newName):
        self.surname = newName

    def set_age(self, newAge):
        self.age = newAge

    # isOlder(self, Person p) : checks if a Person p is older than the current person
    
    def isOlder(self, p):
        return p.get_age() > self.get_age()

    # full_name(self): returns a string in the format "First Last"

    def fullName(self):
        return f"{self.get_name()} {self.get_surname()}"

    # is_adult(self): returns a boolean indicating whether the person is 18 or older

    def isAdult(self):
        return self.get_age() >= 18

person1 = Person('Maksim', 'Pirozhenko', 17)

print(person1)

print(person1.get_name())

person1.set_name("Maxim v2")

print(person1.get_name())

person2 = Person('Albion', 'Sulejmani', 18)

print(person1.isOlder(person2))

print(person2.fullName())

print(person1.isAdult())

print(person2.isAdult())

person3 = person2.copy()

print(person3)


class BankAccount:
    def __init__(self, person, balance):
        self.person = person.copy()
        self.balance = balance

    def __str__(self): #overwriting python's str method
        return f"Name : {self.person.name}, Surname : {self.person.surname}, Age : {self.person.age}, Balance: {self.balance}"
        
bankaccount1 = BankAccount(person2, 1000000)

print(bankaccount1)