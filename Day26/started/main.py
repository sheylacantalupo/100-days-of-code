import json
# started
numbers1 = [1, 2, 3, 4]
new_list = [number * 2 for number in numbers1]
print(new_list)

name = "Sheyla"
letters_list = [letter for letter in name]
print(letters_list)

numbers2 = [number * 2 for number in range(1, 5)]
print(numbers2)

# 26.2 Conditional list comprehension
numbers3 = [number for number in range(1, 100) if number % 2 == 0]
print(numbers3)

with open("file1.txt", "r") as file1:
    list1 = file1.readlines()
with open("file2.txt", "r") as file2:
    list2 = file2.readlines()
numbers4 = [int(number) for number in list1 if number in list2]
print(numbers4)

# 26.3 Dictionary comprehension
import random

names = ["Alex", "Bete", "Carolina", "Davi", "Eliana", "Frede"]
students_score = {student: random.randint(1, 100) for student in names}
print(students_score)
passed_students = {student:score for (student, score) in students_score.items() if score > 50}
print(passed_students)
with open('data.json', 'w') as fp:
    json.dump(passed_students, fp)