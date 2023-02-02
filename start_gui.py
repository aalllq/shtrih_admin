'''start file, gui app, use pyside6'''

import sys,os
from PySide6 import QtWidgets
from modules import gui,http_sender

import modules.http_sender
from modules import logger
logger = modules.logger.get_logger(__name__)

class main_app(QtWidgets.QMainWindow, modules.gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
   
        self.pushButton_1.clicked.connect(self.btn_all_info)
        self.plainTextEdit.appendPlainText("ALL")
        #####write log to gui
        h = modules.logger.GuiLogger()
        h.edit = self.plainTextEdit
        logger.addHandler(h)
        
    def btn_all_info(self):
        print(http_sender.sync_send(["https://google.com"],"GET",data=None,header=None,json=True))
        #data_writter("all_device","to_excel
        for i in range(1):
            logger.info("Программа завершила работуddd")
            


def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = main_app()  #
    window.show()  
    app.exec()       

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем 
    main()  # то запускаем функцию main()

