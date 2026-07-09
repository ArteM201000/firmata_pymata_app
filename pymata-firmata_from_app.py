from pathlib import Path
from pymata4 import pymata4
import time
from servo_py import Servo

board = pymata4.Pymata4("COM6", 57600)

servo = Servo(9, board)

path = Path("C:/Users/admin/Downloads/firmata/angle.txt")

servo.write_servo(0)
time.sleep(1.5)
servo.write_servo(180)
time.sleep(1)
while True:
    angle = path.read_text()
    path_block = Path("C:/Users/admin/Downloads/firmata/block.txt")
    block = path_block.read_text()
    if block == "True":
        print("Поворачиваю...")
        servo.write_servo(angle)
        time.sleep(1)
        path_block.write_text("False")