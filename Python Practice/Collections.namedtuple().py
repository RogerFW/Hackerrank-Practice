# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
N = int(input())
fields = input().split()
total_marks = 0
for _ in range(N):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / N))
