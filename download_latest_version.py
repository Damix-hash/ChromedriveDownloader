from ChromedriverDownloader import *

# operating_systems are avaible at their official site.
# download_chromedriver(path, operating_system, version, bool)
# if you want user on start to get latest version just use latest_

version = latest_chromedriver()

download_chromedriver("", "", version, True)
input("Press ENTER To Leave.")
