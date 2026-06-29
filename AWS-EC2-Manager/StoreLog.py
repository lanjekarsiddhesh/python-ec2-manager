import logging

#LOG Function
def store_log(Filename='logs/aws_manager.log',Msg="Msg",level="info"):
    logging.basicConfig(
        filename=Filename,
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )
    if level == "info":
        logging.info(Msg)
    elif level == "warn":
        logging.warning(Msg)
    elif level == "error":
        logging.error(Msg)
    elif level == "critical":
        logging.critical(Msg)
    else:
        logging.debug(Msg)