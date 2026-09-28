all_Students = []

for i in range(5):
    name = input("Enter the name of student {}: ".format(i + 1))
    admission_number = input("Enter the admission number of {}: ".format(name))
    age = input("Enter the age of {}: ".format(name))
    programming_language = int(input("Enter the programming marks: "))
    internet_technology = int(input("Enter the internet technology marks: "))
    commerce = int(input("Enter the commerce marks: "))
    
    total_marks = int(programming_language + internet_technology + commerce)
    average_marks = float(total_marks / 3)
    
    def calulate_average_marks():
        if average_marks >= 80:
            return "A"
        elif average_marks >= 60:
            return "B"
        elif average_marks >= 45:
            return "C"
        elif average_marks >= 35:
            return "D"
        else:
            return "F"
        
    def classify_student():
        if calulate_average_marks() == "A":
            return "Distinction"
        elif calulate_average_marks() == "B":
            return "Credit"
        elif calulate_average_marks() == "C":
            return "Satisfactory"
        elif calulate_average_marks() == "D":
            return "Pass"
        else:
            return "Fail"
        
    all_Students.append([name, admission_number, age, total_marks, average_marks, calulate_average_marks(), classify_student()])

print("\nAll Students Data: ")
for student in all_Students:
    print("Name:", student[0])
    print("Admission Number:", student[1])
    print("Age:", student[2])
    print("Total Marks:", student[3])
    print("Average Marks:", student[4])
    print("Grade:", student[5])
    print("Classification:", student[6])
    print("-----------------------------")