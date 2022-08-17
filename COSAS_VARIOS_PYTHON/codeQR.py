from tkinter import Scale
import pyqrcode
from pyqrcode import QRCode

url = pyqrcode.create("https://www.jw.org/finder?wtlocale=S&docid=501100044&srcid=share")

url.svg('jw.svg', scale=8)
