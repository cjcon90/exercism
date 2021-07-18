import random

class Robot:
    def __init__(self):
        self.name = ""
        self.gen_name()

    def gen_name(self):
        for i in range(2):
            self.name += chr(random.randint(65,90))
        for i in range(3):
            self.name += str(random.randint(0,9))

    def reset(self):
        random.seed(self.name)
        self.name = ""
        self.gen_name()
