'''
Created on Jan 22, 2015

@author: Georgiana
'''
from domain.ContactDom import Contact

class Ui():
    def __init__(self, ctrl):
        self.ctrl = ctrl
        
    def adauga(self):
        id_cont= int(input("Introduceti id-ul persoanei: "))
        nume= input("Introduceti numele: ")
        nr_tel= input("Introduceti numarul de telefon: ")
        grup= input("Introduceti grupul din care va face parte: ")
        
        # aici prindem eroarea
        try:
            self.ctrl.adauga_la_agenda(id_cont, nume, nr_tel, grup)
        except ValueError as ex:
            print(ex)
        
    def afiseaza_contacte(self):
        lista=self.ctrl.getAllCtrl() 
        for contact in lista:
            print(contact.getNume(), contact.getNr_telefon()) 
        
    def start_ui(self):
        while True:
            print("1. adauga contact")
            print("2. afiseaza toate contactele")
            print("x. exit")
            
            cmd= input("Dati comanda: ")
            
            if cmd == "1":
                self.adauga()
            if cmd == 'x' :
                break
            if cmd == '2':
                self.afiseaza_contacte()