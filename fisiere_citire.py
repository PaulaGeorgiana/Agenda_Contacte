from domain.ContactDom import Contact

# Pentru deschidere de fisier
numeFisier = "ceva_fisier.txt"

# Se incearca deschiderea fisierului pentru citire
# In cazul in care nu exista este aruncata o exceptie
try:
    f = open(numeFisier, "r")
    f.close()
except FileNotFoundError:
    # Daca fisierul nu exista, in momentul cand este deschis
    # pentru scriere este creat automat
    f = open(numeFisier, "w")
    f.close()
    
# Cand executia ajunge aici, in mod sigur fisierul exista
# deci e sigur sa-l deschidem pentru citire
f = open(numeFisier, "r")

# Se citeste continutul fisierului
continut = f.read()

# Am terminat cu fisierul deci il inchidem
f.close()

# Separam **linile** din fisier si le punem intr-o lista
linii = continut.split("\n")

# Luam fiecare linie individual
for linie in linii:
    
    # Separam datele de pe linie, separate prin virgula
    date = linie.split(",")
    
    # Daca exista exact 4, sau cate ne intereseaza numai atunci facem
    # ceva cu ele
    if len(date) == 4:
        c = Contact(date[0],date[1],date[2],date[3])