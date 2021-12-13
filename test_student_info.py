import unittest
from student_info import StudentInfo
"""
First unittest is imported and the StudentInfo class from the student_info file is imported.
I then created the class TestingStudent which inherits the class TestCase from unittest.
Note: I have named all my functions starting with test_ so that unittest can recognise the tests.
In the first function 'test_display_name' I created two objects of the StudentInfo class
and passed three parameters (first name, last name, list of grades. 
These objects are stored in the variables student1 and student2.
I used the assertEqual function to check if the information in the object matches up with 
the expected test information.
In the assertEqual function I use student1 and student2 to access the property display_name 
using dot notation in the student info file.

I repeated this process for the rest of the functions and ran the tests.
"""

class TestingStudent(unittest.TestCase):

    def test_display_name(self):
        student1 = StudentInfo("Colum","O'Siochru",[80,70,90,98])
        student2 = StudentInfo("John","O'Brien",[40,56,78,67])
        self.assertEqual(student1.display_name,"Colum O'Siochru")
        self.assertEqual(student2.display_name,"John O'Brien")

    def test_display_email(self):
        person1 = StudentInfo("Colum","O'Siochru",[80,70,90,98])
        person2 = StudentInfo("John", "O'Brien", [40, 56, 78, 67])

        self.assertEqual(person1.display_email,"columo'siochru@yahoo.ie")
        self.assertEqual(person2.display_email,"johno'brien@yahoo.ie")

    def test_display_average(self):
        student_score1 = StudentInfo("Colum","O'Siochru", [80, 70, 90, 98])
        student_score2 = StudentInfo("John", "O'Brien", [40, 56, 78, 67])

        self.assertEqual(student_score1.display_average_score,84.5)
        self.assertEqual(student_score2.display_average_score,60.25)


























    # def test_display_name(self):
    #     stu_1 = StudentInfo("Colum","O'Siochru", [80, 68, 94, 92])
    #     self.assertEqual(stu_1.display_name, "Colum O'Siochru")