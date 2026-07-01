#Funtion to calculate the Average of the marks recieved in main function
def calculate_average(marks):
    Sum_of_Marks = 0
    Average_Marks = 0
    for i in marks:
        Sum_of_Marks = Sum_of_Marks + i
    Average_Marks = Sum_of_Marks/len(marks)
    return Average_Marks
#Funtion to calculate the grade of the marks recieved in main function
def get_grade(average):
    grade = "NA"
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade
#Main function to recieve the list of marks and calculate the average and grade by invoking them
def main():
    print("ENTER THE MARKS FOR FIVE SUBJECTS")
    Mark_List = []
    
    for i in range(1,6):
        while True:
            try:
                n=int(input(f"Enter the Mark for Subject {i} :"))
            except ValueError:
                print("Invalid Number , Please enter a Valid number !!!")
                continue
            if n >=0 and n <= 100:
               Mark_List.append(n)
               break
            else:
                print("Enter a valid mark - Mark should be in the range of 0 to 100")
    Average = calculate_average(Mark_List)
    Grade = get_grade(Average)
    print("Average Mark of the Student is  ",Average)
    if Grade == "F":
        print("Unfotunately , Grade secured by the student is ",Grade)
    else:
        print("Congratulations! Grade secured by the student is ",Grade)

main()


            

