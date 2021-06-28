# Encoding type: UTF-8
#Ending: CRLF
# Case type: Snake Case
from os import system
system("cls||clear")
print("""
      .
     / \ 
  1 /   \ 2
   /_____\  
      3         
      
      
      
""")

triangle_sides = []


def is_valid_triangle(tr_sides):
    if tr_sides[0]+tr_sides[1] >= tr_sides[2] and tr_sides[1]+tr_sides[2] >= tr_sides[0] and tr_sides[2]+tr_sides[0] >= tr_sides[1]:
        return True
    else:
        return False


def type_triangle(tr_sides):
    if tr_sides[0] == tr_sides[1] and tr_sides[1] == tr_sides[2]:
        print("It's an Equilateral Triangle")
    elif tr_sides[0] == tr_sides[1] or tr_sides[1] == tr_sides[2] or tr_sides[2] == tr_sides[1]:
        print("It's an Isoceles Triangle")
    else:
        print("It's a Scalene Triangle")


def take_input():
    for i in range(3):
        while True:
            try:
                side = float(input(f"Enter length of side {i+1} (cm): "))
                if side > 0:
                    triangle_sides.append(side)
                    break
                else:
                    print("Enter side length > 0")
            except ValueError as e:
                print("String or empty field not allowed!")


take_input()
while True:
    if is_valid_triangle(triangle_sides):
        type_triangle(triangle_sides)
        break
    else:
        print("""
Please enter a valid traingle!
""")
        take_input()
