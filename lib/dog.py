#!/usr/bin/env python3

class Dog:

    def __init__(self, name, breed = "Mutt"): #init method
        self.name = name #attribute1
        self.breed = breed #attribute2
    pass

pass

sadie = Dog("Sadie")
print(sadie.name)
