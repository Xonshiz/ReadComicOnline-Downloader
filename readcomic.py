#!/usr/bin/env python
# -*- coding: utf-8 -*-


# pyinstaller.exe --onefile --icon=favicon.ico --version-file=version.txt readcomic.py

# pyinstaller.exe --onefile --icon=favicon.ico readcomic.py

__author__      = "Xonshiz"
__email__ = "Xonshiz@psychoticelites.com"
__website__ = "http://www.psychoticelites.com"
__version__ = "v2.2"
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
# 5.) Option to choose Qulity of Images. 																	#
# 6.) Option to download Latest or Older releases.	 														#
# 7.) Option to download particular Issues from a series. 													#
#																											#
#############################################################################################################
# 										FUTURE FEATURES :													#
#############################################################################################################
#																											#
# 1.) Error Log File creation. 																				#
#																											#
#############################################################################################################
# 										CHANGELOG :															#
#############################################################################################################
#																											#
# 1.) Re-Wrote the whole script for better understanding and flow. 											#
# 2.) Downloading of all the Issues available for a series. 												#
# 3.) Corresponding Directories for the series and an Issue. 												#
# 4.) File skipping, if the file already exists. 															#
# 5.) Option to choose Qulity of Images. 																	#
# 6.) Option to download Latest or Older releases.	 														#
# 6.) Script won't break on HTTP errors.(Thanks to @Efreak)	 												#
# 6.) Weird File name Fix and some Minor Bug Fix	 														#
# 7.) Annual Issues are now downloadable,			 														#
# 8.) Option to download particular Issues from a series. 													#
#																											#
#############################################################################################################	

"""




import requests, sys,urllib,urllib2,os,re,shutil,ConfigParser
from urllib2 import URLError
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
	
	print '\n'
	print '{:^80}'.format('################################################')
	print '{:^80}'.format('Author : Xonshiz')
	print '{:^80}'.format('################################################\n')
	

	try:
		Series_URL = raw_input('Enter The URL of Series Issue :  ')
	except Exception, e:
		#raise e
		print e
		sys.exit()
	
	#Series_Regex = re.compile('https?://(?:(?P<prefix>www\.)?readcomiconline.to/Comic/)[A-Za-z\-\d]+$')
	Issue_Regex = re.compile('https?://(?P<host>[^/]+)/Comic/(?P<comic>[\d\w-]+)(?:/Issue-)?(?P<issue>\d+)?')
	Annual_Regex = re.compile('https?://(?P<host>[^/]+)/Comic/(?P<comic>[\d\w-]+)(?:/Annual-)?(?P<issue>\d+)?')
	#Issue_Regex = re.compile('https?://(?P<host>[^/]+)/Comic/(?P<comic>[\d\w-]+)(?:/Issue-)?|(?:/Annual-)?(?P<issue>\d+)?')

	lines = Series_URL.split('\n')
	for line in lines:
		found = re.search(Issue_Regex, line)
		if found:
			match = found.groupdict()
			if match['issue']:
				#print('Issue url: {}'.format(match))
				Edited_Url = str(Series_URL)+'?&readType=1'
				url = str(Edited_Url)
				Quality = Settings_Reader()
				Single_Issue(url,Quality)

			else:
				#print('Series url: {}'.format(match))
				#Edited_Url = str(Series_URL)
				url = str(Series_URL)
				driver = create_driver()
				Quality = Settings_Reader()
				Whole_Series(driver,url,Quality)

		found = re.search(Annual_Regex, line)
		if found:
			match = found.groupdict()
			
			if match['issue']:
				#print('Issue url: {}'.format(match))
				Edited_Url = str(Series_URL)+'?&readType=1'
				url = str(Edited_Url)
				Quality = Settings_Reader()
				Single_Issue(url,Quality)
			else:
				print 'Uh, please check the link'	

		if not found:
			print 'Please Check Your URL one again!'
			sys.exit()


def create_driver():
	driver = webdriver.PhantomJS(service_args=['--load-images=no'])
	return driver

def Single_Issue(url,Quality):
	#print url
	print 'Quality To Download : ',Quality[0]
	print 'Order To Download : ',Quality[1]
	#sys.exit()
	#print url,' This is first'
	
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
		browser.save_screenshot('Single_exception.png')
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
	
	
	Series_Name_Splitter = url.split('/')
	Series_Name = str(Series_Name_Splitter[4]).replace('-',' ')
	#print Series_Name

	Issue_Number_Splitter = str(Series_Name_Splitter[5])
	#print Issue_Number_Splitter
	Issue_Or_Annual_Split = str(Issue_Number_Splitter).split("?")
	Issue_Or_Annual = str(Issue_Or_Annual_Split[0]).replace("-"," ").strip()
	#print Issue_Or_Annual
	reg = re.findall(r'[(\d)]+',Issue_Number_Splitter)
	#print reg
	Issue_Number = str(reg[0])
	#print Issue_Number


	print '\nSeries Name : ', Series_Name,' -',Issue_Number,'\n'
	#print Series_Name,'\n'
	#print Issue_Number,'\n'
	print '#####################################\n'
	Raw_File_Directory = str(Series_Name)+'/'+str(Issue_Or_Annual)
	File_Directory = re.sub('[^A-Za-z0-9\-\.\'\#\/ ]+', '', Raw_File_Directory) # Fix for "Special Characters" in The series name
	#print File_Directory
	Directory_path = os.path.normpath(File_Directory)
	#print Directory_path


	with open('source.txt') as searchfile:
			for line in searchfile:
				left,sep,right = line.partition('lstImages.push("') 
				if sep:
					OG_Title = right.replace('");','')
					#print OG_Title
					#print str(OG_Title).replace('=s0','=s1600')
					if not os.path.exists(File_Directory):
						os.makedirs(File_Directory)
					if Quality[0] in ['LQ']:
						OG_Title = str(OG_Title).replace('=s0','=s1600')
						#print OG_Title
						try:
							u = urllib2.urlopen(OG_Title)
						except URLError, e:
							if not hasattr(e, "code"):
								raise
							print "Got error from "+OG_Title, e.code, e.msg
							resp = e
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
					elif Quality[0] in ['HQ']:
						OG_Title = str(OG_Title).replace('=s1600','=s0')
						#print OG_Title
						try:
							u = urllib2.urlopen(OG_Title)
						except URLError, e:
							if not hasattr(e, "code"):
								raise
							print "Got error from "+OG_Title, e.code, e.msg
							resp = e
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

def Whole_Series(driver,url,Quality):
	#print '\nDownloading Whole Series'
	#print url

	Range_Input = str(raw_input("Enter The Range : ")).strip()

	

	if Range_Input.upper() not in ["NONE","NULL","ALL"]:

		Range_Splitter = Range_Input.split("-")
		Starting_Range = int(str(Range_Splitter[0]).strip())
		Ending_Range = int(str(Range_Splitter[1]).strip())

		Url_Spliiter = url.split("/Comic/")
		Extra_Remover = str(Url_Spliiter[1]).replace('/','')
		#print "Extra remover : ",Extra_Remover
		Show_Name = str(Extra_Remover).strip()
		Type_Input = str(raw_input("Annual or Issue? : ")).strip()

		if Type_Input.upper() in ["ANNUAL"]:
			Type = "Annual"
		if Type_Input.upper() in ["ISSUE"]:
			Type = "Issue"

		for x in range(Starting_Range,Ending_Range+1):
			#print x
			#Example URL = http://readcomiconline.to/Comic/Injustice-Gods-Among-Us-I/Issue-36?
			url = "http://readcomiconline.to/Comic/"+Show_Name+"/{}-".format(Type)+str(x)+"?&readType=1"
			#print url
			Single_Issue(url,Quality)

	if Range_Input.upper() in ["NONE","NULL","ALL"]:

		driver.get(url)
		try:
			print 'Bypassing the check. Wait for a few seconds please.'
			element = WebDriverWait(driver, 10).until(
				EC.presence_of_element_located((By.ID, "stSegmentFrame"))
			)
			#print 'Downloading the whole page! Will take some time, please don\'t close this script...\n'
			#print 'I\'ve waited long enough'
		except Exception, e:
			#raise e
			driver.save_screenshot('Whole_exception.png')
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
			os.remove('.Temp_File') #Removing this because I need to check if there's a file with this name or not. Because if the file exists, then it'll APPEND to the older script and it'll download old + new comics
		except Exception, e:
			#raise e
			pass

	
		with open('source2.txt') as searchfile:
			with open('.Temp_File','a') as Temp_File_variable:
				for line in searchfile:
					left,sep,right = line.partition('title="Read ') # Extra Space to make it more precise and drop the readcomiconline.to link
					if sep:
						OG_Title = left.split('"')
						#print OG_Title
						#print OG_Title[1]
						Raw_Issue_Links = OG_Title[1].strip()
						Issue_Links = 'http://readcomiconline.to'+str(Raw_Issue_Links)
						#print Issue_Links,' #'
						Temp_File_variable.write(str(Issue_Links)+'\n')
						Temp_File_variable.flush()
			Temp_File_variable.close()


		with open(".Temp_File","r") as input:
			with open(".Temp_File2","wb") as output: 
				for line in input:
					if line != "http://readcomiconline.to../../Content/images/bullet.png":
						output.write(line)
						#print line

		
		if Quality[1] in ['LATEST']:
			with open('.Temp_File','r') as Link_File:
				for line in Link_File:
					bs_link = 'http://readcomiconline.to../../Content/images/bullet.png'
					if bs_link in line:
						#print 'line'
						pass
					else :
						url = str(line)
						#print url
						Single_Issue(url,Quality)

	
		elif Quality[1] in ['OLD']:
			for line in reversed(open('.Temp_File').readlines()):
				#print line
				bs_link = 'http://readcomiconline.to../../Content/images/bullet.png'
				if bs_link in line:
					#print 'line'
					pass
				else :
					url = str(line)
					#print url
					Single_Issue(url,Quality)

		'''
		os.remove('source2.txt')		
		'''
		

	
		#Remove the .temp_fle so that it doesn't append to the old data!	

def Settings_Reader():

	#config = ConfigParser()
	config = ConfigParser.ConfigParser(allow_no_value=True)
	config.read('Settings.ini')
	#print config.sections()
	Quality = config.get('ScriptSettings', 'Quality')
	Order = config.get('ScriptSettings', 'Order')
	#Chapters_Range = config.get('ScriptSettings', 'Chapters(Range)')

	#Chap_Range_Breaker = str(Chapters_Range).split('-')
	#Start_Number = str(Chap_Range_Breaker[0]).strip()
	#End_Number = str(Chap_Range_Breaker[1]).strip()
	#print Chapters_Range
	#print Start_Number
	#print End_Number

	#print Quality,Order

	if Quality.upper() in ['LQ','LOW','LOW QUALITY']:
		#print 'Lower Quality'
		Quality = 'LQ'
	elif Quality.upper() in ['HQ','HIGH','HIGH QUALITY']:
		#print 'Higher Quality'
		Quality = 'HQ'

	if Order.upper() in ['LATEST','NEW']:
		#print 'Lastest Issues'
		Order = 'LATEST'
	elif Order.upper() in ['OLD','INITIAL']:
		#print 'Older Issues'
		Order = 'OLD'
	
	return (Quality,Order)

try:
	#Chap_Checker()
	Url_Fetching()
	#Settings_Reader()
except Exception, e:
	#raise e
	print e
	sys.exit()


#url = 'http://readcomiconline.to/Comic/Injustice-Gods-Among-Us-I'	
#url = 'http://readcomiconline.to/Comic/Injustice-Gods-Among-Us-I/Issue-36?id=25113'
