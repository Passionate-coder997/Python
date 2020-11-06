Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:52:53) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pyautogui
>>> #for multiple keys at a time
>>> pyautogui.click(150,150);pyautogui.typewrite('Hello', interval=0.5}
SyntaxError: closing parenthesis '}' does not match opening parenthesis '('
>>> pyautogui.click(150,150);pyautogui.typewrite('Hello', interval=0.5)
>>> pyautogui.click(150,150);pyautogui.typewrite('Hello'*4, interval=0.5)
>>> #all keyboard keys
>>> pyautogui.KEY
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    pyautogui.KEY
AttributeError: module 'pyautogui' has no attribute 'KEY'
>>> pyautogui.KEYBOARD_KEYS
['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace', 'browserback', 'browserfavorites', 'browserforward', 'browserhome', 'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear', 'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete', 'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20', 'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja', 'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail', 'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack', 'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn', 'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn', 'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator', 'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab', 'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen', 'command', 'option', 'optionleft', 'optionright']
>>> pyautogui.KEYBOARD_KEYS()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    pyautogui.KEYBOARD_KEYS()
TypeError: 'list' object is not callable
>>> pyautogui.click(150,150);pyautogui.typewrite('space Hello'*4, interval=0.5)
>>> pyautogui.click(150,150);pyautogui.typewrite(space,'Hello'*4, interval=0.0.1)
SyntaxError: invalid syntax
>>> pyautogui.click(150,150);pyautogui.typewrite('This \ text \ is \ written \ in \ python'*4, interval=0.0.1)
SyntaxError: invalid syntax
>>> pyautogui.click(150,150);pyautogui.typewrite('This \ text \ is \ written \ in \ python'*4, interval=0.1)
>>> pyautogui.click(150,150);pyautogui.typewrite('This text is written in python'*4, interval=0.1)
>>> pyautogui.click(150,150);pyautogui.typewrite('This text is written in python '*4)
>>> #for pressing single key at a time
>>> pyautogui.press(f1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    pyautogui.press(f1)
NameError: name 'f1' is not defined
>>> pyautogui.press('f1')
>>> #for pressing shortcut keys
>>> pyautogui.hotkey('ctrl','n')
>>> 