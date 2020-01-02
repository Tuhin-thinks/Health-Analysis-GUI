import sys
# import time
from PyQt5.QtWidgets import QApplication, QDialog

from new_biggestUI import *


def check_pulse(pulse_rate):
    comment = '-->------------ Irrelevant Pulse Rate!Please Recheck ---------------'
    if 60 <= pulse_rate <= 100:
        comment = '-->Normal Pulse Rate...'
    if pulse_rate < 60:
        if pulse_rate < 40:
            comment = '-->you are actually going to die,very low pulse rate...'
        else:
            comment = '-->Low Pulse Rate, seek medical attention!'
    if pulse_rate > 100:
        if pulse_rate < 120:
            comment = '-->Pulse rate high seek medical attention,immediately!'
        else:
            comment = '-->Your heart is going to come out of your mouth!,too much high pulse rate...'
    return comment


def check_cholestrol(clstrl): # checked
    comment = ''
    if clstrl < 125:
        comment = '-->Low Cholesterol, seek Medical Attention...'
    elif 125 < clstrl <= 200:
        comment = '-->Optimal Total Cholestrol.'
    elif 200 < clstrl <= 239:
        comment = '-->Boderline High Cholestrol'
    elif 239 < clstrl:
        comment = '-->High Cholestrol, Seek Medical Attention'
    return comment


def check_sugar(bs): # checked
    comment = ''
    if bs > 297:
        comment = '-->Seek Medical Attention, too high PP Blood Sugar level...'
    elif 219 < bs <= 297:
        comment = '-->Seek Medical Attention, High PP Blood Sugar...'
    elif 182 < bs <= 219:
        comment = '-->Consult your Doctor, Boderline high PP Blood Sugar Level...'
    elif 140 < bs <= 182:
        comment = '-->Near Optimal PP sugar level...'
    elif 120 < bs <= 140:
        comment = '-->Optimal PP Sugar Level,no risk!'
    elif 95 < bs <= 120:
        comment = '-->Consult your Doctor,Borderline Low PP Blood sugar level...'
    elif 70 < bs <= 95:
        comment = '-->Seek Medical Attention,Low PP Blood Sugar Level!'
    elif bs < 70:
        comment = '-->Seek Medical Attention,Very low PP Blood Sugar Level!'
    return comment


def check_bp(sys_bp, dias_bp): # checked
    comment = '-->xxxx Irrelevant Blood Pressure Level xxxxx'
    if 120 <= sys_bp <= 129 and 80 <= dias_bp <= 84:
        comment = '-->Perfect Blood Pressure level!'
    elif 130 <= sys_bp <= 139 and 85 <= dias_bp <= 89:
        comment = '-->BP category: Higher Normal.'
    elif 140 <= sys_bp <= 159 and 90 <= dias_bp <= 99:
        comment = '-->You are suffering from "Grade 1 Hyper Tension", Please take care!'
    elif 160 <= sys_bp <= 179 and 100 <= dias_bp <= 109:
        comment = '-->You are suffering from "Grade 2 Hyper Tension", Care is needed !'
    elif sys_bp >= 180 and dias_bp >= 110:
        comment = '-->You are suffering from "Grade 3 Hyper Tension",You need some urgent care!'
    elif sys_bp < 55 and dias_bp < 50:
        comment = '-->You have extremely low BP... Please contact a doctor!'
    elif 180 <= sys_bp and dias_bp < 90:
        comment = '-->You are suffering from "Isolated Systolic Hyper Tension"'
    return comment


class MyForm(QDialog):
    def __init__(self):
        # initialization
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Event Handling
        self.ui.horizontalScrollBarSugarLevel.valueChanged.connect(self.scrolledSugar)
        self.ui.horizontalSliderSystolic.valueChanged.connect(self.scrolled_Systolic)
        self.ui.horizontalSliderDiastolic.valueChanged.connect(self.scrolled_Diastolic)
        self.ui.verticalScrollBarPulseRate.valueChanged.connect(self.scrolled_Pulse)
        self.ui.verticalSliderCholestrol.valueChanged.connect(self.scrolled_cholestrol)
        self.ui.pushButtonAnalyse.clicked.connect(self.all_analyse)
        self.show()

    # managing slots
    def scrolledSugar(self, value):
        self.ui.lineEditSugarLevel.setText(str(value))

    def scrolled_Systolic(self, value):
        self.ui.lineEditBPlevel.setText(f'{value}/{self.ui.horizontalSliderDiastolic.value()}')

    def scrolled_Diastolic(self, value):
        self.ui.lineEditBPlevel.setText(f'{self.ui.horizontalSliderSystolic.value()}/{value}')

    def scrolled_Pulse(self, value):
        self.ui.lineEditPulseRate.setText(str(value))

    def scrolled_cholestrol(self, value):
        self.ui.lineEditCholestrol.setText(str(value))

    def all_analyse(self):
        try:
            bp = str(self.ui.lineEditBPlevel.text())
            sys_bp = bp.split('/')[0]
            dias_bp = bp.split('/')[1]
        except IndexError:
            sys_bp = 'null'
            dias_bp = 'null'

        bs = str(self.ui.lineEditSugarLevel.text())
        self.ui.plainTextEditResult.setPlainText(str('Collecting analysis data, wait...\n'))
        # time.sleep(1.0)
        try:
            comment_bp = check_bp(int(sys_bp), int(dias_bp))  # checking BP
        except ValueError:
            comment_bp = '--null--'
        self.ui.plainTextEditResult.appendPlainText(comment_bp)
        try:
            comment_sugar = check_sugar(int(self.ui.lineEditSugarLevel.text()))  # checking blood sugar
        except ValueError:
            comment_sugar = '--null--'
        self.ui.plainTextEditResult.appendPlainText(comment_sugar)
        try:
            comment_cholestrol = check_cholestrol(int(self.ui.lineEditCholestrol.text()))
        except ValueError:
            comment_cholestrol = '--null--'
        self.ui.plainTextEditResult.appendPlainText(comment_cholestrol)
        try:
            comment_pulserate = check_pulse(int(self.ui.lineEditPulseRate.text()))
        except ValueError:
            comment_pulserate = '--null--'
        self.ui.plainTextEditResult.appendPlainText(comment_pulserate)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())
