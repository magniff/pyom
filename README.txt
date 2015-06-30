Python Object Massacre (PyOM)

Simple ctypes hack, which gives you direct control under python objects`s memory

>>> import pyom
>>> pyom.activate()
>>>
>>> for index, value in enumerate((100).dump[:13]):
...     print(index, value)
...
0 7
1 0
2 0
3 0
4 80
5 41
6 180
7 98
8 1
9 0
10 0
11 0
12 100
>>> (100).dump[12] = 200
>>> 100
200
>>> 100+100
400
