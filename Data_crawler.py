from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

def crawler_download_table(driver):
    driver.find_element_by_class_name('jfBasicModal-close').click()
    time.sleep(5)
    driver.find_element_by_class_name('lsApp-list-item-link').click()
    time.sleep(8)
    buttons = driver.find_elements_by_tag_name('button')
    for b in buttons:
        val = b.get_attribute('aria-label')
        if val == "Download All":
            b.click()
            break
    time.sleep(4)
    dev = driver.find_element_by_class_name('jSheetDownload-links')
    buttons = dev.find_elements_by_tag_name('button')
    buttons[0].click()
    time.sleep(15)

def crawler_insert_data_to_login(driver):
    usrName = 'archanr@synopsys.com'
    password = 'IWillSucceed1$'
    driver.find_element_by_name('email').send_keys(usrName)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('signinButton').click()
    time.sleep(8)

def crawler_open_chrome():
    c = webdriver.ChromeOptions()
    c.add_argument("--incognito")
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=c)
    driver.implicitly_wait(0.5)
    url = "https://www.jotform.com/login/"
    driver.get(url.format(q='Car'))
    driver.maximize_window()
    time.sleep(5)
    return driver

def crawler_main():
    driver = crawler_open_chrome()
    crawler_insert_data_to_login(driver)
    crawler_download_table(driver)
    driver.quit()

