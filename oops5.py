#import random (isme random.randint likhna pdta)
from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo 

    def book(self, fro, to):
        print(f"Train is booked in train {self.trainNo}, It goes from {fro} to {to}")

    def getstatus(self):
        print(f"Train {self.trainNo} is running on time")

    def getFare(self, fro, to):
        print(f"The ticket for Train {self.trainNo}, running from {fro} to {to} is {randint(800,1000)}")

express = Train(234567)   #jaha bhi self vali cheeje h, vaha ye chipak jayega
express.book("New Delhi", "Etawah")
express.getstatus()
express.getFare("New Delhi", "Etawah")

