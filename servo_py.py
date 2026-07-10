from time import sleep as sp

"""
Библиотека для упрощенного управления сервоприводом через pymata4.
init_servo() вызывается в любых операциях с сервоприводом, чтобы устранить баги, вызванные pymata4.py + StandardFirmataPlus.ino.
"""

class Servo:
    def __init__(self, servo_pin, board):
        self.servo = servo_pin
        self.board = board

    def write_servo(self, angle):
        self.init_servo()
        sp(1.5)

        self.board.servo_write(self.servo, angle)

    def init_servo(self):
        self.board.set_pin_mode_servo(self.servo, 500, 2500)