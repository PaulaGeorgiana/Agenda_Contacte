from domain.ContactDom import Contact
lista = []
lista.append(Contact("1", "Paula", "07432", "familie"))
lista.append(Contact("2", "Paul", "0743954630", "altele"))
lista.append(Contact("3", "Darius", "0758", "job"))

numeFisier = "scriere.txt"

f = open(numeFisier, "w")
for c in lista:
    f.write(c.getId_contact() + "," + c.getNume() + "," + c.getNr_telefon() + "," + c.getGrup() + "\n")

f.close()
    