"""
    A data repository of courses, students, and instructors
"""
from collections import defaultdict
from HW08_Hengyuan_Zhang import file_reader
from typing import List, Dict, Any
from prettytable import PrettyTable


# define Student Class
class Student:
    def __init__(self, SCWID: int, Sname: str, Major: str) -> None:
        self.CWID = SCWID
        self.name = Sname
        self.major = Major
        self._mygrade = dict()

    @property
    def mygrade(self):
        return self._mygrade

    @mygrade.setter
    def mygrade(self, classes: str, grade: str) -> None:
        self.mygrade[classes] = grade


# define Instructor Class
class Instructor:
    def __init__(self, ICWID: int, Iname: str, Department: str) -> None:
        self.CWID = ICWID
        self.name = Iname
        self.department = Department
        self.mycourse = defaultdict()

    def add_student(self, Sname: str) -> None:
        self.mycourse[Sname] += 1


# define University Class
class University:
    def __init__(self) -> None:
        self.studentlist = list()
        self.instructorlist = list()
        self.gradelist = list()
        self.stu_summary: Dict[int, Dict[str, Any]] = defaultdict(dict)
        self.ins_summary: Dict[int, Dict[str, Any]] = defaultdict(dict)

    # read gradefile
    def readgrade(self, gradesfile: str) -> None:
        listgra: List[str] = file_reader(gradesfile, 4, sep='\t', header=False)
        self.gradelist = [item for item in list(listgra)]

    # read student
    def readstudent(self, studentsfile: str) -> None:
        liststu: List[str] = file_reader(studentsfile, 3, sep='\t', header=False)
        self.studentlist = [item for item in list(liststu)]

    # read instructorsfile
    def readinstructor(self, instructorsfile: str) -> None:
        listins: List[str] = file_reader(instructorsfile, 3, sep='\t', header=False)
        self.instructorlist = [item for item in list(listins)]

    # process student data
    def summary_stu(self) -> None:
        for i in self.studentlist:
            index = list()
            for j in self.gradelist:
                if i[0] == j[0]:
                    self.stu_summary.get(i[0])
                    self.stu_summary[i[0]]['Name'] = i[1]
                    index.append(j[1])
                    self.stu_summary[i[0]]['Compeleted Courses'] = sorted(index)

    # process instructor data
    def summary_ins(self) -> None:
        for i in self.gradelist:
            self.ins_summary.get(i[1])
            self.ins_summary[i[1]].setdefault('Students', 0)
            self.ins_summary[i[1]]['Students'] += 1
            for j in self.instructorlist:
                if i[3] == j[0]:
                    self.ins_summary[i[1]]['CWID'] = j[0]
                    self.ins_summary[i[1]]['Name'] = j[1]
                    self.ins_summary[i[1]]['Dept'] = j[2]

    # student summary pretty table
    def student_table(self) -> None:
        pt: PrettyTable = PrettyTable(field_names=['CWID', 'Name', 'Compeleted Courses'])
        for key, values in self.stu_summary.items():
            pt.add_row([key, values['Name'], values['Compeleted Courses']])
        return pt

    # instructor summary pretty table
    def instructor_table(self) -> None:
        pt: PrettyTable = PrettyTable(field_names=['CWID', 'Name', 'Dept', 'Course', 'Students'])
        for key, values in self.ins_summary.items():
            try:
                pt.add_row([values['CWID'], values['Name'], values['Dept'], key, values['Students']])
            except KeyError:
                print('can not find corresponding data')
        return pt
