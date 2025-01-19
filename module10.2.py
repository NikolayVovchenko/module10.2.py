import threading
import time

class Knidht(threading.Thread):
    def __init__(self, name:str, power:int):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100


    def run(self):
        days = 0
        print(f'{self.name}, на нас напали')
        while self.enemies > 0:
            days += 1
            self.enemies -= self.power

            print(f'{self.name} сражается {days} дней(дня).., осталось{self.enemies} врагов')
            time.sleep(1)
        print(f'{self.name} одержал победу спустя {days} дней!')

first_knight =Knidht('Sir Lancelot', 10,)
second_knight =  Knidht('Sir Galahad', 20,)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились!')