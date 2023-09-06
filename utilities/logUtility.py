import logging
import os
from datetime import datetime
class LogGeneration:
    @staticmethod
    def loggen():
        # logging.basicConfig(
        #     filename=".\\Logs\\automation.log",
        #     filemode='w',
        #     format="%(asctime)s: %(levelname)s: %(message)s",
        #     datefmt="%Y-%m-%d %H:%M:%S",
        # )
        # logger = logging.getLogger()
        # logger.setLevel(logging.DEBUG)
        
        # new method is working for me 
        logger = logging.getLogger()
        fhandler = logging.FileHandler(filename='.\\Logs\\automation.log', mode='a')
        formatter = logging.Formatter('%(asctime)s -  %(levelname)s - %(message)s')
        fhandler.setFormatter(formatter)
        logger.addHandler(fhandler)
        logger.setLevel(logging.INFO)
        return logger