#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
class Student:
   '所有学生的基类'
   male = 0
   stu_count = 0
   stu_count_nan = 0
   stu_count_nv = 0
 
   def __init__(self,stu_no, name,stu_class, male):
      self.stu_no=stu_no 
      self.name = name
      self.stu_class=stu_class
      self.male = male
      Student.stu_count += 1
      if self.male == '1':
         Student.stu_count_nan += 1
      elif self.male == '0':
         Student.stu_count_nv += 1
         
   
   def displayCount(self):
       print "Count :", Student.stu_count
 
   def displayStudent(self):
       print "Stu_no :", self.stu_no, "Name : ", self.name, "Stu_class :", self.stu_class , " male :",  self.male
 
