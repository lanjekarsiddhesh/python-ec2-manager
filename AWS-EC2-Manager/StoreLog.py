import logging

#create logger
logger = logging.getLogger('aws_manager.log')
logger.setLevel(logging.DEBUG)

#prevent duplicate handlers.
if not logger.handlers:
    file_handler = logging.FileHandler("logs/aws_manager.log")

    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s %(message)s"
    )
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

#LOG Function
def store_log(Msg="Msg",level="info",traceback=False):
    if level == "info":
        logger.info(Msg)
    elif level == "warn":
        logger.warning(Msg)
    elif level == "error" and traceback:
        logger.exception(Msg)   # FULL TRACEBACK
    elif level == "error":
        logger.error(Msg)
    elif level == "critical":
        logger.critical(Msg)
    else:
        logger.debug(Msg)

