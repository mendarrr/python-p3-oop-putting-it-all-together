#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        if not isinstance(size, int):
            print("size must be an integer")
            self.size = 0
        else:
            self.size = size
        self.brand = brand
        self.condition = "New"

    def cobble(self):
        self.condition = "New"
        print("The shoe has been repaired.")   
    pass