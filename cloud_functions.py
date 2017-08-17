#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlalchemy


def add(x, y):
    return x + y

def get_config():
    # config variable is a dict that is loaded into the cloud_functions file at runtime
    return config

def get_config_keys():
    return config.keys()

def get_config_values():
    return config.values()

def log_something():
    logger.debug('this is the debug message')
    logger.info('this is the info message')
    logger.error('this is the error message')
    logger.exception('this is the exception message')
    logger.warning('this is the warning message')
    logger.critical('this is the critical message')


def connect(user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)
    if con:
        con = 'connected'
    if meta:
        meta = 'meta'

    return con, meta

