"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a
list of students. Print the average of the marks array for the student name provided, showing 2 places
after the decimal.

Example
'alpha':[20,30,40]
'beta':[30,50,70]
query_name = 'beta'
The query_name is 'beta'. beta's average score is (30 + 50 + 70)/3 = 50.0

INPUT FORMAT: The first line contains the integer n, the number of students' records. The next n lines contain the
names and marks obtained by a student, each value separated by a space. The final line contains
query_name, the name of a student to query.

CONSTRAINTS
2 <= n <= 10
0 <= marks[i] <= 100
length of marks arrays = 3

OUTPUT FORMAT: Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input
3
James 44 54 60
Mary 40 55 70
Mike 55 60 50
Mary

Output: 34.0 Explanation: (40 + 55 + 70)/3
"""


class FindPercentage:
    def __init__(self):
        self.student_marks = dict()

    # a static method to accept and return the number of students whose marks will be inputted
    @staticmethod
    def number_of_students():
        num_of_students = int(input("Total number of students: "))
        return num_of_students

    # a method to accept the names and scores and add them as key value pair to the student_marks variable
    def student_name_and_marks(self):
        for _ in range(self.number_of_students()):
            name, *line = input("Enter student name and marks separated by a space: ").split()
            scores = list(map(float, line))
            self.student_marks[name] = scores
        return self.student_marks

    # a method to  accept student name and compute the average for that student.
    def compute(self):
        total_mark = 0
        query_name = input("Enter student name to find average for: ")
        mark_length = len(self.student_marks[query_name])

        for i in self.student_marks[query_name]:
            total_mark += i

        average_mark = format((total_mark / mark_length), ".2f")
        return average_mark


# Use Cases
percentage = FindPercentage()
percentage.student_name_and_marks()
print(f"Average Score: {percentage.compute()}")
