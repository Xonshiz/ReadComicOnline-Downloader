# Readcomic Online Downloader

[![N|Solid](https://raw.githubusercontent.com/Xonshiz/ReadComicOnline-Downloader/master/favicon.ico)](https://github.com/Xonshiz/ReadComicOnline-Downloader)

# This is not maintained anymore. Please check [Comic-dl](https://github.com/Xonshiz/comic-dl) instead.
[Comic-dl](https://github.com/Xonshiz/comic-dl) is a command line tool to download manga and comic from various websites. It supports readcomiconline.to and is faster and better than this one.

# Introduction
ReadComic Online Downloader is a command line tool to download comics from http://readcomiconline.to/

  - Don't forget to read the ["Settings.ini"](https://github.com/Xonshiz/ReadComicOnline-Downloader#settingsini-file-) file.
  

> Don't overuse this script. Support the developers of readcomiconline.to by disabling your adblock on their site. Advertisments pay for the website servers.

## Table Of Content
* [Dependencies Installation](https://github.com/Xonshiz/ReadComicOnline-Downloader#dependencies-installation)
* [Installation](https://github.com/Xonshiz/ReadComicOnline-Downloader#installation)
* [Settings.ini File](https://github.com/Xonshiz/ReadComicOnline-Downloader#settingsini-file)
* [Windows Binary](https://github.com/Xonshiz/ReadComicOnline-Downloader#windows-binary)
* [Usage](https://github.com/Xonshiz/ReadComicOnline-Downloader#usage)
* [Features](https://github.com/Xonshiz/ReadComicOnline-Downloader#features)
* [Future Features](https://github.com/Xonshiz/ReadComicOnline-Downloader#future-features)
* [Known Issues/Bugs](https://github.com/Xonshiz/ReadComicOnline-Downloader#known-issuesbugs-)
* [Changelog](https://github.com/Xonshiz/ReadComicOnline-Downloader#changelog)
* [Contributors](https://github.com/Xonshiz/ReadComicOnline-Downloader#contributors)

## Dependencies Installation
This script can run on multiple Operating Systems. However, if you're using any OS other than windows, then you might need to install certain things before hand to get this script working.

### Linux/Debian :

First, make sure your system is updated :
```
sudo apt-get update
sudo apt-get install build-essential chrpath libssl-dev libxft-dev
```
Grab Dependencies for PhantomJS (most important) :
```
sudo apt-get install libfreetype6 libfreetype6-dev
sudo apt-get install libfontconfig1 libfontconfig1-dev
```
Grab the suitable `tar.bz2` file from this [link](http://phantomjs.org/download.html)
Extract the contents of this `tar.bz2` file you just downloaded. Open a terminal and follow the commands. 
* Don't forget the change the name of the file(s) mentioned here with the ones that you downloaded.There might be a newer version when you download
```
cd /Name/of_the/directory/that/contains/the/tar_bz2/file
export PHANTOM_JS="phantomjs-2.1.1-linux-x86_64"
sudo tar xvjf $PHANTOM_JS.tar.bz2
```
Once downloaded, move Phantomjs folder to /usr/local/share/ and create a symlink:
```
sudo mv $PHANTOM_JS /usr/local/share
sudo ln -sf /usr/local/share/$PHANTOM_JS/bin/phantomjs /usr/local/bin
```
If none of these commands gave error(s), PhantomJS should be installed in your Linux/Debian systems just fine. You can check it by entering this command in any terminal :
```
phantomjs --version
```

### Windows :
If you're on windows, then it is recommended to download the [`windows binary`](https://github.com/Xonshiz/ReadComicOnline-Downloader#windows-binary) for this script. If you use the windows binary, you don't need to install anything. But, if for some weird reason you want to use Python script instead, then follow these steps :

* Install Python > 2.7.6. Download the desired installer from [here](https://www.python.org/downloads/).
* [Add it in the system path](http://superuser.com/questions/143119/how-to-add-python-to-the-windows-path) (if not already added).
* If you're using python >2.7.9, you don't need to install `PIP`. However, if you don't have pip installed and added in windows path, then do so by following [this little tutorial](http://stackoverflow.com/a/12476379).
* Download [this `text`](https://raw.githubusercontent.com/Xonshiz/ReadComicOnline-Downloader/master/requirements.txt) file and put it in some directory/folder.
* Open Command Prompt and browse to the directory where you downloaded your requiremenets.txt file and run this command :

    ```pip install -r requirements.txt```
* It should install the required external libraries.
* Download PhantomJS : http://phantomjs.org/download.html

Well, if everything came up good without any error(s), then you're good to go!

### Mac OS X :
Mac OS X users will have to fetch their version of `PhantomJS` ,`Python` and `Pip`.
* Python installation guide : http://docs.python-guide.org/en/latest/starting/install/osx/
* Pip installation guide : http://stackoverflow.com/questions/17271319/installing-pip-on-mac-os-x
* PhantomJS Mac Binary : http://phantomjs.org/download.html (Download the latest build for your OS)

After downloading and installing these, you need to add PIP,Python and PhantomJS in your path. You can look it up on internet to follow the guides to achieve this.

I'd manually show it here how to do it, but I don't have a Mac OS X system. So, you'll need to follow those links.

## Installation
After installing and setting up all the dependencies in your Operating System, you're good to go and use this script.
The instructions for all the OS would remain same. Download [`this python file`](https://github.com/Xonshiz/ReadComicOnline-Downloader/blob/master/readcomic.py) and put it in a folder somewhere in your system.

For windows and Mac OS X, you'll need to copy phantomJS in the directory of this script. Meaning, copy the phantomJS binary that you downloaded in to the folder where you're kept this `readcomic.py` file.

As for Linux/Debain users, we've already put the binary in the appropriate place. Hence, you don't need to copy the PhantomJS binary in the folder.

##### `NOTE`: Windows users can put the PhantomJS.exe somewhere safe in your system and add the path to it in your system path.


## Settings.ini File
Please Read these instructions carefully for updating the settings for the script.

`Quality` represents which quality image you want to download. Low Quality or High Quality. Change this parameter to "LQ","HQ","Low Quality" or "High Quality".
By default, "HQ" is set.

`Order` represents which ISSUE you want to download first. Latest uploaded Issue for a series or the oldest uploaded Issue. Option for this parameter are "Old","Latest","New" or "Initial".
Initial means the oldest chapter.

There are various options you can choose to write. Write either of them. By default, the settings are to download "High Quality" images, while downloading the "Oldest" Issue first.

Check the "`Settings.ini`" file in this repo. and update it to your requirements (if needed).

## Windows Binary
It is recommended that windows users use this binary to save both, your head and time from installing all the dependencies. You can download the binary and start using the script right off the bat. Grab the respective binaries from the links below :
* `x86 Systems` : [COMING SOON](#)
* `x64 Systems` : [CLICK ME](https://drive.google.com/file/d/0B27CFrTCSppNeU56Tk5lR0ZJOTg/view)

## Usage
Using the script is pretty simple. Execute the `.py` or the `.exe` file and paste the link to the ISSUE/SERIES you want to download.

If you want to download chapters/issue within a range, you'll have to specify a range. Let's say you want to download only chapters from chapter 20 to chapter 30 from a certain series, you can do so by entering the range when asked. If you want to download all the chapter from a show, then just enter `none`,`all` or `null` when asked about it.

For now, let's just download all the chapter from [this](http://readcomiconline.to/Comic/Injustice-Gods-Among-Us-I) series. Here's what you'll do :
* Open command prompt/Terminal and browse to the directory that have this script.

**Note :** Windows users can hold down shift and right click anywhere in the area and select "open command prompt here".

* Type `"ReadComicOnline Downloader.exe"` (with quotes) if you downloaded windows binary. Type `readcomic.py`, if you're using .py file instead.
* Press ENTER/RETURN.
* Enter the URL to the whole series, if you want to download all the chapter (or chapters within a range) or, if you want to download a particular chapter, enter the URL to that.
* Press ENTER/RETURN.
* If you're downloading a particular chapter, just sit back and wait till it downloads everything.
* However, if you're downloadig whole series or ranged chapters, you got more work to do. If you're downloading all or ranged chapters, follow along. Single Chapter downloaders should be reading the comic now ;)
* Now, the script should ask for the range. If you want to download chapters within a range, follow the steps from [How To Enter Range](https://github.com/Xonshiz/ReadComicOnline-Downloader#how-to-enter-range) section now. But, if you're downloading everything, enter `null`,`none` or `all` in this range question.
* Your job is done. It should download everything.

**Look at the GIF image below to see it all in action.**

**`Downloading Single Issue`**

[![N|Solid](https://github.com/Xonshiz/ReadComicOnline-Downloader/blob/master/Tutorial%20Images/Single_Issue.gif?raw=true)](https://github.com/Xonshiz/ReadComicOnline-Downloader/blob/master/Tutorial%20Images/Single_Issue.gif)

**`Downloading All The Chapters`**

[![N|Solid](https://github.com/Xonshiz/ReadComicOnline-Downloader/blob/master/Tutorial%20Images/Whole_Series.gif?raw=true)](https://github.com/Xonshiz/ReadComicOnline-Downloader/blob/master/Tutorial%20Images/Whole_Series.gif)

#### How to Enter Range
Range is to be entered in the following syntax : `4-6`

This tells the script that you want to download chapter 4 to chapter 6 **(both included)**.

Follow the first `7` steps mention in the [USAGE](https://github.com/Xonshiz/ReadComicOnline-Downloader#usage) section and then carry on from here:
* So, when it asks for you to enter range, you're going to enter from where to where you want to download chapters. Let's say you want to download from chapter 5 to chapter 10. You'll enter `5-10`.
* Now, it'll ask you whether those are `Issue or Annual`. Readcomic have two things, `Annual` chapters and `Issue Chapters`. So, check on that site whether it is an Annual or a normal Issue. It's safe to enter `Issue` in most cases.
* Press ENTER/RETURN and it'll download it.

**Look at the GIF image below to see it all in action.**

**`Downloading Chapters Within A Certain Range`**

[![N|Solid](https://github.com/Xonshiz/ReadComicOnline-Downloader/blob/master/Tutorial%20Images/Range_Chapters.gif?raw=true)](https://github.com/Xonshiz/ReadComicOnline-Downloader/blob/master/Tutorial%20Images/Range_Chapters.gif)


## Features
Since this is a very simple and basic script, at the current moment, it has limited features :

* Downloads all the Issues available for a series. 

* Puts the files in corresponding directories after downloading the files.

* Downloads High Quality images.

* Skips the file if it already exists in the path. 

* Option to choose Quality of Images

* Option to download Latest or Older releases.

* Option to download certain chapters within a range.

## Known Issues/Bugs
Because readcomiconline.to is behind CloudFlare, there's a limit to visit the site. If you're downloading a series with a lot of Issues or chapters, the script will halt mid-way, because cloudflare needs a 'Human Check'. Example URL to replicate this issue : http://readcomiconline.to/Comic/The-Amazing-Spider-Man-1963

Thanks to [Gizmo179](https://github.com/gizmo179) for notifying me about the issue. Currently there's nothing I can do about it.

Workaround for this Issue is by opening the website via your browser and verifying manually and then downloading chapters within a range. If that doesn't work, try downloading the chapters within a range after some time.

## CHANGELOG
* Re-Wrote the whole script for better understanding and flow.

* Downloading of all the Issues available for a series.

* Corresponding Directories for the series and an Issue.

* File skipping, if the file already exists.

* Error Log File creation.

* Option to download Latest or Older releases.

* Option to choose Quality of Images.

* File name Fix and some Minor Bug Fix

* Annual Issues are downloaded properly now.

* Option to download certain chapters within a range.

* Fix for #4
 
## Contributors:
Thank you guys for pull requests and fixing silly issues.

1.) [Efreak](https://github.com/Efreak)
