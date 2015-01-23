'''
Created on Jan 22, 2015

@author: Georgiana
'''

class  ContactRepo():
    def __init__(self):
        self.lista = []
        
    def adauga(self, contact):
        nume = contact.getNume() # numele persoanei de adaugat
        
        for c in self.lista: # ia fiecare contact din lista de contacte
            if c.getNume() == nume: # verifica daca numele e egal cu numele contactului de adaugat
                raise ValueError("Numele exista deja") # daca da, arunca eroare si se opreste executia functiei
        
        self.lista.append(contact)
        
    def getAll(self):
        return self.lista
    
    def cauta(self, nume):
        lista_finala=[]
        for un_nume in self.lista:
            if un_nume.getNume()== nume:
                lista_finala.append(un_nume)
        return lista_finala