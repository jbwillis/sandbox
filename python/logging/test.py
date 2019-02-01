""" logging test program
    Logging is used as an alternative to printing information
"""

import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s: %(message)s', datefmt="%d-%b-%y %H:%M:%S", filename='logTest.log', level=logging.DEBUG)
logging.debug("Verbose debugging log message")
logging.info("Informative log message")
logging.warning("Something might be wrong")
logging.error("Something is wrong")
logging.critical("I can't believe this is still working")

