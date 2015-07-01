Python Object Massacre (PyOM)

Simple ctypes hack, which gives you direct control under python objects`s memory
via injected into common base class AKA object the 'dump' attribute.

Lets hack int 100 to be 200:
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
>>> (100).dump[:20].index(100)
12
>>> (100).dump[12] = 200
>>> 100
200
>>> 100+100
400

Another example:
>>> word = 'hello world'
>>> word.dump[:100].index(ord('h'))
24
>>> word.dump[:100].index(ord('e'))
25
>>> word.dump[:100].index(ord('l'))
26
>>> word.dump[24]=ord('c')
>>> word.dump[25]=ord('r')
>>> word.dump[26]=ord('u')
>>> word.dump[27]=ord('e')
>>> word.dump[28]=ord('l')
>>> word
'cruel world'
>>>
