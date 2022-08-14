from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")





# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

# drive_path: str = '/Users/apple/Documents/Python/Project/Automation/chromedriver'
#
# from selenium import webdriver
# import chromedriver_autoinstaller
#
#
# chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
#                                       # and if it doesn't exist, download it automatically,
#                                       # then add chromedriver to path
#
# driver = webdriver.Chrome()
# driver.get("http://www.python.org")
# assert "Python" in driver.title

# options = webdriver.ChromeOptions()
# # options.set_capability("loggingPrefs", {'performance': 'ALL'})
# options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
# driver = webdriver.Chrome(executable_path=r'\\path\\chromedriver.exe')
#
# # service = Service(executable_path=r, drive_path)
# driver = webdriver.Chrome(service=service, options=options)




# s=Service(drive_path)
#
# browser = webdriver.Chrome(service=s, "goog")
# url='https://www.google.com'
# browser.get(url)

# ser = Service(drive_path)
# op = webdriver.ChromeOptions()
# s = webdriver.Chrome(service=ser, options=op)




# from selenium import webdriver
# from selenium.webdriver.chrome.webdriver import WebDriver
#
# chrome_browser: WebDriver = webdriver.Chrome('/Users/apple/Documents/Python/Project/Automation/chromedriver')
# chrome_browser.maximize_window()