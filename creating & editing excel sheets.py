Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import os
>>> import openpyxl
>>> os.chdir('C:\\Users\\kushal\\Desktop\\python')
>>> wb = openpyxl.Workbook()
>>> wb
<openpyxl.workbook.workbook.Workbook object at 0x000000000B8155B0>
>>> sheet = wb.get_sheet_names()

Warning (from warnings module):
  File "<pyshell#5>", line 1
DeprecationWarning: Call to deprecated function get_sheet_names (Use wb.sheetnames).
>>> sheet = wb.get_sheet_names
>>> sheet
<bound method Workbook.get_sheet_names of <openpyxl.workbook.workbook.Workbook object at 0x000000000B8155B0>>
>>> wb.get_sheet_names
<bound method Workbook.get_sheet_names of <openpyxl.workbook.workbook.Workbook object at 0x000000000B8155B0>>
>>> new_sheet = wb.create_sheet()
>>> new_sheet
<Worksheet "Sheet1">
>>> wb.get_sheet_names
<bound method Workbook.get_sheet_names of <openpyxl.workbook.workbook.Workbook object at 0x000000000B8155B0>>
>>> wb.get_sheet_names.value
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    wb.get_sheet_names.value
AttributeError: 'function' object has no attribute 'value'
>>> new_sheet['A3'].value
>>> new_sheet['A3'].value == None
True
>>> sheet2.title = 'Pysheet'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    sheet2.title = 'Pysheet'
NameError: name 'sheet2' is not defined
>>> new_sheet.title = 'Pysheet'
>>> wb.get_sheet_names
<bound method Workbook.get_sheet_names of <openpyxl.workbook.workbook.Workbook object at 0x000000000B8155B0>>
>>> names = wb.get_sheet_names()
>>> names
['Sheet', 'Pysheet']
>>> new_sheet['A1'] = 'afhsaklfkds'
>>> new_sheet['A1'].value
'afhsaklfkds'
>>> new_sheet['B2'] = '-'
>>> new_sheet['C1] = 12
	  
SyntaxError: EOL while scanning string literal
>>> new_sheet['C1'] = 12
>>> new_sheet['D2'] = '-'
>>> wb.save('created_with_python.xlsx')
>>> workbook = openpyxl.load_workbook('created_with_python')
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    workbook = openpyxl.load_workbook('created_with_python')
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\openpyxl\reader\excel.py", line 313, in load_workbook
    reader = ExcelReader(filename, read_only, keep_vba,
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\openpyxl\reader\excel.py", line 124, in __init__
    self.archive = _validate_archive(fn)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\openpyxl\reader\excel.py", line 94, in _validate_archive
    raise InvalidFileException(msg)
openpyxl.utils.exceptions.InvalidFileException: openpyxl does not support  file format, please check you can open it with Excel first. Supported formats are: .xlsx,.xlsm,.xltx,.xltm
>>> workbook = openpyxl.load_workbook('created_with_python.xlsx')
>>> sheet1=workbook.get_sheet_names()
>>> sheet1
['Sheet', 'Pysheet']
>>> sheet1 = workbook.get_sheet_by_name('Pysheet')

Warning (from warnings module):
  File "<pyshell#31>", line 1
DeprecationWarning: Call to deprecated function get_sheet_by_name (Use wb[sheetname]).
>>> sheet1
<Worksheet "Pysheet">
>>> sheet1['A1'].value
'afhsaklfkds'
>>> sheet2 = wb.create_sheet(title='new_sheet',index=0)
>>> sheet2
<Worksheet "new_sheet">
>>> workbook.save('created_with_python.xlsx')
>>> sheet2 = workbook.save('created_with_python.xlsx')
>>> sheet2
>>> wb1= openpyxl.load_workbook('created_with_python')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    wb1= openpyxl.load_workbook('created_with_python')
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\openpyxl\reader\excel.py", line 313, in load_workbook
    reader = ExcelReader(filename, read_only, keep_vba,
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\openpyxl\reader\excel.py", line 124, in __init__
    self.archive = _validate_archive(fn)
  File "C:\Users\kushal\AppData\Local\Programs\Python\Python38\lib\site-packages\openpyxl\reader\excel.py", line 94, in _validate_archive
    raise InvalidFileException(msg)
openpyxl.utils.exceptions.InvalidFileException: openpyxl does not support  file format, please check you can open it with Excel first. Supported formats are: .xlsx,.xlsm,.xltx,.xltm
>>> wb1= openpyxl.load_workbook('created_with_python.xlsx')
>>> sheets = wb1.get_sheet_names()
>>> sheets
['Sheet', 'Pysheet']
>>> 