import requests
import os
import platform

def latest_chromedriver():
    chromedriver_download_site = "https://getwebdriver.com/chromedriver"

    response = requests.get(chromedriver_download_site)
    if response.status_code == 200:
        for line in response:
            if "<h2>Stable</h2><p>Version:" in line.decode('utf-8'):
                version = line[0:-15].decode('utf-8').strip().replace("<code>", "")
                break
            
    stable_version = ''
    version_start = version.find("Version:")
    version_start = version_start + 9
    version_check = version[version_start:]
    if "<" in version_check:
        version_end = version.find("<", version_start)
        stable_version = version[version_start:version_end]
    else:
        stable_version = version[version_start:]
    return stable_version

    
def download_chromedriver(path, operating_system, version, override):
    if operating_system == "":
        computer_os = platform.system()
        computer_bits = platform.architecture()[0]
        
        if computer_os == "Linux" and computer_bits == "x86_64":
            operating_system = "linux64"
        elif computer_os == 'Darwin' and computer_bits == 'arm64':
            operating_system = "mac-arm64"
        elif computer_os == 'Darwin' and computer_bits == 'x86_64':
            operating_system = "mac-arm64"
        elif computer_os == 'Windows' and computer_bits == '32bit':
            operating_system = "win32"
        elif computer_os == 'Windows' and computer_bits == '64bit':
            operating_system = "win64"
        
    if path == "":
        path = os.getcwd()

    chromedriver_dir = path
    chromedriver_path = f"{chromedriver_dir}/chromedriver.exe"
    
    print("===========================[ChromedriverDownloader]===========================")
    print(f"Checking for chromedriver.exe at: {chromedriver_path}")
    
    if not os.path.exists(chromedriver_path):
        print(f"Downloading Chromedriver To: {path}, Version: {version}, OS: {operating_system}")
        url = f"https://storage.googleapis.com/chrome-for-testing-public/{version}/{operating_system}/chromedriver-{operating_system}.zip"


        try:
            response = requests.get(url)
            with open(chromedriver_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded Chromedriver To: {path}, Version: {version}")
        except Exception as e:
            print("ERROR:", str(e)) # :3
            input("Press ENTER To Leave. Please Provide Above Error To Author On Github. https://github.com/Damix-hash/ChromedriveDownloader/issues")
            exit()
            
    elif os.path.exists(chromedriver_path) and override == True:
        print(f"Removing chromedriver.exe From: {chromedriver_path}")

        try:
            os.remove(chromedriver_path)
        except Exception as e:
            print("ERROR:", str(e)) # :3
            input("Press ENTER To Leave. Please Provide Above Error To Author On Github. https://github.com/Damix-hash/ChromedriveDownloader/issues")
            exit()
            
        print(f"Downloading Chromedriver To: {path}, Version: {version}")
        url = f"https://storage.googleapis.com/chrome-for-testing-public/{version}/{operating_system}/chromedriver-{operating_system}.zip"


        try:
            response = requests.get(url)
            with open(chromedriver_path, 'wb') as file:
                file.write(response.content)
            print(f"Downloaded Chromedriver To: {path}, Version: {version}")
        except Exception as e:
            print("ERROR:", str(e)) # :3
            input("Press ENTER To Leave. Please Provide Above Error To Author On Github. https://github.com/Damix-hash/ChromedriveDownloader/issues")
            exit()
    else:
        print(f"chromedriver.exe Already Exists At: {chromedriver_path}")
