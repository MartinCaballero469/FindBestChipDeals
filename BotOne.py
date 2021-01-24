from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

favChips = ['Takis','Flamin hot crunchy cheetos','Doritos','Turbos Flamas']
superMarkets = ['Walmart Supercenter','Target','Albertsons','Sam\'s Club']


for chips in favChips:
    driver.get("https://google.com/shopping")
    googleInput = driver.find_element_by_css_selector("input[type='search'][class='r7gAOb yyJm8b']")

    googleInput.send_keys(chips)
    googleInput.send_keys(Keys.ENTER)
