'''start file, gui app, use pyside6'''

import sys,os
from PySide6 import QtWidgets

import modules.logger,modules.gui
logger=modules.logger.get_logger(__name__)
# simple pyside6app
class Ui_MainWindow(QtWidgets.QMainWindow, modules.gui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)  
        self.pushButton_1.clicked.connect(self.btn_all_info)
        print(dir(self.plainTextEdit))
        self.plainTextEdit.appendPlainText("ALL")
        #self.logTextBox.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
        #logging.getLogger().addHandler(logTextBox)
        #logging.g
   
    def btn_all_info(self):
        #data_writter("all_device","to_excel")
        print(1)
        for i in range(99999):
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
    window = Ui_MainWindow()  #
    window.show()  
    app.exec()       

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()



