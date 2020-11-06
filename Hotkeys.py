from pynput import keyboard

COMBINATIONS=[{keyboard.Key.shift, keyboard.KeyCode(char='n')},
			{keyboard.Key.shift, keyboard.KeyCode(char='N')}]

current=set()

def execute():
	print('New File')
def on_press(key):
	if any([key in COMBO for COMBO in COMBINATIONS]):
		current.add(key)
		if any(all(k in current for k in COMBO)for COMBO in COMBINATIONS):
			execute()
def on_realese(key):
	if any([key in COMBO for COMBO in COMBINATIONS]):
		current.remove(key)

with keyboard.Listener(on_press=on_press, on_realese=on_realese) as listener:
	listener.join()
