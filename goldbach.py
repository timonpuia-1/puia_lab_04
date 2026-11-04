def este_prim(numar):
    if numar < 2:
        return False
    for i in range(2, int(numar**0.5) + 1):
        if numar % i == 0:
            return False
    return True

def conjectura_goldbach():
    try:
        n = int(input("Introduceți un număr natural par (n > 2): "))
        
        if n <= 2 or n % 2 != 0:
            print("Eroare: Valoare invalidă! Numărul trebuie să fie par și strict mai mare decât 2.")
            return

        for p in range(2, n // 2 + 1):
            q = n - p
            if este_prim(p) and este_prim(q):
                print(f"{p} + {q}")
                
    except ValueError:
        print("Eroare: Nu ați introdus un număr valid!")

if __name__ == "__main__":
    conjectura_goldbach()