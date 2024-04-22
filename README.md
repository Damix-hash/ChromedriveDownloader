# ChromedriveDownloader
Alternative to ChromeDriverManager

# What's that?
This is alternative to ChromeDriverManager that should'nt create any issues with for example version download.
It downloads latest STABLE version of ChromeDriver into specified folder of your project!
Allows overriting which lets you update chromedriver.exe to the latest version.
Also allows you to download chromedriver for specified operating systems!

Allowed operating systems are:

- linux64
- mac-arm64
- mac-x64
- win32
- win64
  
You must write the operating systems as provided

# Requirements
All you need is to install requests by putting this into command prompt.
```
pip install requests
```
# How to use it?
To import this into your project (after downloading and placed into the project) do:
```
from ChromedriverDownloader import *
```
on top of the code.
