'''
Created on 24 ian. 2015

@author: ToTaL
'''

import unittest
from domain.ContactVal import ContactValidator
from domain.ContactDom import Contact

class TestCase(unittest.TestCase):
    
    def testMet1(self):
        val = ContactValidator()
        
        c = Contact("1","","123","job")
        self.assertRaises(ValueError, val.Contact_Val, c)
        
        c = Contact("1","Paul","","job")
        self.assertRaises(ValueError, val.Contact_Val, c)
        
        c = Contact("1","Paul","123","te_iubesc_Paul!_(multumesc ca esti mereu alaturi de mine)")
        self.assertRaises(ValueError, val.Contact_Val, c)
        
if __name__ == '__main__':
    unittest.main()