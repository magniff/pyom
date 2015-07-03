Python Object Massacre (PyOM)

Simple ctypes hack, which gives you direct control under python objects`s memory
via injected into common base class AKA object the 'memory' attribute.

Lets hack int 100 to be 200:
>>> import pyom
>>> pyom.activate()
>>>
>>> for index, value in enumerate((100).memory[:13]):
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
>>> (100).memory[:20].index(100)
12
>>> (100).memory[12] = 200
>>> 100
200
>>> 100+100
400

NOTE: this memory indexes are extremely low level, so they are actually depend
on your platform and compiler. 

Another example:
>>> word = 'hello world'
>>> word.memory[:100].index(ord('h'))
24
>>> word.memory[:100].index(ord('e'))
25
>>> word.memory[:100].index(ord('l'))
26
>>> word.memory[24]=ord('c')
>>> word.memory[25]=ord('r')
>>> word.memory[26]=ord('u')
>>> word.memory[27]=ord('e')
>>> word.memory[28]=ord('l')
>>> word
'cruel world'
>>>
