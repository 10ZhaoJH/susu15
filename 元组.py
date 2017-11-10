Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tup1 = ('physics', 'chemistry', 1997, 2000);
>>> tup2 = (1, 2, 3, 4, 5 );
>>> tup3 = "a", "b", "c", "d";
>>> len((1,2,3))
3
>>> L[-2]

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    L[-2]
NameError: name 'L' is not defined
>>> tup1[-2]
1997
>>> tup1[1:]
('chemistry', 1997, 2000)
>>> tup1[2]
1997
>>> (1,2,3) + (4,5,6)
(1, 2, 3, 4, 5, 6)
>>> ('4') * 4
'4444'
>>> 3 in (1,2,3)
True
>>> for 2 in (1,2,3) : print 2,
SyntaxError: can't assign to literal
>>> for x in (1,2,3) : print x

1
2
3
>>> 
