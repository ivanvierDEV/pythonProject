from pynput.keyboard import Listener, Key

def press(Key):
    print(Key)

def release(Key):
    pass

with Listener(on_press=press, on_release=release) as pegaTecla:
    pegaTecla.join()
