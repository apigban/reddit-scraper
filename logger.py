#!/usr/bin/env python3.7
import logging

def logDefault():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

# create a file handler
    handler = logging.FileHandler('hello.log')
    handler.setLevel(logging.INFO)

# create a logging format
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

# add the handlers to the logger
    :wqlogger.addHandler(handler)
