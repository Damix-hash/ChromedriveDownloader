from ChromedriverDownloader import *

# operating_systems are avaible at their official site.
# download_chromedriver(path, operating_system, version, overrite)

# PATH || STR = Your chromedriver path folder. Leave empty to put chromedriver to PATH of the script.
# OPERATING_SYSTEM || STR = Operating system. Leave empty for win32.
# VERSION || INT = Version of chromedriver.
# OVERRITE || BOOL = Removes chromedriver.exe if exists. (for updating chromedriver to latest)

# if you want user on start to get latest version just use latest_chromedriver()

version = latest_chromedriver()

download_chromedriver("", "", version, True)
input("Press ENTER To Leave.")
