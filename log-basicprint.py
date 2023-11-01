Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('Hello World')
Hello World
>>> print('Hello Loong')
Hello Loong
>>> name = 'Uncle'
>>> lastname = 'Engineer'
>>> fullname = name + ' ' + lastname
>>> print(fullname)
Uncle Engineer
>>> fullname = name + lastname
>>> print(fullname)
UncleEngineer
>>> name = 'สมชาย'
>>> lastname = 'ดีมาก'
>>> fullname = name + lastname
>>> print(fullname)
สมชายดีมาก
>>> type(name)
<class 'str'>
>>> age = 10
>>> type(age)
<class 'int'>
>>> name = 'Uncle'
>>> name.upper()
'UNCLE'
>>> name.lower()
'uncle'
print(name)
Uncle
name = name.upper()
print(name)
UNCLE
number = '1'
number.zfill(5)
'00001'
number = '15'
number.zfill(5)
'00015'
'อายุ'+10
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    'อายุ'+10
TypeError: can only concatenate str (not "int") to str
print('ลุงครับผมชื่อ{} นามสกุล{} อายุ {} ขวบ'.format(name,lastname,age))
ลุงครับผมชื่อUNCLE นามสกุลดีมาก อายุ 10 ขวบ
print(f'ลุงครับผมชื่อ{name} นามสกุล{lastname} อายุ {age} ขวบ')
ลุงครับผมชื่อUNCLE นามสกุลดีมาก อายุ 10 ขวบ
