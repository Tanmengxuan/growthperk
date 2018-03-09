from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.command import Command

class PersistentWebdriver (webdriver.Remote):
    
    def __init__(self, session_id=None, browser_name=''):
        command_executor='http://localhost:4444/wd/hub'
        platform = version = ''
        javascript_enabled = True

        self.command_executor = command_executor
        if type(self.command_executor) is str:
            self.command_executor = RemoteConnection(command_executor)
        
        self.command_executor._commands['GET_SESSION'] = ('GET', '/session/$sessionId')
        
        self.session_id = session_id
        self.capabilities = {}
        self.error_handler = ErrorHandler()

        if session_id:
            self.connect_to_session(
                browser_name=browser_name,
                platform=platform,
                version=version,
                javascript_enabled=javascript_enabled
            )
        else:
            self.start_session(
                browser_name=browser_name,
                platform=platform,
                version=version,
                javascript_enabled=javascript_enabled
            )
            
    def connect_to_session(self, browser_name, platform, version, javascript_enabled):
        response =  self.execute('GET_SESSION', {
            'desiredCapabilities': {
                'browserName': browser_name,
                'platform': platform or 'ANY',
                'version': version or '',
                'javascriptEnabled': javascript_enabled
            },
            'sessionId': self.session_id
        })
        self.session_id = response['sessionId']
        self.capabilities = response['value']







#a = PersistentWebdriver()

from selenium import webdriver
driver = webdriver.Chrome(executable_path=r"/home/mostafa/chromedriver") #I actually used the chromedriver and did not test firefox, but it should work.
#driver = webdriver.Firefox()

#url = driver.command_executor._url  
#session_id = driver.session_id
#driver = webdriver.Remote(command_executor=url,desired_capabilities={})
#driver.session_id = session_id

#class SessionRemote(webdriver.Remote):
#    def start_session(self, desired_capabilities, browser_profile=None):
#        # Skip the NEW_SESSION command issued by the original driver
#        # and set only some required attributes
#        self.w3c = True

import time

profile_link=[ "https://sg.linkedin.com/in/ashley-chua", "https://www.linkedin.com/in/johnsmith1","https://sg.linkedin.com/in/garyheng"]

for i in profile_link:
    #driver = SessionRemote(command_executor=profile_link, desired_capabilities={})
    #session_id = driver.session_id
    driver.get(i)
    time.sleep(20)
    html=driver.page_source
    #print html
    soup=BeautifulSoup(html, "lxml") #specify parser or it will auto-select for you
    
    name = soup.findAll('h1',{'class':'pv-top-card-section__name Sans-26px-black-85%'})[0]
    name = name.text

    title = soup.findAll('h2',{'class':'pv-top-card-section__headline Sans-19px-black-85%'})[0]
    title = title.text

    coy = soup.findAll('h3',{'class':'pv-top-card-section__company Sans-17px-black-70% mb1 inline-block'})[0]
    coy = coy.text

    print name
    print title
    print coy
    print "\n"
