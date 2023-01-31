import logging,arrow
from logging.handlers import RotatingFileHandler
start_time=arrow.now().format("YY-MM-DD")

def get_logger(name):
    """получает __name__  возвращает logger"""
    log_file_name=f"log/{start_time}.log"
    logger= logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    #file
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.DEBUG)
    #stdout
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    #formatter
    _log_format = f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    formatter = logging.Formatter(_log_format)
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    #add handler
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    #rotate
    rotate_handler = RotatingFileHandler(log_file_name,maxBytes=(5*1024)*1024,backupCount=10)
    logger.addHandler(rotate_handler)
    return logger