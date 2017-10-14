#!/bin/python3
# -*- coding: utf-8 -*-

import sys
from ftplib import FTP


class ftpconnect(object):
    """docstring forftpconnect."""
    def __init__(self, server, username='anonymous', password='', port='21'):
        self.HOST = server
        self.PORT = port
        if self.connect():
            sys.exit("connect fail")

    def connect(self):
        try:
            self.CON = FTP.connect(host=self.HOST, port=self.PORT)
            return True
        except Exception:
            return False

    def login(self, username, password):
        try:
            self.LOGIN = FTP.login(user=username, passwd=password)
            return True
        except Exception:
            return False
