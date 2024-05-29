# # Let's learn about list comprehensions! You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.
#  Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to n . 
# Here, 0<= i <= x, 0 <=j <= y , 0<= k <= z . Please use list comprehensions rather than multiple loops, as a learning exercise.
# Example
# x = 1
# y = 1
# z = 2
# n = 3
# All permutations of  (i, j , k)are:
# [[0,0,0],[0,0,1],[0,0,2][0,1,0],[0,1,1],[0,1,2],[1,0,0],[1,0,1],[1,0,2],[1,1,0],[1,1.
# Print an array of the elements that do not sum to n = 3 .
# [[0,0,0],[0,0,1],[0,0,2][0,1,0],[0,1,1],[0,1,2],[1,0,1],[1,1,0],[1,1,0],[1,1,2]
# Input Format
# Four integers (x,y,z) and n, each on a separate line.
# Constraints
# Print the list in lexicographic increasing order.
# Sample Input 0
# 1
# 1
# 1
# 2
# Sample Output 0
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]





# Input values
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# List comprehension to generate the coordinates
coordinates = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i + j + k) != n]

# Print the result
print(coordinates)







# # Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.
# Input Format
# The first line contains n. The second line contains an array  A[] of n integers each separated by a space.
# Constraints
# 2 <= n <= 10
# -100 <= A[i] <= 100
# Output Format
# Print the runner-up score.
# Sample Input 0
# 5
# 2 3 6 6 5
# Sample Output 0
# 5









# # Step 1: Read the input values
n = int(input())
scores = list(map(int, input().split()))

# Step 2: Convert the list of scores to a set to remove duplicates
unique_scores = set(scores)

# Step 3: Convert the set back to a list and sort it in descending order
sorted_scores = sorted(unique_scores, reverse=True)

# Step 4: The runner-up score is the second element in the sorted list
runner_up_score = sorted_scores[1]

# Print the runner-up score
print(runner_up_score)









#  Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
# Example
# records=[["chi",20.00], ["beta",50.00],["alpha",50.00]]
# The ordered list of scores is [20.0, 50.0], so the second lowest score is 50.00. There are two students with that score:["beta","alpha"] . Ordered alphabetically, the names are printed as:
# alpha
# beta
# Input Forma
# The first line contains an integer,N , the number of students.
# The 2N subsequent lines describe each student over 2 lines.
# - The first line contains a student's name.
# - The second line contains their grade.
# Constraints
# 2 <= N <= 5
# There will always be one or more students having the second lowest grade.
# Output Format
# Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.

# Sample Input 0

# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39
# Sample Output 0

# Berry
# Harry









# Read number of students
n = int(input())

# Initialize the list to hold student records
students = []

# Read the student names and grades
for _ in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])

# Extract the grades and find the unique sorted list of grades
grades = sorted(set(student[1] for student in students))

# The second lowest grade is the second element in the sorted list of unique grades
second_lowest_grade = grades[1]

# Find all students who have the second lowest grade
second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]

# Sort the names of these students alphabetically
second_lowest_students.sort()

# Print the names of the students with the second lowest grade
for student in second_lowest_students:
    print(student)







# # The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
#  Print the average of the marks array for the student name provided, showing 2 places after the decimal.







if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    sonuc = 0
    average = float()
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    for i in student_marks[query_name]:
        sonuc += i
    average = sonuc / len(student_marks[query_name])
    print("%.2f" %average)





