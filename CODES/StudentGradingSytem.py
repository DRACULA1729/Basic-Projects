'''STUDENT GRADING SYSTEM
.>take the name, marks of subjects and give grades(find Percentage )
'''

print("Hey JR. Hope you are having a good day!")
def greet():
    print("Hey JR. Hope you are having a good day!")

def get_student_name():
    name = input("Gimme your name kid:").title()
    return name

def get_marks(subjects):
    marks = []
    for subject in subjects:
        mark = int(input(f"Enter your marks in {subject}:"))
        marks.append(mark)
    return marks

def calculate_percentage(marks, total_subjects):
    total_marks = sum(marks)
    percentage = (total_marks / (total_subjects * 100)) * 100
    return percentage

def check_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'

def main():
    greet()
    name = get_student_name()
    subjects = ["maths", "science", "english", "social science", "hindi"]
    
    marks = get_marks(subjects)
    
    choice = input("Do you have more subjects (y/n): ").lower()
    if choice == 'y':
        n = int(input("How many?: "))
        for _ in range(n):
            extra_subject = input("Enter the name of the other subject: ")
            subjects.append(extra_subject)
            mark = int(input(f"Enter your marks in {extra_subject}: "))
            marks.append(mark)

    total_subjects = len(subjects)
    percentage = calculate_percentage(marks, total_subjects)
    grade = check_grade(percentage)
    
    print(f"Hey {name}, you got {grade} grade with {percentage:.2f}%")

if __name__ == "__main__":
    main()
























'''    
name=input("Gimme your name kid:").title()
print(f"Hey {name} lets get started with your grading system")
marks1=int(input("Enter your marks in maths:"))
marks2=int(input("Enter your marks in science:"))
marks3=int(input("Enter your marks in english:"))
marks4=int(input("Enter your marks in Social science:"))
marks5=int(input("Enter your marks in Hindi:"))
#if more subjects
choice=input("Do you have more subjects(y/n):").lower()
if choice=='n': 
    Percentage=((marks1+marks2+marks3+marks4+marks5)/500)*100
    if Percentage>=90:
        print(f"Hey {name} you got A grade with {Percentage}%")
    elif Percentage>=80:
        print(f"Hey {name} you got B grade with {Percentage}%")
    elif Percentage>=60:
        print(f"Hey {name} you got C grade with {Percentage}%")
    elif Percentage>=40:
        print(f"Hey {name} you got D grade with {Percentage}%")
    else:
        print(f"Hey {name} you got F grade with {Percentage}%")
elif choice=='y':
    n=int(input("How many?:"))
    extra_sub=[]
    for i in range(n):
       marks6=int(input("Enter your marks in other subject:"))
       extra_sub.append(marks6)
    Percentage=round((((marks1+marks2+marks3+marks4+marks5+sum(extra_sub))/((5+n)*100))*100),2)
    if Percentage>=90:
        print(f"Hey {name} you got A grade with {Percentage}%")
    elif Percentage>=80:
        print(f"Hey {name} you got B grade with {Percentage}%")
    elif Percentage>=60:
        print(f"Hey {name} you got C grade with {Percentage}%")
    elif Percentage>=40:
        print(f"Hey {name} you got D grade with {Percentage}%")
    else:
        print(f"Hey {name} you got F grade with {Percentage}%")
    

'''