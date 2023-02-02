import logging

logging.basicConfig(filename="D://Logs//Test.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%m/%d/%y/%I:%M:%S %p",
                    level=logging.DEBUG
                    )
logging.info("This is info massage")
logging.debug("This is debug massage")
logging.warning("This is warn massage")
logging.critical("This is critical massage")
logging.error("This is error massage")


# Second Method
logging.basicConfig(filename="D://Python_VS//Demo.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",
                    datefmt="%m/%d/%y/%I:%M:%S %p",
                    )
log = logging.getLogger()
log.setLevel(logging.DEBUG)

log.info("This is info massage")
log.debug("This is debug massage")
log.warning("This is warn massage")
log.critical("This is critical massage")
log.error("This is error massage")