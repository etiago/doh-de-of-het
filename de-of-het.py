#encoding=utf8
import os
import re
from urllib.parse import quote
from wox import Wox,WoxAPI
from bs4 import BeautifulSoup
import requests

#Your class must inherit from Wox base class https://github.com/qianlifeng/Wox/blob/master/PythonHome/wox.py
#The wox class here did some works to simplify the communication between Wox and python plugin.
class Main(Wox):
    def get_lidwoord(self, woord):
        r = requests.get('https://www.welklidwoord.nl/{}'.format(woord))
        bs = BeautifulSoup(r.text, "html.parser")
        return bs.find('div',{'id': 'content'}).find('h1').find('span').text;
            
    # A function named query is necessary, we will automatically invoke this function when user query this plugin
    def query(self,query):
        lidwoord = self.get_lidwoord(query)
        result = {"Title": "De Of Het?",
                  "IcoPath":"Images/doh.gif",
                  "SubTitle": "Lidwoord for {} is {}".format(query, lidwoord)}
        
        return [result]
        
#Following statement is necessary
if __name__ == "__main__":
    Main()
