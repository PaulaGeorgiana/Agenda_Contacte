'''
Created on Jan 22, 2015

@author: Georgiana
'''
from domain.ContactDom import Contact

class ContactCtrl():
    def __init__(self, repo, val):
        self.repo = repo
        self.val = val
        
    def adauga_la_agenda(self, id_cont, nume, nr_tel, grup):
        c= Contact(id_cont, nume, nr_tel, grup)
        
        # incearca validarea
        # daca se arunca o eroare, o prindem in UI, nu aici
        self.val.Contact_Val(c)
        
        # daca a fost aruncata o eroare, nu se ajunge executia pana aici
        self.repo.adauga(c)
    
    def getAllCtrl(self):
        return self.repo.getAll()
    
    def getAllForCtrl(self,grup):
        return self.repo.getAllFor(grup)
    
    def cautare_numar(self,nume):
        return self.repo.cauta(nume)
    
    def exportCSV(self, grup, numeFisier):
        lista = self.repo.getAllFor(grup)
        
        f = open(numeFisier, "w")
        for c in lista:
            f.write(c.getId_contact() + "," + c.getNume() + "," + c.getNr_telefon() + "," + c.getGrup() + "\n")
        f.close()
    
