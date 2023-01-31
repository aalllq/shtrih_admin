'''start file, gui app, use pyside6'''

import sys,os
from PySide6 import QtWidgets
import lib_api_pyside 
import modules.logger
import logging,aiologger
logger=modules.logger.get_app_logger(__name__)
# simple pyside6app
class lib_api_pyside_App(QtWidgets.QMainWindow, lib_api_pyside.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.btn_all_device_info.clicked.connect(self.btn_all_info)
        self.ALL_textEdit.append("ALL")
        #self.logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        #logging.getLogger().addHandler(logTextBox)
        #logging.g
   
    def btn_all_info(self):
        #data_writter("all_device","to_excel")
        print(1)
        logger.info("Программа завершила работуddd")
    #logging to self.All_plainTextEdit
    
    
    def emit(self, record):
        msg0 = self.format(record)
        self.PVELogs.appendPlainText(msg0)

        msg1 = self.format(record)
        self.PVPLogs.appendPlainText(msg1)
        
    
    
    
    
    
    
    
    
    
    
    
    

''''В этом классе мы будем взаимодействовать с элементами интерфейса,
добавлять соединения и всё остальное, что нам потребуется. Но для начала
нам нужно инициализировать класс при запуске кода. С этим мы разберёмся в функции main():'''      

def main():
    app = QtWidgets.QApplication(sys.argv)  
    window = lib_api_pyside_App()  #
    window.show()  
    app.exec()       

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()



