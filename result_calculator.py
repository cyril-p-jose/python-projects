print("STUDENT RESULT CALCULATOR")
print("--------------------------")

name = input("Enter Student Name: ")

m1 = int(input("Enter Marks in Subject 1: "))
m2 = int(input("Enter Marks in Subject 2: "))
m3 = int(input("Enter Marks in Subject 3: "))
m4 = int(input("Enter Marks in Subject 4: "))
m5 = int(input("Enter Marks in Subject 5: "))

total = m1 + m2 + m3 + m4 + m5
average = total / 5

print("\n--- RESULT ---")
print("Name    :", name)
print("Total   :", total)
print("Average :", average)

if average >= 50:
    print("Result  : PASS")

    if average >= 90:
        print("Grade   : A+")
    elif average >= 75:
        print("Grade   : A")
    elif average >= 60:
        print("Grade   : B")
    else:
        print("Grade   : C")
else:
    print("Result  : FAIL")
    print("Grade   : F")
