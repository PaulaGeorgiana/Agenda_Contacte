'''
Created on Jan 22, 2015

@author: Georgiana
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
        

class  ContactRepo():
    def __init__(self):
        self.lista = []
        
    def adauga(self, contact):
        self.lista.append(contact)
        
    def getAll(self):
        return self.lista
    

class ContactCtrl():
    def __init__(self, repo):
        self.repo = repo
        
    def adauga_la_agenda(self, id_cont, nume, nr_tel, grup, repo):
        c= Contact(id_cont, nume, nr_tel, grup)
        repo.adauga(c)
    
    
class Ui():
    def __init__(self, ctrl):
        self.ctrl = ctrl
        
    def adauga(self):
        id_cont= int(input("Introduceti id-ul persoanei: "))
        nume= input("Introduceti numele: ")
        nr_tel= int(input("Introduceti numarul de telefon: "))
        grup= input("Introduceti grupul din care va face parte: ")
        
        self.ctrl.adauga_la_agenda(id_cont, nume, nr_tel, grup)
    def UI(self):
        while True:
            print("1. adauga contact")
            print("x. exit")
            
            cmd= input("Dati comanda: ")