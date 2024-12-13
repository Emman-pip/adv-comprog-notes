# superclass
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    # define a method to print the full name of the perfon
    def printName(self):
        print(f"I am {self.fname} {self.lname}")


# a class that inherits from the Person superclass
class FamilyPerson(Person):
    # override the constructor, add the role parameter
    def __init__(self, fname, lname, role):
        super().__init__(
            fname, lname
        )  # call the constructor of parent class and pass arguments
        self.role = role

    # define the ability method
    def ability(self):
        print("Unknown")

    # define the printRole method: prints the role of a family person (parent, child)
    def printRole(self):
        print(f"A {self.role}")


# a class that inherits fromt the FamilyPerson class
class Parent(FamilyPerson):
    def __init__(self, fname, lname):
        super().__init__(fname, lname, "Parent")  # defines the role to be 'Parent'


# inherits from the Parent class
class Father(Parent):
    # override the ability method
    def ability(self):
        print("Ability: Fixes stuff")


# inherits from the Parent class
class Mother(Parent):
    # override the ability method
    def ability(self):
        print("Ability: Shouts like an ambulance")


# inherits from the FamilyPerson class
class Child(FamilyPerson):
    # override the constructor
    # add the mother, father, and hobby as parameters

    def __init__(self, fname, lname, mother, father, hobby):
        super().__init__(fname, lname, "Child")
        self.hobby = hobby
        self.mother = mother
        self.father = father

    # override the printName method
    def printName(self):
        print(
            f"I am {self.fname} {self.lname}. Child of {self.mother.fname} {self.mother.lname} and {self.father.fname} {self.father.lname}"
        )

    # override the ability method
    def ability(self):
        print(f"Ability: i am good at {self.hobby}")


# run the program here
if __name__ == "__main__":
    # create an instance of the Mother class
    mom = Mother("Linda", "Parreno")

    # create an instance of the Father class
    father = Father("Parjadeco", "Parreno")

    # create an instance of the Child class
    child = Child("Emmanuel", "Parreno", mom, father, "sleeping")

    # application of duck typing
    # loop and invoke the printRole, printName, and ability methods of the different objects
    for i in [mom, father, child]:
        i.printRole()
        i.printName()
        i.ability()
        print()
