from bs4 import BeautifulSoup

from selenium import webdriver

from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.command import Command
import time
from selenium import webdriver
import csv
import random

#driver = webdriver.Chrome(executable_path=r"/home/mostafa/chromedriver") #I actually used the chromedriver and did not test firefox, but it should work.
driver = webdriver.Firefox()

#url = driver.command_executor._url  
#session_id = driver.session_id
#driver = webdriver.Remote(command_executor=url,desired_capabilities={})
#driver.session_id = session_id

#class SessionRemote(webdriver.Remote):
#    def start_session(self, desired_capabilities, browser_profile=None):
#        # Skip the NEW_SESSION command issued by the original driver
#        # and set only some required attributes
#        self.w3c = True
csvpath = '/home/mostafa/Desktop/growthperk/models/BDM_Boston_0416.csv'
outFile = open(csvpath,"wb")
csvFile = csv.writer(outFile, delimiter='\t') 
csvFile.writerow(["name", "company", "title", "url"])



file_path = 'outputfile-BDM_Boston.txt' #length:854
count = 650 
with open(file_path) as f:
    profile_link = f.readlines()


#profile_link=[ "https://sg.linkedin.com/in/ashley-chua", "https://www.linkedin.com/in/johnsmith1","https://sg.linkedin.com/in/garyheng"]

for i in profile_link[650:700]:
    #driver = SessionRemote(command_executor=profile_link, desired_capabilities={})
    #session_id = driver.session_id
    try:
        print count
        count += 1
        sleeptime = random.randint(10,200)
        print "please wait for: " + str(sleeptime)
        print i
        driver.get(i)
        time.sleep(sleeptime)
        html=driver.page_source
        #print html
        soup=BeautifulSoup(html, "lxml") #specify parser or it will auto-select for you
        
        name = soup.findAll('h1',{'class':'pv-top-card-section__name Sans-26px-black-85%'})[0]
        name = name.text

        title = soup.findAll('h2',{'class':'pv-top-card-section__headline Sans-19px-black-85%'})[0]
        title = title.text

        coy = soup.findAll('h3',{'class':'pv-top-card-section__company Sans-17px-black-70% mb1 inline-block'})[0]
        coy = coy.text
        coy = " ".join(coy.split())

        print name
        print title
        print coy
        print "\n"
        
        csvFile.writerow([name, coy, title, i])
    except:
        continue

outFile.close()
