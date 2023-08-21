import threading
import time


def squares(numbers):
    for number in numbers:
        time.sleep(0.2)
        print("Square of numbers is:",number*number)

def cubes(numbers):
    for number in numbers:
        time.sleep(0.2)
        print('Cube of numbers is:', number*number*number)

initial_time = time.time()
l = [1,2,3,4,5]
t1 = threading.Thread(target=squares, args=(l, ))
t2 = threading.Thread(target=cubes, args=(l, ))
t1.start()
t2.start()

t1.join()
t2.join()
print("Time Taken:", time.time()-initial_time)