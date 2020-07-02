
# while loop for trip expense calculator
while True:
    number_of_students = int(input("Enter number of students: "))
    try:
        number_of_students <= 1000
        break

    except:
        print("Enter valid number of students")
        continue

total = 0
# ensuring valid numbers
for i in range(number_of_students):
    a = float(input())
    while a <= 10000:
        total += a
        break

    else:
        print("enter valid amount")
        continue

# price per student
Avg = total/number_of_students
print(Avg)