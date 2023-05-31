from threading import *
from time import sleep

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hellooooo")
            sleep(0.5)


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(0.5)


t1 = Hello()
t2 = Hi()

# t1.run_fn()
# t2.run_fn()


t1.start()
sleep(0.2)
t2.start()


# main
t1.join()
t2.join()

print("bye")