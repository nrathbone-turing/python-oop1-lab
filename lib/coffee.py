#!/usr/bin/env python3

class Coffee:
    def __init__(self, size, price):
        self.size = size
        self.price = price

    # size property
    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not value in ["Small","Medium","Large"]:
            print("size must be Small, Medium, or Large")

        self._size = value

    # price property
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value
    
    def tip(self):
        print("This coffee is great, here’s a tip!")
        self._price += 1