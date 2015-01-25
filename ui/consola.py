'''
Created on Jan 22, 2015

@author: Georgiana
'''
from domain.ContactDom import Contact

class Ui():
    def __init__(self, ctrl):
        self.ctrl = ctrl
        
    def adauga(self):
        
        id_cont = input("Introduceti id-ul persoanei: ")
          
        nume = input("Introduceti numele: ")
        nr_tel = input("Introduceti numarul de telefon: ")
        grup = input("Introduceti grupul din care va face parte: ")
        
        # aici prindem eroarea
        try:
            self.ctrl.adauga_la_agenda(id_cont, nume, nr_tel, grup)
        except ValueError as ex:
            print(ex)
        
    def afiseaza_contacte(self):
        lista = self.ctrl.getAllCtrl() 
        for contact in lista:
            print(contact.getNume(), contact.getNr_telefon()) 
    
    def cautare_numar(self):
        nume= input("Dati un nume dupa care sa se efectueze cautarea: ")
        
        lista = self.ctrl.cautare_numar(nume)
        if lista== []:
            print("Numele nu exista in lista de contacte")
        for c in lista:
            print(c.getId_contact(), c.getNume(), c.getNr_telefon(), c.getGrup())
    
    def contacte_grup(self):
        grup=input("Introduceti un grup: ")
        
        lista = self.ctrl.getAllForCtrl(grup)
        if lista == []:
            print("Nu au fost adaugate contacte pe acest grup")
        for g in lista:
            print(g.getId_contact(), g.getNume(), g.getNr_telefon(), g.getGrup())
        
    def exporta(self):
        nume_fisier = input("Introduceti un  nume de fisier: ")
        grup = input("Introduceti un nume de grup: ")
        self.ctrl.exportCSV(grup,nume_fisier)
            
        
    def start_ui(self):
        while True:
            print("---------------------------------------------")
            print("1. adauga contact")
            print("2. afiseaza toate contactele")
            print("3. cautare dupa nume")
            print("4. tipareste lista de contacte de la un grup")
            print("5. exporta contactele in CSV")
            print("x. exit")
            print("---------------------------------------------")
            
            
            cmd = input("Dati comanda: ")
            print("--------------------")
            if cmd == "1":
                self.adauga()
            if cmd == 'x' :
                break
            if cmd == '2':
                self.afiseaza_contacte()
            if cmd == '3':
                self.cautare_numar()
            if cmd == '4':
                self.contacte_grup()
            if cmd == "5":
                self.exporta()
                
            