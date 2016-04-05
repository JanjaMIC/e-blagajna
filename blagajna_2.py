# -*- coding: utf-8 -*-

groceries = {
    "cmoki": 1.15,
    "grenivke": 1.45,
    "moka": 0.92,
    "pijaca": 0.78,
    "kruh": 1.80,
    "radenska": 2.0
}

def searchPrice(item):
    for food, price in groceries.iteritems():
        if item == food:
            return price

    print "Nimamo na zalogi"



item = (raw_input("Vtipkaj ime izdelka: ").lower())
print "cena izdleka je: " , searchPrice(item)

#if __name__== "__main__":