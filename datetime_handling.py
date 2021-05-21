Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import datetime as dt
>>> dt.datetime.now()
datetime.datetime(2021, 5, 21, 15, 16, 18, 266631)
>>> print(dt.datetime.now())
2021-05-21 15:16:31.951576
>>> dt.datetime(2020, 5, 17)
datetime.datetime(2020, 5, 17, 0, 0)
>>> date = dt.datetime.now()
>>> date.year
2021
>>> date.month
5
>>> date.date
<built-in method date of datetime.datetime object at 0x00000215C9668570>
>>> date.date()
datetime.date(2021, 5, 21)
>>> date.day
21
>>> date.hour
15
>>> date.mintues
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    date.mintues
AttributeError: 'datetime.datetime' object has no attribute 'mintues'
>>> date.mintue
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    date.mintue
AttributeError: 'datetime.datetime' object has no attribute 'mintue'
>>> date.minute
18
>>> date.second
10
>>> date.minute
18
>>> date.weekday
<built-in method weekday of datetime.datetime object at 0x00000215C9668570>
>>> date.weekday()
4
>>> date.strftime(
	'%b
	
SyntaxError: EOL while scanning string literal
>>> date.strftime("%B")
'May'
>>> date.strftime("%b")
'May'
>>> date.strftime("%a")
'Fri'
>>> date.strftime("%A")
'Friday'
>>> date.strftime("%w")
'5'
>>> date.strftime("%y")
'21'
>>> date.strftime("%Y")
'2021'
>>> date.strftime("%H")
'15'
>>> date.strftime("%I")
'03'
>>> date.strftime("%p")
'PM'
>>> date.strftime("%M")
'18'
>>> date.strftime("%S")
'10'
>>> date.strftime("%W")
'20'
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2021, 5, 21, 15, 23, 59, 744664)
>>> dt.date.today()
datetime.date(2021, 5, 21)
>>> from random import randint, choice
>>> randint(2,7)
6
>>> choice([1,2,34])
1
>>> choice(["Hello","World"])
'World'
>>> 