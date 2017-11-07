#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:

   stu_Count = 0
   stu_Count_male = 0
   stu_Count_female = 0
   
 
   def __init__(self, stu_no, name,stu_class, male):
      self.stu_no=stu_no
      self.name = name
      self.stu_class=stu_class
      self.male=male
      Student.stu_Count += 1
      if self.male == '1':
         Student.stu_Count_male += 1
      elif self.male == '0':
         Student.stu_Count_female += 1
   
   
   def displayCount(self):
     print "Total Count %d" % Student.stu_Count
 
   def displayStudent(self):
      print "Name : ", self.name,  ", stu_no: ", self.stu_no, ",stu_class:", self.stu_class, ",male:", self.male
