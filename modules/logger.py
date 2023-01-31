import asyncio
from aiologger import Logger


async def get_app_logger(logger_name):
    logger = Logger.with_default_handlers(name=logger_name)
    logger.setLevel(logging.INFO)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler("x.log")
    file_handler.setLevel(logging.WARNING)
    #await logger.shutdown()
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return(logger)
#loop = asyncio.get_event_loop()
#loop.run_until_complete(get_app_logger())
#loop.close()
#loop.run_forever()


