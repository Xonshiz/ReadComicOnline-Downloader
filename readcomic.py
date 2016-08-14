#!/usr/bin/env python
# -*- coding: utf-8 -*-


# pyinstaller.exe --onefile --icon=favicon.ico --version-file=version.txt readcomic.py

# pyinstaller.exe --onefile --icon=favicon.ico readcomic.py

__author__      = "Xonshiz"
__email__ = "Xonshiz@psychoticelites.com"
__website__ = "http://www.psychoticelites.com"
__version__ = "v1.0"
__description__ = "Downloads Issues from http://readcomiconline.to/"
__copyright__ = "None!"





import requests, sys,urllib,urllib2,os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import selenium.webdriver.support.ui as ui
#from bs4 import BeautifulSoup


reload(sys)  
sys.setdefaultencoding('utf-8')

try:
	Series_URL = raw_input('Enter The URL of Series Issue :  ')
except Exception, e:
	#raise e
	print e
	sys.exit()

Edited_Url = str(Series_URL)+'&readType=1'

#url = 'http://readcomiconline.to/Comic/Injustice-Gods-Among-Us-I/Issue-17?id=25075&readType=1'
url = str(Edited_Url)

'''

	There's this annoying Browser Check when you visit to the site. So, I had to wait for an element to load, which denotes that whole page has been rendered.
	It would've taken a long time if I had approached this normally, because downloading all the images would definitely take hell of a time.
	Hence, I used '--load-images=no' command line argument with the PhantomJS to disable to image downloading, which significantly decreases page load time.

'''
driver = webdriver.PhantomJS(service_args=['--load-images=no'])
#options = webdriver.ChromeOptions()
#options.add_extension('adblockpluschrome-1.11.0.1591.crx')
#driver = webdriver.Chrome(chrome_options=options, service_args=["--verbose", "--log-path=Main_Log_File.log"])

driver.get(url)
#driver.implicitly_wait(30)


try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "stSegmentFrame"))
	)
	print 'Downloading the whole page! Will take some time, please don\'t close this script...\n'
	#print 'I\'ve waited long enough'
except Exception, e:
	#raise e
	print e
	pass
finally:
	Source_Code = driver.page_source

	soure_file = open('source.txt','w')
	soure_file.write(Source_Code)
	soure_file.flush()
	soure_file.close()
	driver.quit()

'''

	The link to images was in the source code itself, so all I had to do was parse the page, grab the source code and look for the links in it.
	Example Link looks like : lstImages.push("http://2.bp.blogspot.com/9Y9Cz93VWku6OXRi6l_-EdQyMJa_qqVjrCHMGa7uihY-n5SrA2ZvVOZJo9kzEBoHUSK6d8A16Vgt=s0");
	So, grab it, get the name of the file from the server, remove unnecessary things from file name and save the file

'''


print 'Looking For Links In The Pages!\n'
with open('source.txt') as searchfile:
        for line in searchfile:
            left,sep,right = line.partition('lstImages.push("') #Looking For "Content_id" in the <meta content="http://ib3.huluim.com/video/60585710?region=US&amp;size=600x400" property="og:image"/> (60585710 is Con_id)
            if sep:
            	OG_Title = right.replace('");','')
            	#print OG_Title
            	u = urllib2.urlopen(OG_Title)
            	meta = u.info()['Content-Disposition']
            	File_Name_Final = meta.replace('inline;filename="','').replace('"','').replace('RCO','')
            	print 'Downloading : ',File_Name_Final,'\n'
            	urllib.urlretrieve(OG_Title, File_Name_Final)




os.remove('source.txt')
os.remove('ghostdriver.log')
