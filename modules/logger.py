# Path: modules/logger.py
import logging,arrow
from logging.handlers import RotatingFileHandler
from modules import files_worker

start_time=arrow.now().format("YY-MM-DD")
def get_logger(name):
    
    """получает __name__  возвращает logger"""
    files_worker.make_dir(["log"])
    log_file_name=f"log/{start_time}.log"
    logger= logging.getLogger(name)
    #formatter
    _log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    formatter = logging.Formatter(_log_format)
    logger.setLevel(logging.DEBUG)
    #file
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    
    
    #stdout
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    #rotate
    rotate_handler = RotatingFileHandler(log_file_name,maxBytes=(5*1024)*1024,backupCount=10)
   # logger.addHandler(rotate_handler)
   # gui_handler = Ui_MainWindow.return_gui_handler()
   # logger.addHandler(gui_handler)
    return logger

#make gui logger handler

class GuiLogger(logging.Handler):
    def emit(self, record):
        self.edit.appendPlainText(self.format(record))  # implementation of append_line omitted


# Path: modules/gui.py
