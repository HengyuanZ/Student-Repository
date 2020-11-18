"""
    Test Case of Student Repository
"""
import Student_Repository_Hengyuan_Zhang
import unittest


class HW09(unittest.TestCase):
    def test_summary_stu(self) -> None:
        un = Student_Repository_Hengyuan_Zhang.University()
        un.readgrade('grades.txt')
        un.readstudent('students.txt')
        un.readinstructor('instructors.txt')
        un.summary_stu()
        self.assertIsNotNone(un.stu_summary.items())
        un.summary_ins()
        self.assertIsNotNone(un.ins_summary.items())
        print(un.student_table())
        print(un.instructor_table())


if __name__ == "__main__":
    unittest.main(exit=False, verbosity=2)
