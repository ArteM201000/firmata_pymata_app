from time import sleep as sp

class Servo:
    def __init__(self, servo_pin, board):
        self.servo = servo_pin
        self.board = board

    def write_servo(self, angle):
        self.init_servo()
        
        sp(0.5)

        angle = int(angle)
        self.board.servo_write(self.servo, angle)

    def init_servo(self):
        self.board.set_pin_mode_servo(self.servo, 500, 2500)