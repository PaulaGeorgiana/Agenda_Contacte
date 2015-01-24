'''
Created on 24 ian. 2015

@author: ToTaL
'''


class ContactValidator():
    def Contact_Val(self, contact):
        erori= []
        grup=["prieteni", "familie", "job", "altele"]
        
        if contact.getNume()=="":
            erori.append("Nume vid")
        if contact.getGrup() not in grup:
            erori.append("Grup invalid")   # cu acent pe GRUP INVALID =))
        nr=contact.getNr_telefon()
        if nr == "":
            erori.append("numar vid")
        else:
            for i in nr:
                if i not in "0123456789":
                    erori.append("numar invalid")
                    
                    # daca nu pui break aici sa opresti if-ul
                    # o sa adauge cate o eroare pentru fiecare caracter care nu e cifra
                    break
        
        if erori != []:
            raise ValueError(erori)
