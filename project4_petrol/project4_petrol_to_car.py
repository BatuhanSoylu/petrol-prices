from PyQt5 import QtWidgets,uic
import sys
import os
from project4_petrol_to_car_functions import *
class petrol(QtWidgets.QWidget):
    #os.system("start EXCEL.EXE petrolpricesof{}".format(country)) #open specific excel file

    def __init__(self):
        super(petrol, self).__init__()
        uic.loadUi(r'C:\Users\Batu1\PycharmProjects\pythonProject1\Quizzes\OOP\project4_petrol\petrol_prices_gui.ui',self)
        self.pushButton.clicked.connect(self.show_prices)
        self.pushButton.clicked.connect(self.total_price)
        #self.checkBox.stateChanged.connect(self.dollar)
        #self.checkBox_2.stateChanged.connect(self.euro)

    def show_prices(self):
        if self.radioButton.isChecked() == True and self.radioButton_2.isChecked() ==False:  #super95
            country=self.comboBox.currentText()
            petrol_countries_build(country)
            super95=building_super_95_prices(country)
            dates=building_petrol_dates(country)
            if self.checkBox.isChecked()==True and self.checkBox_2.isChecked()==False:
                os.system("start EXCEL.EXE petrolpricesof{}".format(country)) #open specific excel file
            elif self.checkBox.isChecked()==False and self.checkBox_2.isChecked()==True:
                building_graph(super95,dates)


        elif self.radioButton.isChecked() == False and self.radioButton_2.isChecked() == True:  #gas oil
            country=self.comboBox.currentText()
            petrol_countries_build(country)
            gas_oil=building_gas_oil_prices(country)
            dates=building_petrol_dates(country)
            if self.checkBox.isChecked()==True and self.checkBox_2.isChecked()==False:
                os.system("start EXCEL.EXE petrolpricesof{}".format(country)) #open specific excel file
            elif self.checkBox.isChecked()==False and self.checkBox_2.isChecked()==True:
                building_graph(gas_oil,dates)

        elif self.radioButton_3.isChecked()==True and self.radioButton_2.isChecked()==False and self.radioButton.isChecked()==False:#both
            country=self.comboBox.currentText()
            petrol_countries_build(country)
            dates=building_petrol_dates(country)
            super95=building_super_95_prices(country)
            gas_oil=building_gas_oil_prices(country)
            if self.checkBox.isChecked()==True and self.checkBox_2.isChecked()==False:
                os.system("start EXCEL.EXE petrolpricesof{}".format(country)) #open specific excel file
            elif self.checkBox.isChecked()==False and self.checkBox_2.isChecked()==True:
                building_graph_all(super95,gas_oil,dates)


    def total_price(self):
        pass




app = QtWidgets.QApplication(sys.argv)
window = petrol()
window.show()
app.exec_()
