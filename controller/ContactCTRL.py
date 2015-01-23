'''
Created on Jan 22, 2015

@author: Georgiana
'''
from domain.ContactDom import Contact

class ContactCtrl():
    def __init__(self, repo):
        self.repo = repo
        
    def adauga_la_agenda(self, id_cont, nume, nr_tel, grup):
        c= Contact(id_cont, nume, nr_tel, grup)
        self.repo.adauga(c)
    
    def getAllCtrl(self):
        return self.repo.getAll 