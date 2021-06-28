# Sohel Shekh
import os
os.system('cls||clear')    #To clear the screen for better view

print("""
---------------------------------
|	Marks Calculator	|
---------------------------------
|				|
--------- Sohel Shekh -----------
|				|
|____ENTER MARKS OUT OF 100_____|

    """)
subjects = ["English", "Maths", "Chemistry", "Biology", "IP"]
totalMarks = 0

for i in range(len(subjects)):
    while True:
        try:
            marksInput =  float(input(f"""
    Enter {subjects[i]} marks: """))
            if marksInput >= 0.0 and marksInput <= 100.0:
                subjects[i] = marksInput
                break
            else:
                print("""
    ERROR: Enter proper marks from 0 - 100""")
        except ValueError:
            print("""
    ERROR: Enter marks in numerical, string or empty field not allowed!""")

for i in range(len(subjects)):
    totalMarks = totalMarks + subjects[i]

percentage  = totalMarks / 500 * 100

if percentage >= 90:
	grade = "A+"
elif percentage >= 80 and percentage <= 90:
	grade = "A"
elif percentage >= 60 and percentage <= 80:
	grade = "B"
elif percentage >= 50 and percentage <= 60:
	grade = "C"
elif percentage < 50:
	grade = "Fail"

print(f"""   

    Total Marks :   {totalMarks} / 500
    Percentage  :   {percentage}%
    Grade       :   {grade}
    

    """)
