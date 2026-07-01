class person:
    def accept(self):
        self.gender=input("Enter persons gender:")
        self.age=int(input("Enter perosons age:"))

    def display(self):
        print("Name:",self.gender)
        print("Age:",self.age)

class student(person):
    def acc(self):
        self.name=input("Enter student name:")
        self.rollno=int(input("Enter students Roll no."))

    def dis(self):
        print("Name:",self.name)
        print("Roll no.:",self.rollno)

s=student()
s.accept()
s.acc()
s.display()
s.dis()
