Important differences between Python 2.x and Python 3.x with examples

Division operator-
If we are porting our code or executing the python 3.x code in python 2.x, it can be dangerous if integer division changes go unnoticed (since it doesn’t raise any error). It is preferred to use the floating value (like 7.0/5 or 7/5.0) to get the expected result when porting our code.

print function-
This is the most well known change. In this the print function in Python 2.x is replaced by print() function in Python 3.x,i.e, to print in Python 3.x an extra pair of parenthesis is required.

Unicode:
 Python 2, implicit str type is ASCII. But in Python 3.x implicit str type is Unicode.
 
 xrange:
 xrange() of Python 2.x doesn’t exist in Python 3.x. In Python 2.x, range returns a list i.e. range(3) returns [0, 1, 2] while xrange returns a xrange object i. e., xrange(3) returns iterator object which work similar to Java iterator and generates number when needed.
 
 Error Handling:
 There is a small change in error handling in both versions. In python 3.x, ‘as’ keyword is required.
 
 _future_module:
 This is basically not a difference between two version, but useful thing to mention here. The idea of __future__ module is to help in migration. We can use Python 3.x
If we are planning Python 3.x support in our 2.x code,we can use_future_ imports it in our code.

TOOLS TO EXECUTE PYTHON
1. python IDLE
2)command prompt
3) subline text
4) pycharm
5) spydeer
6) pyScripter


PYTHON TOOLS FOR DIFFERENT DOMAIN 
1.for machine learning 
a) Scikit learn
b) StatsModel
c)Pymac
d)Theano


2.for big data
a)Pandas 
b)PySpark
c)Scikit learn

3.for IOT
a) mraa
b) sockets
c)mysqldb
d)numpy
e)matplotlib
f)tensorflow


4. for cyber security
a) SCAPY
b) nmap
c) yara
d) beautifulsoup
e)request


5.for automation Testing
a)selenium
b)TestComplete
c)Robotframework

6.network programing
a) scapy
B)dnspython

7. artificial inteligency
A) tensorflow
b) theano
c) keras
d) scikit-learn

