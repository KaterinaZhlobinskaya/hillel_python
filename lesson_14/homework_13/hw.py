from threading import Thread
from random import randint

digits = []
res = []


def fill_list():
    global digits
    digits = [randint(1, 10) for i in range(10000)]


def sum_list():
    global digits
    res.append("sum=" + str(sum(digits)))


def avg_list():
    global digits
    res.append("avg=" + str((sum(digits) / len(digits))))


t1 = Thread(target=fill_list)
t2 = Thread(target=sum_list)
t3 = Thread(target=avg_list)
t1.start()
t1.join()
t2.start()
t3.start()
t2.join()
t3.join()
print(digits)
print(res)