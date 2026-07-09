from pathlib import Path
from pymata4 import pymata4
import time
from servo_py import Servo

board = pymata4.Pymata4("COM6", 57600)

servo = Servo(9, board)

path = Path("angle.txt")
path_block = Path("block.txt")

while True:
    angle = path.read_text()
    block = path_block.read_text()
    if block == "True":
        servo.write_servo(angle)
        time.sleep(0.5)
        path_block.write_text("False")