from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

MainForm, Window = uic.loadUiType("MainForm.ui")
DialogFormTask, DialogTaskWindow= uic.loadUiType("DialogFormTask.ui")
DialogFormFinance, DialogFinanceWindow= uic.loadUiType("DialogFormFinance.ui")


app=QApplication([])
mainWindow=Window()
dialogTaskWindow=DialogTaskWindow()
dialogFinanceWindow=DialogFinanceWindow()

mainForm=MainForm()
dialogFormTask=DialogFormTask()
dialogFormFinance=DialogFormFinance()


mainForm.setupUi(mainWindow)
dialogFormTask.setupUi(dialogTaskWindow)
dialogFormFinance.setupUi(dialogFinanceWindow)

mainWindow.show()
