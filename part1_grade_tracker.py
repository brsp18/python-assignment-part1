

#Task 1 — Data Parsing & Profile Cleaning

raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

    
cleaned_students = [] # creating an empty list
for i in raw_students: 
    name = i["name"].strip().title() # strip() removes mpty spaces and title() converts to title case
    roll=int(i["roll"]) # converting roll from string to int
    marks_int=i["marks_str"].split(", ") # splitting marks with ','
    cleaned_students.append({"name": name, "roll": roll, "marks": marks_int}) # appends formatted values to cleaned_students
print("\n")
print(cleaned_students) # Printing cleaned students list
print("\n") 

    #2. Print "✓ Valid name" or "✗ Invalid name" next to each student.

for i in cleaned_students:
       valid = i["name"].replace(" ", "").isalpha()
       if valid:
         print(i["name"], "✓ Valid name")
       else:
         print(i["name"], "✗ Invalid name")

     #3.Print a formatted profile card for each cleaned student using f-strings:

for i in cleaned_students: # printing all students in the given format using f string
    print("======================================") 
    print(f"Name: {i['name']}")
    print(f"Roll: {i['roll']}")
    print(f"Marks: {i['marks']}")
    print("======================================")

    #4.After processing all students, print the name in ALL CAPS and lowercase for the student with roll number 103.

for i in cleaned_students:
    if i["roll"] == 103:
        print("\n")
        print(f"UPPER CASE: {i['name'].upper()}")
        print(f"LOWER CASE: {i['name'].lower()}") 
        print("\n")# calculating total marks for each student
    





#Task 2 — Marks Analysis Using Loops & Conditionals 
#1. print each subject alongside its marks and a grade label based on this scheme:

student_name = "Ayesha Sharma"
subjects     = ["Math", "Physics", "CS", "English", "Chemistry"]
marks        = [88, 72, 95, 60, 78]

print("*****",student_name,"*****") 
grade = 0


for i in subjects:
    index = subjects.index(i)
    mark = marks[index]
   

for subject, mark in zip(subjects, marks):
    if mark >= 90:
        grade = "A+"
    elif mark >= 90:
      grade = "A+"
    elif mark >= 80:
      grade = "A"
    elif mark >= 70:
      grade = "B"
    elif mark >= 60:            
     grade = "C"
    else:
     grade = "F"
    print(f"{subject}: {mark} - {grade}")

    #2. Calculate and print:

total_marks = sum(marks)
average_marks = total_marks / len(marks)
Min_marks = min(marks)
Max_marks = max(marks)
print("\n")
print("Total Marks:", total_marks)
print("Average Marks:", average_marks)
print("Minimum Marks:", Min_marks)
print("Maximum Marks:", Max_marks)
print("\n")

   #3.  while loop, simulate a marks-entry system

while True:
    choice = input("Do you want to add a new subject and marks? Enter 'yes' to add or 'done' to exit : ")
    if choice == "done":
        break
    new_subject = input("Enter new subject name: ")
    new_mark = int(input("Enter marks for the subject (0-100): "))
    subjects.append(new_subject)
    marks.append(new_mark)
     
print("\n")
print("Updated Subjects and Marks lists:", "\n")
print(subjects)
print(marks)
print("\n")
print("Name           | Average       | Status ")







#Task 3 — Class Performance Summary

class_data = [
    ("Ayesha Sharma",  [88, 72, 95, 60, 78]),
    ("Rohit Verma",    [55, 68, 49, 72, 61]),
    ("Priya Nair",     [91, 85, 88, 94, 79]),
    ("Karan Mehta",    [40, 55, 38, 62, 50]),
    ("Sneha Pillai",   [75, 80, 70, 68, 85]),
]

#1.Loop through class_data and for each student:

pass_count = 0
fail_count = 0

for name, marks in class_data:
   marks_sum = sum(marks)
   average = marks_sum/len(marks)
   
# 2. Print a formatted class report:

   status = "Pass" if average>=60 else "Fail"
   print("--------------------------------------")
   print(f"{name:10}     | {sum(marks)/len(marks):8.2f} | {status:6} ") 
   print("--------------------------------------")

   if status == "Pass":
      pass_count = pass_count + 1
   else:        
      fail_count = fail_count + 1

print("\n")
print("Total Passed:", pass_count) 
print("Total Failed:", fail_count)


#3. After the table, print:Class Topper and Class Average.

avg = []
for name, marks in class_data:
   average = sum(marks)/len(marks)
   avg.append(average)

topper = max(avg)
print("\n")
print("Class Topper:",name,":" ,topper)
print("\n")





   #Task 4: String Manipulation Utility   

essay = "  python is a versatile language. it supports object oriented, functional, and procedural programming. python is widely used in data science and machine learning.  "
   
print("\n")    
clean_essay = essay.strip()
print("Cleaned Essay:", clean_essay)
print("\n")
titlecase_essay = clean_essay.title()
print("Title Case Essay:", titlecase_essay)
print("\n")
python_count =clean_essay.count("python")
print("Occurrences of 'python':", python_count)
print("\n")
clean_essay_replaced = clean_essay.replace("python", "Python 🐍")
print("Replaced Essay:", clean_essay_replaced)
print("\n")
split_clean_essay =clean_essay_replaced.split(". ")
print("Split Essay:", split_clean_essay)
print("\n")
n=0
for i in split_clean_essay:
    print(f"{n+1}. {i}")
    n=n+1

print("\n")
      
