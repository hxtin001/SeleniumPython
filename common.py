from selenium.webdriver.support.ui import Select
from random import randint
import constants

#initial
def init(driver, web_address):
    driver.get(web_address)
    driver.implicitly_wait(100)

#Select oneway or round, xpath = xpath_oneway or xpath = round
def select_oneway_or_round(driver, xpath):
    # Click choose oneway or round
    driver.find_element_by_xpath(xpath).click()

# Select a random number
def select_random_num():
    return randint(1, 10)

#get a city from list
def select_city_value(listx, id):
    return listx[id]

#select a value from element
def select_value_by_id(driver, element_id, value):
    select = Select(driver.find_element_by_id(element_id))
    select.select_by_value(value)

#Select date depart
def select_datepicker(driver, yearx, monthx, dayx, xpath):
    #Click to show calendar
    driver.find_element_by_xpath(constants.xpath_calendar).click()
    xpath = xpath.replace("YEAR", yearx)
    xpath = xpath.replace("MONTH", monthx)
    xpath = xpath.replace("DAY", dayx)
    #Find a date
    try:
        driver.find_element_by_xpath(xpath).click()
    except:
        pass

#Select value by xpath
def select_value_by_xpath(driver, xpath, value):
    select = Select(driver.find_element_by_xpath(xpath))
    select.select_by_value(value)
