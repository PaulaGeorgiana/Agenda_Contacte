'''
Created on Jan 22, 2015

@author: Georgiana
'''

class Ui():
    def __init__(self, ctrl):
        self.ctrl = ctrl
        
    def adauga(self):
        id_cont= int(input("Introduceti id-ul persoanei: "))
        nume= input("Introduceti numele: ")
        nr_tel= int(input("Introduceti numarul de telefon: "))
        grup= input("Introduceti grupul din care va face parte: ")
        
        self.ctrl.adauga_la_agenda(id_cont, nume, nr_tel, grup)
    def start_ui(self):
        while True:
            print("1. adauga contact")
            print("x. exit")
            
            cmd= input("Dati comanda: ")
            
        if cmd == 1:
            self.adauga()
        if cmd == 'x' :
            break
