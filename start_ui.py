'''
Created on Jan 22, 2015

@author: Georgiana
'''
from repository import ContactRepo
from controller.ContactCTRL import ContactCtrl
from ui.consola import Ui

repo = ContactRepo()
ctrl = ContactCtrl(repo)
ui = Ui(ctrl)
ui.start_ui()