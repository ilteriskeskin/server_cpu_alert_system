import time
import datetime
import timeit


def countdown_timer(x):
    a = 50
    while x >= 0 :
        x -= 1
        print("{} remaining".format(str(datetime.timedelta(seconds=x))))
        print("\n")
        time.sleep(1)
        a = a - 1
        if a == 48 or a == 45 or a == 42:
            print("Taaaaataataa")

if __name__ == '__main__':
    print(timeit.timeit(lambda:countdown_timer(120), number=1))
