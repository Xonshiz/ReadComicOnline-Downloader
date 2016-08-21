#!/usr/bin/env python
# -*- coding: utf-8 -*-


# pyinstaller.exe --onefile --icon=favicon.ico --version-file=version.txt readcomic.py

# pyinstaller.exe --onefile --icon=favicon.ico readcomic.py

__author__      = "Xonshiz"
__email__ = "Xonshiz@psychoticelites.com"
__website__ = "http://www.psychoticelites.com"
__version__ = "v2.0"
__description__ = "Downloads Issues from http://readcomiconline.to/"
__copyright__ = "None!"

# A big thanks to 'c17r' for his help on getting the Regex checking done. More Info : https://www.reddit.com/r/learnpython/comments/4yq7it/regex_clashing_as_substring_regexes/d6pr39n

"""
#############################################################################################################
# 										FEATURES :															#
#############################################################################################################
#																											#
# 1.) Downloads all the Issues available for a series. 														#
# 2.) Puts the files in corresponding directories after downloading the files. 								#
# 3.) Downloads Hight Quality images. 																		#
# 4.) Skips the file if it already exists in the path. 														#
#																											#
#############################################################################################################
# 										FUTURE FEATURES :													#
#############################################################################################################
#																											#
# 1.) Download the series in chronological order. (Currently Downloads the latest Issue Uploaded on site).  #
# 2.) Option to download Low Quality Images. 																#
# 3.) Option to download particular Issues from a series. 													#
#																											#
#############################################################################################################
# 										CHANGELOG :															#
#############################################################################################################
#																											#
# 1.) Re-Wrote the whole script for better understanding and flow. 											#
# 2.) Downloading of all the Issues available for a series. 												#
# 3.) Corresponding Directories for the series and an Issue. 												#
# 4.) File skipping, if the file already exists. 															#
# 5.) Error Log File creation. 																				#
#																											#
#############################################################################################################	

"""




import requests, sys,urllib,urllib2,os,re,shutil
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


'''

	There's this annoying Browser Check when you visit to the site. So, I had to wait for an element to load, which denotes that whole page has been rendered.
	It would've taken a long time if I had approached this normally, because downloading all the images would definitely take hell of a time.
	Hence, I used '--load-images=no' command line argument with the PhantomJS to disable to image downloading, which significantly decreases page load time.

'''

def Url_Fetching():
	try:
		Series_URL = raw_input('Enter The URL of Series Issue :  ')
	except Exception, e:
		#raise e
		print e
		sys.exit()
	
	print '{:^80}'.format('################################################')
	print '{:^80}'.format('Author : Xonshiz')
	print '{:^80}'.format('################################################')
	
	#Series_Regex = re.compile('https?://(?:(?P<prefix>www\.)?readcomiconline.to/Comic/)[A-Za-z\-\d]+$')
	Issue_Regex = re.compile('https?://(?P<host>[^/]+)/Comic/(?P<comic>[\d\w-]+)(?:/Issue-)?(?P<issue>\d+)?')

	lines = Series_URL.split('\n')
	for line in lines:
		found = re.search(Issue_Regex, line)
		if found:
			match = found.groupdict()
			if match['issue']:
				#print('Issue url: {}'.format(match))
				Edited_Url = str(Series_URL)+'&readType=1'
				url = str(Edited_Url)
				Single_Issue(url)

			else:
				#print('Series url: {}'.format(match))
				#Edited_Url = str(Series_URL)
				url = str(Series_URL)
				driver = create_driver()
				Whole_Series(driver,url)

		if not found:
			print 'Please Check Your URL one again!'
			sys.exit()

def create_driver():
	driver = webdriver.PhantomJS(service_args=['--load-images=no'])
	return driver

def Single_Issue(url):
	#print url
	
	
	browser = webdriver.PhantomJS(service_args=['--load-images=no'])
	browser.get(url)
	try:
		element = WebDriverWait(browser, 10).until(
			EC.presence_of_element_located((By.ID, "stSegmentFrame"))
		)
		#print 'Downloading the whole page! Will take some time, please don\'t close this script...\n'
		#print 'I\'ve waited long enough'
	except Exception, e:
		#raise e
		print e
		pass
	finally:
		Source_Code = browser.page_source

		soure_file = open('source.txt','w')
		soure_file.write(Source_Code)
		soure_file.flush()
		soure_file.close()
		browser.quit()
	
	'''

		The link to images was in the source code itself, so all I had to do was parse the page, grab the source code and look for the links in it.
		Example Link looks like : lstImages.push("http://2.bp.blogspot.com/9Y9Cz93VWku6OXRi6l_-EdQyMJa_qqVjrCHMGa7uihY-n5SrA2ZvVOZJo9kzEBoHUSK6d8A16Vgt=s0");
		So, grab it, get the name of the file from the server, remove unnecessary things from file name and save the file

	'''
	
	#print 'Looking For Links In The Pages!\n'
	with open('source.txt') as searchfile:
			for line in searchfile:
				left,sep,right = line.partition('meta name="keywords" content="read') 
				if sep:
					#print sep
					OG_Title = right.split('#')
					#print OG_Title,'\n'
					Raw_Issue_Number = str(OG_Title[-1]).replace('"','').replace('>','').strip()
					Issue_Number = 'Issue '+str(Raw_Issue_Number)
					#print Issue_Number
	searchfile.close()
	
	with open('source.txt') as searchfile:
			for line in searchfile:
				left,sep,right = line.partition('meta name="description" content=') 
				if sep:
					#print sep
					OG_Title = right.split('Issue')
					Series_Name = str(OG_Title[0]).replace('Read','').replace('"','').strip().encode('utf-8')
					print '\nSeries Name : ', Series_Name,' -',Issue_Number,'\n'
					print '#####################################\n'
					Raw_File_Directory = str(Series_Name)+'/'+str(Issue_Number)
					File_Directory = re.sub('[^A-Za-z0-9\-\.\'\#\/ ]+', '', Raw_File_Directory) # Fix for "Special Characters" in The series name
					#print File_Directory
					Directory_path = os.path.normpath(File_Directory)
					#print Directory_path
					
	searchfile.close()

	with open('source.txt') as searchfile:
			for line in searchfile:
				left,sep,right = line.partition('lstImages.push("') 
				if sep:
					OG_Title = right.replace('");','')
					#print OG_Title
					if not os.path.exists(File_Directory):
						os.makedirs(File_Directory)
					u = urllib2.urlopen(OG_Title)
					meta = u.info()['Content-Disposition']
					File_Name_Final = meta.replace('inline;filename="','').replace('"','').replace('RCO','')
					File_Check_Path = str(Directory_path)+'/'+str(File_Name_Final)
					if os.path.isfile(File_Check_Path):
						print 'File Exist! Skipping ',File_Name_Final,'\n'
						pass
					if not os.path.isfile(File_Check_Path):	
						print 'Downloading : ',File_Name_Final
						urllib.urlretrieve(OG_Title, File_Name_Final)
						File_Path = os.path.normpath(File_Name_Final)
						#print Directory_path,'\n',File_Path
						try:
							shutil.move(File_Path,Directory_path)

						except Exception, e:
							#raise e
							print e,'\n'
							os.remove(File_Path)
							pass	

	print '#####################################\n'					
	
	os.remove('source.txt')
	os.remove('ghostdriver.log')
	#os.remove('source2.txt')

def Whole_Series(driver,url):
	#print '\nDownloading Whole Series'
	#print url
	driver.get(url)
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

		soure_file = open('source2.txt','w')
		soure_file.write(Source_Code)
		soure_file.flush()
		soure_file.close()
		driver.quit()
	
	driver.quit()
	try:
		os.remove('.Temp_File')
	except Exception, e:
		#raise e
		pass
	with open('source2.txt') as searchfile:
		with open('.Temp_File','a') as Temp_File_variable:
			for line in searchfile:
				left,sep,right = line.partition('title="Read ') # Extra Space to make it more precise and drop the readcomiconline.to link
				if sep:
					OG_Title = left.split('"')
					#print OG_Title[1]
					Raw_Issue_Links = OG_Title[1].strip()
					Issue_Links = 'http://readcomiconline.to'+str(Raw_Issue_Links)
					#print Issue_Links
					Temp_File_variable.write(str(Issue_Links)+'\n')
					Temp_File_variable.flush()
		Temp_File_variable.close()			
	with open('.Temp_File','r') as Link_File:
		for line in Link_File:
			url = str(line)
			#print url
			Single_Issue(url)

	os.remove('source2.txt')		
		

	
	#Remove the .temp_fle so that it doesn't append to the old data!	
					

try:
	Url_Fetching()
except Exception, e:
	#raise e
	print e
	sys.exit()


#url = 'http://readcomiconline.to/Comic/Injustice-Gods-Among-Us-I'	
#url = 'http://readcomiconline.to/Comic/Injustice-Gods-Among-Us-I/Issue-36?id=25113'
