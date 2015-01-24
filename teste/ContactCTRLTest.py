'''
Created on 24 ian. 2015

@author: ToTaL
'''
import unittest
from domain.ContactVal import ContactValidator
from repository.ContactRepo import ContactRepo
from domain.ContactDom import Contact
from controller.ContactCTRL import ContactCtrl

class TestCase(unittest.TestCase):

    def testContactCTRL(self):
        val = ContactValidator()
        repo = ContactRepo()
        ctr = ContactCtrl(repo, val)
        
        self.assertRaises(ValueError, ctr.adauga_la_agenda,"1","Paul","123","")
        
        ctr.adauga_la_agenda("1","Paul","123","job")
        self.assertRaises(ValueError, ctr.adauga_la_agenda, "2", "Paul", "123", "job")

if __name__ == '__main__':
    unittest.main()