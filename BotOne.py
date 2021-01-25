from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

favChips = ['Takis','Cheetos Crunchy Flamin Hot','Doritos','Turbos Flamas']
superMarkets = ['Walmart Supercenter','Target','Albertsons','Sam\'s Club']
#for loop will check for every chip price favChips in Target 


for chip in enumerate(favChips):
    driver.get("https://www.target.com/")
    targetSearchBar = driver.find_element_by_xpath('//*[@id="search"]')
    targetSearchBar.send_keys(chip)
    targetSearchBar.send_keys(Keys.ENTER)




