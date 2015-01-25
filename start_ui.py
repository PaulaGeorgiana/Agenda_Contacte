'''
Created on Jan 22, 2015

@author: Georgiana
'''
from repository.ContactRepo import ContactRepo
from controller.ContactCTRL import ContactCtrl
from ui.consola import Ui
from domain.ContactVal import ContactValidator


val = ContactValidator()
# aici pur si simplu alegi un nume de fisier
numeFisier = "contacte.txt"
repo = ContactRepo(numeFisier)
ctrl = ContactCtrl(repo,val)
ui = Ui(ctrl)
ui.start_ui()
