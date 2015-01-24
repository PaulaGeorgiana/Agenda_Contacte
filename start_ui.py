'''
Created on Jan 22, 2015

@author: Georgiana
'''
from repository.ContactRepo import ContactRepo
from controller.ContactCTRL import ContactCtrl
from ui.consola import Ui
from domain.ContactVal import ContactValidator


val = ContactValidator()
repo = ContactRepo()
ctrl = ContactCtrl(repo,val)
ui = Ui(ctrl)
ui.start_ui()
