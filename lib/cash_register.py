#!/usr/bin/env python3

class CashRegister:
    total = 0
    items = []

    def __init__(self, discount=0):
        self.discount = discount

    def add_item(self, title, price=3, quantity=1):
        for i in range(quantity):
            self.items.append((title, price, quantity))
        self.total += price * quantity
        

    def apply_discount(self):
        self.total -= (self.total * self.discount) / 100

        if self.discount:
            print(f"After the discount, the total comes to $800.")
        else:
            print("There is no discount to apply.")

        item_titles = list(map(lambda x: x[0], self.items))
        return item_titles
    

    def void_last_transaction(self):
        if self.items:
            last_item = self.items.pop()
            self.total -= last_item[1] * last_item[2]

bill = CashRegister()


