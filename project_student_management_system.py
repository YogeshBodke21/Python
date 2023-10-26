
#PROJECT :- Student management system


class Student:

    def __init__(self, n, rn, m):
        self.name = n
        self.rollno = rn
        self.marks = m

    def __str__(self):
        
        return f"\nName : {self.name}, Roll_No: {self.rollno}, Marks:{self.marks}"

s1 = Student("Yogesh", 1, 85.0)
s2 = Student("Mahesh", 2, 75.0)
s3 = Student("Ajit", 3, 95.0)
s4 = Student("Sourabh", 4, 85.0)

student_list = [s1, s2, s3, s4]

def show_student():
    ch = int(input("\nEnter choice:\n1.To show student in alphabetical order\n2.To show in ascending order of marks\n3.To show in roll number wise"))
    match ch:
        case 1:
            sort_list = sorted(student_list, key=lambda  x:x.name)
            for stu in sort_list:
                 print(stu)
        case 2:
            sort_list = sorted(student_list, key=lambda x:x.marks)
            for stu in sort_list:
                 print(stu)

        case 3:
            sort_list = sorted(student_list, key=lambda x:x.rollno)
            for stu in sort_list:
                 print(stu)
               
    

def add_student():
    print("\nTo add a student please enter below details carefully.")
    n = input("Enter the name of student:")
    rn = int(input("Enter the roll number of student:"))
    m = float(input("Enter the marks of student:"))
    t = Student(n, rn, m)
    student_list.append(t)

def choice(student_to_be_update):
    c = int(input("Enter the choice:\n1.To update roll number\n2.To update name\n3.To update marks"))
    match c:
        case 1:
            new_roll =  int(input("Enter the new Roll number:"))
            student_to_be_update.rollno = new_roll

        case 2:
            new_name =  int(input("Enter the new name :"))
            student_to_be_update.name = new_name

        case 3:
            new_marks =  int(input("Enter the new marks :"))
            student_to_be_update.marks = new_marks
            

def update_student():
    roll = int(input("Enter the roll number to change"))
    found = False
    for stu in student_list:
        if stu.rollno == roll:
            found = True
            student_to_be_update = stu
            break
    if found:
        choice(student_to_be_update)
    else:
        print("No such roll number found")
            
def delete_student():
    roll = int(input("Enter the roll number of student which u hv to delete"))
    for stu in student_list:
        found = False
        if stu.rollno == roll:
            found = True
            student_to_be_delete = stu

    if found:
        student_list.remove(student_to_be_delete)
        print(f"{student_to_be_delete} is deleted successfully.")
    else:
        print("No such roll no found")
            
while True:
    ch = int(input("\nEnter the choice:\n1.To show Students\t2.To add student\n3.To Update student\t4.To delete student\n5.Exit"))

    match ch:

        case 1:
            show_student()

        case 2:
            add_student()

        case 3:
            update_student()

        case 4:
            delete_student()

        case 5:
            print("\nExiting..!!")
            break

        case _:
            print("Invalid Input..!")
        


print("PROGRAM ENDS.\nBye..!!!")
