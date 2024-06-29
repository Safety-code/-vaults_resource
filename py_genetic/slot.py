from enum import Enum


class ClassroomType(Enum):

    Tutorial = 1
    Lecture = 2
    Lab = 3

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


class Classrooms:
    def __init__(self, id, capacity, type:ClassroomType):
        self.id = id
        self.capacity = capacity
        self.type = type

    def __str__(self):
        return f"{self.id} {self.capacity} {self.type}"

# class Day:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

class Period:
    def __init__(self, id, time):
        self.id = id
        self.time = time

class Slot:
    id_counter = 0
    def __init__(self, day:Weekday, classroom:Classrooms, period:Period):
        self.id = Slot.id_counter
        Slot.id_counter += 0
        self.day = day
        self.classroom = classroom
        self.period = period


class Session:
    id_counter = 0
    def __init__(self, id, lecturerId, courseCode, class_Size):
        self.id = Session.id_counter
        Session.id_counter += 0
        self.id = id
        self.lecturerId = lecturerId
        self.courseCode = courseCode
        self.class_Size = class_Size
        
        