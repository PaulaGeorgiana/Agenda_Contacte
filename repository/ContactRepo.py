'''
Created on Jan 22, 2015

@author: Georgiana
'''

class  ContactRepo():
    def __init__(self, numeFisier):
        # mai iei un parametru, numeFisier si il salvezi in
        # self.numeFisier
 
        self.lista = []
        self.numeFisier = numeFisier
        
    def adauga(self, contact):
        nume = contact.getNume() # numele persoanei de adaugat
        
        for c in self.lista: # ia fiecare contact din lista de contacte
            if c.getNume() == nume: # verifica daca numele e egal cu numele contactului de adaugat
                raise ValueError("Numele exista deja") # daca da, arunca eroare si se opreste executia functiei
        
        self.lista.append(contact)
        self.scrie_fisier()
        
        
    def getAll(self):
        return self.lista
    
    def cauta(self, nume):
        lista_finala=[]
        for element in self.lista:
            if element.getNume()== nume:
                lista_finala.append(element)
        return lista_finala
    
    def getAllFor(self,grup):
        lista_finala=[]
        for element in self.lista:
            if element.getGrup() == grup:
                lista_finala.append(element)
        a= sorted(lista_finala, key=lambda x:x.getNume())
        return a
    
    def citeste_fisier(self):
        try:
            f = open(self.numeFisier, "r")
            f.close()
        except FileNotFoundError:
            # Daca fisierul nu exista, in momentul cand este deschis
            # pentru scriere este creat automat
            f = open(self.numeFisier, "w")
            f.close()
            
        # Cand executia ajunge aici, in mod sigur fisierul exista
        # deci e sigur sa-l deschidem pentru citire
        f = open(self.numeFisier, "r")
        
        # Se citeste continutul fisierului
        continut = f.read()
        linii = continut.split("/n")
        for linie in linii:
            element = linie.split(",")
            self.lista.append(element)
        
        # Am terminat cu fisierul deci il inchidem
        f.close()
    
    def scrie_fisier(self):
        f = open(self.numeFisier, "w")
        for c in self.lista:
            f.write(c.getId_contact() + "," + c.getNume() + "," + c.getNr_telefon() + "," + c.getGrup() + "\n")
        f.close()

        
    # ai nevoie de doua(noua?!)) functii
    # una care citeste din fisier si salveaza in self.lista
    # alta care salveaza self.lista in fisier
    # ambele functii trebuie sa lucreze cu numele de fisier
    # self.numeFisier