print ("Dobrodosli v spletni trgovini! Za ceno izberite izdelek iz nasega seznama!")


seznam_izdelkov = {"jajca": float(5.3), "moka": float(1.4), "kava": float(1.8), "caj": float (4.8), "mleko": float(2.2) }

for produkt in seznam_izdelkov:
    print produkt


while True:
    izbrani_izdelek = str(raw_input("Izberi izdelek iz seznama: "))

    if izbrani_izdelek in seznam_izdelkov.keys():
        cena = seznam_izdelkov[izbrani_izdelek]
        print ("Cena izdelka je %s" % (cena)), "Ce te zanima se kaj..."

    else:
        print ("Tega izdelka zal nimamo.Hvala do naslednjic.")
        break




