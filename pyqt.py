#!/usr/bin/python

import sys
  
from PyQt5.QtGui import *  
from PyQt5.QtCore import *  
from PyQt5.QtWebKit import *
from PyQt5.QtWebKitWidgets import *
from PyQt5.QtWidgets import QApplication 
from lxml import html
from bs4 import BeautifulSoup 

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

url = 'http://www.boards.ie'  
r = Render(url)  
result = r.frame.toHtml()
soup = BeautifulSoup(result, "lxml")
links = soup.find_all("a")
for link in links:
	print("<a href=%s>%s</a>" %(link.get("href"),link.text))
