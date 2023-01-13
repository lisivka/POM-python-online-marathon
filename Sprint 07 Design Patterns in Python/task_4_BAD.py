"""
Imagine we have a washing machine which can wash the clothes, rinse the clothes and spin the clothes
but all the tasks separately. We need a system that can automate the whole task without the disturbance
or interference of us.

To solve the above-described problem, we would like to hire the Facade Method. It will help us to hide
or abstract the complexities of the subsystems as follows.

Примітка: методи wash(), rinse() і spin() забезпечують результат відповідної операції.

img_2.png

"""


class WashingMachine:
    pass

    def wash(self):
        print("Washing...")

    def rinse(self):
        print("Rinsing...")

    def spin(self):
        print("Spinning...")

    def startWashing(self):
        self.wash()
        self.rinse()
        self.spin()


if __name__ == "__main__":
    washingMachine = WashingMachine()
    washingMachine.startWashing()

    # Washing...
    # Rinsing...
    # Spinning...
