class Student:
    def __init__(self,roll_number,name,class_name) -> None:
        self.roll_number=roll_number
        self.name=name
        self.class_name=class_name
        self.marks={}

    def add_marks(self,subject,marks):
        if subject in self.marks:
            print(f"{self.marks} already exits.")
        else:
            self.marks[subject]=marks
    
    def display_all_info(self):
        print(f"\nStudent Name : {self.name}")
        print(f"Roll Number   : {self.roll_number}")        
        print(f"Marks:{self.marks}\n") 

A=Student(1,"A",12)
A.add_marks("English",85)
A.display_all_info()       

