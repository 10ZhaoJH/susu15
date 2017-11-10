#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   stuCount = 0 
 
   def __init__(self,stu_no, name,stu_class, gender):
      self.stu_no=stu_no 
      self.name = name
      self.stu_class=stu_class
      self.gender = gender
      Student.stuCount += 1
   
   def study(self):
       print "Student can study"
       
   def getStuCount(self):
      return Student.stuCount

class PrimaryStudent(Student):
   primaryStuCount = 0
   
   def canRecite(self):
        print "Primary Student can recite"

   def canOral(self):
        print "Primary Student can oral"


class MiddleStudent(Student): 
   middleStuCount = 0

   def __init__(self,stu_no, name,stu_class, gender):
      self.stu_no=stu_no 
      self.name = name
      self.stu_class=stu_class
      self.gender = gender
      MiddleStudent.middleStuCount += 1


   def canChemistry(self):
      print "middle Student can Chemistry"

   def canPhyics(self):
      print "middle Student can Phyics"

