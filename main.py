from formcreator import mainForm, dialogFormTask, dialogFormFinance, app
from Flags import Flags
from MainForm.onClickCalendar import onClickCalendar
from MainForm.CheckBoxClick import ChecBoxClick
from MainForm.DatePeriod import setDateIn, setDateOut
from MainForm.changeRecords import AddRecordClick, DelRecordClick, EditRecordClick
from DialogFormTask.DialogFormTaskClose import DialogFormTaskClose
from DialogFormFinance.DialogFormFinanceClose import DialogFormFinanceClose

flags = Flags()

mainForm.calendarWidget.clicked.connect(onClickCalendar)
mainForm.checkBoxFilterDate.clicked.connect(ChecBoxClick)
mainForm.dateEditIn.dateChanged.connect(setDateIn)
mainForm.dateEditOut.dateChanged.connect(setDateOut)
mainForm.ButtonAddRecord.clicked.connect(AddRecordClick)
mainForm.ButtonDeleteRecord.clicked.connect(DelRecordClick)
mainForm.ButtonEditRecord.clicked.connect(EditRecordClick)
dialogFormTask.ButtonCancel.clicked.connect(DialogFormTaskClose)
dialogFormFinance.ButtonCancel.clicked.connect(DialogFormFinanceClose)

app.exec()