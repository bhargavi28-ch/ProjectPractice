import logging


def getlogger():

    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.file')
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)


    logger.debug("A debug statement is executed")
    logger.info("Information statement")
    logger.warning("Something is in warning")
    logger.error("Major error has happened")
    logger.critical("Critical issue")
