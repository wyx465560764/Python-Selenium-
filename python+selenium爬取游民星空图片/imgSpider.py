
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium import webdriver
import time
import download
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome()
driver.get('http://www.gamersky.com/ent/201807/1080195.shtml')

i=0
while i<50:
    print('第',(i+1),'页')
    imgItem=driver.find_element_by_css_selector('.Mid2L_con')
    for img in imgItem.find_elements_by_xpath('.//img'):
        url=img.get_attribute('src')
        print(url)
        download.download(url)
    driver.find_element_by_xpath('/html/body').send_keys(Keys.RIGHT)
    time.sleep(2)
    i+=1
driver.quit()