'''
Created on 24 ian. 2015

@author: ToTaL
'''

import unittest
from repository.ContactRepo import ContactRepo
from domain.ContactDom import Contact

class TestCase(unittest.TestCase):

    def testMet1(self):
        repo= ContactRepo()
        
        contact = Contact("1","Paul","123","job")
        repo.adauga(contact)
        
        self.assertRaises(ValueError, repo.adauga, Contact("2", "Paul", "456", "familie"))
        lista=repo.getAll()
        
        self.assertEqual(len(lista), 1)
        

if __name__ == '__main__':
    unittest.main()