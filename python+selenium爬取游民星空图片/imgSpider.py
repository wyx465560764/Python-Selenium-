

from selenium import webdriver
import time
import download

driver=webdriver.Chrome()
driver.get('http://www.gamersky.com/ent/201807/1079099.shtml')

i=0
while i<40:
    print('第',(i+1),'页')
    imgItem=driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[1]/div[1]/div[3]')
    for img in imgItem.find_elements_by_xpath('.//img'):
        url=img.get_attribute('src')
        print(url)
        download.download(url)
    if i==0:
        driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[1]/div[1]/div[3]/div/a[11]').click()
    else:
        driver.find_element_by_xpath('/html/body/div[10]/div[2]/div[1]/div[1]/div[3]/div/a[12]').click()
    time.sleep(2)
    i+=1
driver.quit()