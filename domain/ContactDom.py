'''
Created on Jan 22, 2015

@author: Georgiana

cand termini ce ai vrut sa faci, dai commit -> sync si dupa ma uit peste si iti las comentarii
'''

class Contact():
    def __init__(self, id_cont, nume, nr_tel, grup):
        self.id_contact = id_cont
        self.nume = nume
        self.nr_telefon = nr_tel
        self.grup = grup
    
    def getId_contact(self):
        return self.id_contact
    
    def getNume(self):
        return self.nume
    
    def getNr_telefon(self):
        return self.nr_telefon
    
    def getGrup(self):
        return self.grup
        
    def setNume(self, numeN):
        self.nume = numeN
        
    def setNr_telefon(self, nr_telefonN):
        self.nr_telefon= nr_telefonN
        
    def setGrup(self, grupN):
        self.grup= grupN
        

    



