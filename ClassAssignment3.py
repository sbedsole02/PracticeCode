# 1. Create three dictionaries, each one will contain information about a particular student: Steve, Alice and Tyler
#   a. Assign each dictionary to a variable – eg. steve, alice and tyler
#   b. Create the following keys: name, homework, quizzes, and tests
#   c. Set the value of the name key to the name of the student – e.g. Steve's name should be "Steve"
#   d. Set the other keys – e.g. homework, quizzes, and tests – to empty lists (we'll fill them in later)
#   e. Print these empty dictionaries
steve = {"name": "Steve",
         "homework": [''],
         "quizzes": [''],
         "tests": ['']}
alice = {"name": "Alice",
         "homework": [''],
         "quizzes": [''],
         "tests": ['']}
tyler = {"name": "Tyler",
         "homework": [''],
         "quizzes": [''],
         "tests": ['']}

print(f"{steve['name']}\n{steve['homework']}\n{steve['quizzes']}\n{steve['tests']}\n")

print(f"{alice['name']}\n{alice['homework']}\n{alice['quizzes']}\n{alice['tests']}\n")

print(f"{tyler['name']}\n{tyler['homework']}\n{tyler['quizzes']}\n{tyler['tests']}\n")

# 2. Now fill in the dictionaries above with the following scores and print the dictionaries:
# Steve
#   Homework: 90, 97, 75, 92
#   Quizzes: 88, 40, 94
#   Tests: 75, 90
# Alice
#   Homework: 100, 92, 98, 100
#   Quizzes: 82, 83, 91
#   Tests: 89, 97
# Tyler
#   Homework: 0, 87, 75, 22
#   Quizzes: 0, 75, 78
#   Tests: 100, 100
steve.update({'homework': [90.0, 97.0, 75.0, 92.0]})
steve.update({'quizzes': [88.0, 40.0, 94.0]})
steve.update({'tests': [75.0, 90.0]})
print(f"{steve['name']}\n{steve['homework']}\n{steve['quizzes']}\n{steve['tests']}\n")

alice.update({'homework': [100.0, 92.0, 98.0, 100.0]})
alice.update({'quizzes': [82.0, 83.0, 91.0]})
alice.update({'tests': [ 89.0, 97.0]})
print(f"{alice['name']}\n{alice['homework']}\n{alice['quizzes']}\n{alice['tests']}\n")

tyler.update({'homework': [0.0, 87.0, 75.0, 22.0]})
tyler.update({'quizzes': [0.0, 75.0, 78.0]})
tyler.update({'tests': [100.0, 100.0]})
print(f"{tyler['name']}\n{tyler['homework']}\n{tyler['quizzes']}\n{tyler['tests']}\n")

# 3. Create a list called students that contains your three students and print the list
students = [steve, alice, tyler]
print(students)

# 4. Loop over your students list and print out the following for each student:
#   - Name: (print out the student's name)
#   - Homework: (print out the student's homework)
#   - Quizzes: (print out the student's quizzes)
#   - Tests: (print out the student's tests )
for student in students:
    print(f"{student['name']}\n{student['homework']}\n{student['quizzes']}\n{student['tests']}\n")

# 5. Define a function to calculate the average of a list
#   a. Define a function called average() that has one argument, a list of numbers
#   b. Inside the function, use the built-in Python functions sum() and len() to calculate the average
#   c. Return the result 
#   d. Test it out to make sure it works
def average(numbers):
    return sum(numbers) / len(numbers)
#testing
print(round(average([50, 20, 45]) ,1))
#testing
print(round(average(steve['homework']) ,1))

# 6. Write a function to calculate the weighted average score for a student
#   a. Define a function called get_weighted_average() that takes one argument: student (see the dictionaries we created above)
#   b. Use your average() function to calculate the average of the student's homework, quizzes, and test scores
#   d. Return the weighted average score for each student (homework is 10%, quizzes are 30%, and tests are 60%  of the grade).
#   e. Test out your get_weighted_average() function on each student
def get_weighted_average(student):
    homework = average(student['homework'])
    quizzes = average(student['quizzes'])
    tests = average(student['tests'])
    return 0.1*homework+0.3*quizzes+0.6*tests

print(round(get_weighted_average(steve), 1))
print(round(get_weighted_average(alice), 1))
print(round(get_weighted_average(tyler), 1))
# 7. Write a function to convert a grade into a letter grade
#   a. Define a function called get_letter_grade() that has one argument called score (a number)
#   b. Inside your function, use if / elif /else to return the following letter grades:
#       - 90 or above: “A"
#       - 80 or above: “B"
#       - 70 or above: “C"
#       - 60 or above: “D"
#       - Below 60: “F"
#   c. Test it out on a few different numbers to make sure it works properly
#   d. Use a for loop to get each student's letter grade
def get_letter_grade(score):
    if score >= 90:
        return  'A'
    elif score >= 80:
        return  'B'
    elif score >=70:
        return  'C'
    elif score >= 60:
        return  'D'
    else:
        return "F"

print(get_letter_grade(94))
print(get_letter_grade(82))
print(get_letter_grade(75))
print(get_letter_grade(66))
print(get_letter_grade(50))

for student in students:
    print(get_letter_grade(get_weighted_average(student)))

# 8. Write a function to calculate the class average
#   a. Create a function called get_class_average() that has one argument, students (a list of dictionaries)
#   b. Inside the function, create a temporary empty list called results to store each student's grade
#   c. Loop over the list of students, appending each student's grade into your results list
#   d. Finally, return the average of the results
#   e. Test out your function by printing out the class average
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_weighted_average(student))
    return average(results)

print(round(get_class_average(students) ,1))

# 9. The class has now a new student, Thomas, with the following grades:
#   Homework: 90, 85, 80, 0
#   Quizzes: 80, 100, 87
#   Tests: 85, 90
#   a. Create a dictionary for Thomas (as you did in #1)
#   b. add him to the class, by appending the dictionary to your list of students
#   c. Calculate the new class average and print your results
thomas = {"name": "Thomas",
          "homework": [],
          "quizzes": [],
          "tests": []}
thomas.update({'homework': [90.0, 85.0, 80.0, 0.0]})
thomas.update({'quizzes': [80.0, 100.0, 87.0]})
thomas.update({'tests': [85.0, 90.0]})
print(f"{thomas['name']}\n{thomas['homework']}\n{thomas['quizzes']}\n{thomas['tests']}\n")
students.append(thomas)


print(round(get_class_average(students) ,1))
