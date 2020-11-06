Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import traceback
>>> #try:
>>> 	#raise Exception('This is Error')
>>> #except:
>>> 	#errorFile = open('error_log.txt','a')
>>> 	#errorFile.write(traceback.format_exc()) writes execption in error_log file
>>> 	#errorFile.close()
>>> 
>>> #This script will keep program execution on and raises an exception as string
>>> #This File must be saved in folder where your python.exe is installed