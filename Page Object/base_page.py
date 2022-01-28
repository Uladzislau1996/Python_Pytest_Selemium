from nturl2path import url2pathname
from webbrowser import BaseBrowser


class BasePage():
    
    def __init__(self, browser, url):
        self.browser = browser 
        self.url = url

    
    def open(self):
        self.browser.get(self.url)