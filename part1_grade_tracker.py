from os import name


raw_students = [
    {"name": "  ayesha SHARMA  ", "roll": "101", "marks_str": "88, 72, 95, 60, 78"},
    {"name": "ROHIT verma",       "roll": "102", "marks_str": "55, 68, 49, 72, 61"},
    {"name": "  Priya Nair  ",    "roll": "103", "marks_str": "91, 85, 88, 94, 79"},
    {"name": "karan MEHTA",       "roll": "104", "marks_str": "40, 55, 38, 62, 50"},
    {"name": " Sneha pillai ",    "roll": "105", "marks_str": "75, 80, 70, 68, 85"},
]

    
cleaned_students = [] # creating an empty list
for i in raw_students: 
    name = i["name"].strip().title() # removing empty spaces and converting to title case
    roll=int(i["roll"]) # converting roll from string to int
    marks_int=i["marks_str"].split(", ") # splitting marks with ','
    cleaned_students.append({"name": name, "roll": roll, "marks": marks_int}) # appending formatted values to cleaned students
print(cleaned_students) # Printing cleaned students list

for i in cleaned_students:
    name = i["name"].isalpha() # checking if name contains only alphabets
    if name == False:
        print(i["name"], "✓ Valid name")
    else:        
        print(i["name"], "✗ Invalid name")  

for i in cleaned_students: # printing all students in the given format using f string
    print("======================================") 
    print(f"Name: {i['name']}")
    print(f"Roll: {i['roll']}")
    print(f"Marks: {i['marks']}")
    print("======================================")

for i in cleaned_students:
    if i["roll"] == 103:
        print(f"UPPER CASE: {i['name'].upper()}")
        print(f"LOWER CASE: {i['name'].lower()}") # calculating total marks for each student
    




    
     



