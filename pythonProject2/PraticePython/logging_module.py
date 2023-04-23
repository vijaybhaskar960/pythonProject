'''
1. Using logging module we can log based on severity level.
2. By default, there are 5 standard levels indicating the severity of events.
3. Log levels are ==>  INFO, DEBUG, WARNING, ERROR, CRITICAL
4. The default level is WARNING
'''


import logging

logging.basicConfig(filename="",
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
logging.basicConfig(filename="",
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