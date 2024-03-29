"""
Imagine we have a washing machine which can wash the clothes, rinse the clothes and spin the clothes
but all the tasks separately. We need a system that can automate the whole task without the disturbance
or interference of us.

To solve the above-described problem, we would like to hire the Facade Method. It will help us to hide
or abstract the complexities of the subsystems as follows.

Примітка: методи wash(), rinse() і spin() забезпечують результат відповідної операції.

img_2.png

"""


class Washing:
    def wash(self):
        print("Washing...")


class Rinsing:
    def rinse(self):
        print("Rinsing...")


class Spinning:
    def spin(self):
        print("Spinning...")


class WashingMachine:

    def __init__(self):
        self.wash = Washing()
        self.rinse = Rinsing()
        self.spin = Spinning()

    def startWashing(self):
        self.wash.wash()
        self.rinse.rinse()
        self.spin.spin()


if __name__ == "__main__":
    washingMachine = WashingMachine()
    washingMachine.startWashing()

    # Washing...
    # Rinsing...
    # Spinning...
