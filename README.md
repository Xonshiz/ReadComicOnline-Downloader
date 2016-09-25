# ReadComicOnline-Downloader
A little script to download comics from http://readcomiconline.to/

Don't forget to read the ["Settings.ini"](https://github.com/Xonshiz/ReadComicOnline-Downloader#settingsini-file-) file.

#How To Use
If you're a windows user, download the windows Binaries from these links :


1.) x64 : [CLICK ME](http://www.multiupfile.com/f/22e04cb9) OR [CLICK ME](https://drive.google.com/file/d/0B27CFrTCSppNdTg2LXY3cjEtYzQ/view?usp=sharing)

2.) x86 (32 Bit systems) : [CLICK ME](#)


After downloading, please extract the contents using 7zip/winrar etc.


Don't extract in places where you will need admin privilege. 

After extraction, just run the "ReadComicOnline Downloader.exe" and it'll ask you for the link of the series, enter the link to the Series or a Single Issue :

Series : `http://readcomiconline.to/Comic/The-New-Guardians`

Single Issue : `http://readcomiconline.to/Comic/The-New-Guardians/Issue-12?id=84032`

It will ask for permission to connect to internet, let it connect and it'll do what it is supposed to do.

# First Things First! (For people using the python file, isntead of win. binary)

Download the "requirements.txt" in some directory. Open Command Prompt and browse to the directory where you downloaded your requiremenets.txt file and run this command :

`pip install -r requirements.txt`

NOTE : You need to have "PIP" installed in your system and set in the path. Python 2.7.10 should already have this done. Just double check on your end though.

#Features :
1.) Downloads all the Issues available for a series. 

2.) Puts the files in corresponding directories after downloading the files.

3.) Downloads Hight Quality images.

4.) Skips the file if it already exists in the path. 

5.) Option to choose Qulity of Images

6.) Option to download Latest or Older releases.


#Settings.ini File :
Please Read these instructions carefully for updating the settings for the script.


`Quality` represents which quality image you want to download. Low Qulatiy or High Quality. Change this parameter to "LQ","HQ","Low Quality" or "High Quality".
By default, "HQ" is set.


`Order` represents which ISSUE you want to download first. Latest uploaded Issue for a series or the oldest uploaded Issue. Option for this parameter are "Old","Latest","New" or "Initial".
Initial means the oldest chapter.


There are various options you can choose to write. Write either of them. By default, the settings are to download "High Quality" images, while downloading the "Oldest" Issue first.

Check the "Settings.ini" file in this repo. and update it to your requirements (if needed).


#FUTURE FEATURES :
2.) Option to download particular Issues from a series. 

3.) Option to download particular Issues from a series.

#CHANGELOG :
1.) Re-Wrote the whole script for better understanding and flow.

2.) Downloading of all the Issues available for a series.

3.) Corresponding Directories for the series and an Issue.

4.) File skipping, if the file already exists.

5.) Error Log File creation.

6.) Option to download Latest or Older releases.

7.) Option to choose Qulity of Images.
