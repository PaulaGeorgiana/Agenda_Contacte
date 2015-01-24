'''
Created on 24 ian. 2015

@author: ToTaL
'''

import unittest
from domain.ContactDom import Contact

class TestCase(unittest.TestCase):

    def testContact(self):
        c = Contact("1", "Anca", "123", "job")
        
        self.assertEqual(c.getId_contact(), "1")
        self.assertEqual(c.getNume(), "Anca")
        self.assertEqual(c.getNr_telefon(), "123")
        self.assertEqual(c.getGrup(), "job")
        
    def testContactSetters(self):
        c = Contact("1", "Anca", "123", "job")
        
        c.setNume("Maria")
        self.assertEqual(c.getNume(), "Maria")
        
        c.setNr_telefon("12345")
        self.assertEqual(c.getNr_telefon(), "12345")
        
        c.setGrup("altele")
        self.assertEqual(c.getGrup(), "altele")
        
        
        

if __name__ == '__main__':
    unittest.main()