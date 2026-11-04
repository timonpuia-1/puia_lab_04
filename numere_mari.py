import os

def citeste_numere(nume_fisier):
    """Verifică existența fișierului și validitatea datelor."""
    if not os.path.exists(nume_fisier):
        print(f"Eroare: Fișierul '{nume_fisier}' nu există.")
        return None, None
    
    with open(nume_fisier, 'r') as f:
        linii = f.read().splitlines()
    
    if len(linii) < 2:
        print("Eroare: Fișierul trebuie să conțină cel puțin două numere (câte unul pe rând).")
        return None, None
    
    num1, num2 = linii[0].strip(), linii[1].strip()
    
    if not num1.isdigit() or not num2.isdigit():
        print("Eroare: Fișierul conține caractere invalide (trebuie să conțină doar cifre).")
        return None, None
        
    return num1, num2

def adunare(num1, num2):
    """Adunare cifră cu cifră, de la dreapta la stânga, folosind transportul."""
    rezultat = []
    transport = 0
    # Egalăm lungimile adăugând zerouri nesemnificative la început
    max_len = max(len(num1), len(num2))
    n1 = num1.zfill(max_len)
    n2 = num2.zfill(max_len)
    
    for i in range(max_len - 1, -1, -1):
        cifra_suma = int(n1[i]) + int(n2[i]) + transport
        rezultat.append(str(cifra_suma % 10))
        transport = cifra_suma // 10
        
    if transport > 0:
        rezultat.append(str(transport))
        
    # Inversăm rezultatul deoarece am adăugat de la dreapta la stânga
    return ''.join(rezultat[::-1])

def inmultire(num1, num2):
    """Înmulțire prin produse parțiale și transport, simulând înmulțirea în coloană."""
    if num1 == "0" or num2 == "0":
        return "0"
        
    len1, len2 = len(num1), len(num2)
    rezultat = [0] * (len1 + len2)
    
    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            produs = int(num1[i]) * int(num2[j])
            
            p1 = i + j
            p2 = i + j + 1
            
            # Adăugăm la valoarea existentă pe poziția curentă
            suma = produs + rezultat[p2]
            
            rezultat[p2] = suma % 10
            rezultat[p1] += suma // 10
    
    rez_str = "".join(map(str, rezultat))
    # Eliminăm zerourile nesemnificative de la început
    return rez_str.lstrip("0")

def main():
    fisier = "numere.txt"
    num1, num2 = citeste_numere(fisier)
    
    if num1 is not None and num2 is not None:
        suma = adunare(num1, num2)
        produs = inmultire(num1, num2)
        
        print(f"Numărul 1: {num1}")
        print(f"Numărul 2: {num2}")
        print(f"Suma: {suma}")
        print(f"Produsul: {produs}")

if __name__ == "__main__":
    main()