try:
    van = False
    while not van:
        x = float(input("Kérem az első számot: "))
        y = float(input("Kérem a második számot: "))
        b = input("Milyen műveletet szeretne elvégezni velük: ")

        if b == "+" or b== "összeadás":
            q = x+y
            print("A két szám összege:",q)
        elif b == "-" or b == "kivonás":
            w = x-y
            print("A két szám különbsége:",w)
        elif b== "*" or b=="szorzás":
            r = x*y
            print("A két szám szorzata:",r)
        elif (b=="/" or b =="osztás") and y!=0:
            t = x/y
            print("A két szám hányadosa:",t)
        else:
            print("Valamelyik értéket rosszul adta meg!")
            van = False
        print()
        m = input("Szeretne még más számokkal is számolni? (igen/nem) Válasz: ")
        if m == "igen":
            van = False
        if m == "nem":
            van = True
except:
    print("Valami hiba történt!")
print()
print("Program vége.")