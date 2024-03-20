import os
import sys
import youtube_dl
from PyQt5 import QtCore, QtGui, QtWidgest

class downloader(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)