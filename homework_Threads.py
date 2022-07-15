import threading
import random
import time

auto_speed =random.randint(30, 170)
train_speed =random.randint(70, 110)
train_point = 0
car_point = 0
crossroad = train_speed * 10 / 3.6


def train():
    global train_point
    for i in range(0, 30):
        train_point += train_speed / 3.6
        time.sleep(0.5)
        print(f"Train travelled:{round(train_point, 2)} ")


def car():
    global car_point
    for transit in range(0, 30):
        car_point += auto_speed/3.6
        if transit == 10:
            print(f" The distance difference between car and train is  {round((car_point - train_point),2)}, car moved = {round(car_point, 2)}, train moved = {round(train_point, 2)}")
            if auto_speed > train_speed:
                print("Car speed is higher. Car is moving forward")
            if (car_point - crossroad) < 20:
                print("Car speed is lower.The car is waiting for the train to pass")
                time.sleep(5)
                print("The train passed, the car is starting to move again")
        time.sleep(0.5)
        print(f"Car travelled:{round(car_point, 2)}")



print(f"Speed of the car is {auto_speed}, Speed of the train is {train_speed}")

th1 = threading.Thread(target=car, name="car thread", daemon=False)
th2 = threading.Thread(target=train, name="train thread", daemon=False)

th1.start()
th2.start()
