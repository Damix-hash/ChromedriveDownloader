import requests
import os

def latest_chromedriver():
    chromedriver_download_site = "https://getwebdriver.com/chromedriver"

    response = requests.get(chromedriver_download_site)
    if response.status_code == 200:
        for line in response:
            if "<h2>Stable</h2><p>Version:" in line.decode('utf-8'):
                version = line[0:-15].decode('utf-8').strip().replace("<code>", "")
                break

    n = version.find("Version:")
    if not "<" in version[n+9:]:
        return_version = version[n+9:]
    else:
        version[n+9:].strip("<").strip("\")
    return 

    
def download_chromedriver(path, operating_system, version, override):
    if operating_system == "":
        operating_system = "win32"

    if path == "":
        path = os.getcwd()

    chromedriver_dir = path
    chromedriver_path = f"{chromedriver_dir}/chromedriver.exe"
    
    print("===========================[ChromedriverDownloader]===========================")
    print(f"Checking for chromedriver.exe at: {chromedriver_path}")
    
    if not os.path.exists(chromedriver_path):
        print(f"Downloading Chromedriver To: {path}, Version: {version}")
        url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_{operating_system}.zip"


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
        url = f"https://chromedriver.storage.googleapis.com/{version}/chromedriver_{operating_system}.zip"


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
