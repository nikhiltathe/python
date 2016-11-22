import threading

class MyMessanger(threading.Thread):
    def run(self):
        for _ in range(100):
            print(threading.current_thread().getName())


x = MyMessanger(name="One")
y = MyMessanger(name="Two")
x.start()
y.start()