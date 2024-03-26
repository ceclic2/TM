from formcreator import mainForm

def setDateIn():
    print(mainForm.dateEditIn.dateTime().toString('dd.MM.yyyy'))
    

def setDateOut():
    print(mainForm.dateEditOut.dateTime().toString('dd.MM.yyyy'))