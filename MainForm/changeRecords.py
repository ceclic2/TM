from PyQt5 import QtCore
from PyQt5.QtCore import QDate
from formcreator import mainForm, dialogFormTask, dialogTaskWindow, dialogFormFinance, dialogFinanceWindow

def AddRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(_translate('DialogFormTask', 'добавление записи'))
        dialogFormTask.dateEditTask.setDate(QDate.currentDate())
        dialogFormTask.timeEditStart.setTime(QtCore.QTime.currentTime())
        dialogTaskWindow.show()
    else:
        dialogFormFinance.CaptionLabel.setText(_translate('DialogFormFinance', 'добавление записи'))
        dialogFinanceWindow.show()

def DelRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(_translate('DialogFormTask', 'удаление записи'))
        dialogTaskWindow.show()
    else:
        dialogFormFinance.CaptionLabel.setText(_translate('DialogFormFinance', 'удаление записи'))
        dialogFinanceWindow.show()

def EditRecordClick():
    _translate = QtCore.QCoreApplication.translate
    if mainForm.tabWidget.currentIndex() == 0:
        dialogFormTask.CaptionLabel.setText(_translate('DialogFormTask', 'изменение записи'))
        dialogTaskWindow.show()
    else:
        dialogFormFinance.CaptionLabel.setText(_translate('DialogFormFinance', 'изменение записи'))
        dialogFinanceWindow.show()
