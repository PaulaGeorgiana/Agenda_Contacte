'''
Created on Jan 22, 2015

@author: Georgiana
'''

class  ContactRepo():
    def __init__(self):
        self.lista = []
        
    def adauga(self, contact):
        self.lista.append(contact)
        
    def getAll(self):
        return self.lista
    
