students = int(input("Enter number of students: "))  

result = {}

for i in range(students):
   print("\nEnter Details of student Number.", i+1)

   roll_no = int(input("Roll No: "))  
   name = input("Student Name: ")  
   marks = int(input("Marks: "))  

   result[roll_no] = [name, marks]


print(result)

for student in result:  
   if result[student][1] > 75:  
       print("Student's name who get more than 75 marks is/are",(result[student][0]))