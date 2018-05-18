# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import Select
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import sys
import constants
import common

web_address = 'https://console.cloud.google.com/projectselector/home/dashboard?cloudshell=true&supportedpurview=project&project&folder&organizationId'
path_firefox = r'/usr/bin/firefox'
path_geckodriver = '/home/hxtin001/Documents/Project/software/geckodriver'
marionette = 'marionette'
xpath_round = '//*[@id="gridBox"]/div[2]/div/div[1]/ul/li[1]/label/input'
xpath_oneway = '//*[@id="gridBox"]/div[2]/div/div[1]/ul/li[2]/label/input'
xpath_selectDomesticAirport = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[1]/dl/dd[1]/ul[2]/li/select'
xpath_abroad_area = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[1]/dl/dd[2]/ul/li[1]/select'
xpath_abroad_country = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[1]/dl/dd[2]/ul/li[2]/select'
xpath_abroad_port = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[1]/dl/dd[2]/ul/li[3]/select'
xpath_depTime1 = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[3]/div[1]/dl/dd/ul/li[1]/label/input' #DepTimes 4:00 - 6:59
xpath_depTime2 = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[3]/div[1]/dl/dd/ul/li[2]/label/input' #DepTimes 7:00 - 11:59
xpath_depTime3 = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[3]/div[1]/dl/dd/ul/li[3]/label/input' #DepTimes 12:00 - 17:59
xpath_depTime4 = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[3]/div[1]/dl/dd/ul/li[4]/label/input' #DepTimes 18:00 - 22:59
xpath_depTime5 = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[3]/div[1]/dl/dd/ul/li[5]/label/input' #DepTimes 23:00 - 3:59
xpath_adult_num = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[2]/dl[2]/dd[3]/select' #Adult number from 1 to 9
xpath_total_child_num = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[2]/dl[2]/dd[4]/select'
xpath_seat_class = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[3]/div[2]/dl/dd[1]/select'
xpath_carriers = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[3]/div[2]/dl/dd[2]/select'
xpath_search_criteria = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/p/a'
xpath_datepicker = '//div[@id="ui-datepicker-div"]//td[@data-year="YEAR"][@data-month="MONTH"]/a[@class="ui-state-default"][text()="DAY"]'
xpath_calendar = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[2]/dl[1]/dd/div'
xpath_btn_search = '//*[@id="gridBox"]/div[2]/div/div[1]/div[1]/div[5]/button'
xpath_check_flight_btn = '//*[@id="str-main-content"]/div[5]/div[1]/div[1]/div[3]/div/p/span[2]'
xpath_select_air = '//*[@id="str-main-content"]/div[5]/div[1]/div[2]/div/div[3]/p[1]/a'
xpath_family_name1 = '//*[@id="anchor_traveler_0"]/div[1]/table/tbody/tr[1]/td/div/table/tbody/tr/td[1]/input'
xpath_first_name1 = '//*[@id="anchor_traveler_0"]/div[1]/table/tbody/tr[1]/td/div/table/tbody/tr/td[2]/input'
xpath_sex_female1 = '//*[@id="anchor_traveler_0"]/div[1]/table/tbody/tr[2]/td/div/ul/li[2]/label/input'
xpath_sex_male1 = '//*[@id="anchor_traveler_0"]/div[1]/table/tbody/tr[2]/td/div/ul/li[1]/label/input'
xpath_year1 = '//*[@id="anchor_traveler_0"]/div[1]/table/tbody/tr[3]/td/div/div/input'
xpath_month1 = '//*[@id="anchor_traveler_0"]/div[1]/table/tbody/tr[3]/td/div/div/select[1]'
xpath_day1 = '//*[@id="anchor_traveler_0"]/div[1]/table/tbody/tr[3]/td/div/div/select[2]'
xpath_nationality1 = '//*[@id="anchor_traveler_0"]/div[1]/table/tbody/tr[4]/td/div/select'
xpath_family_name2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[2]/td/div/ul/li[1]/input'
xpath_first_name2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[2]/td/div/ul/li[2]/input'
xpath_family_name_kana2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[3]/td/div/ul/li[1]/input'
xpath_first_name_kana2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[3]/td/div/ul/li[2]/input'
xpath_family_name_alphabet2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[4]/td/div/ul/li[1]/input'
xpath_first_name_alphabet2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[4]/td/div/ul/li[2]/input'
xpath_sex_female2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[5]/td/div/ul/li[2]/label/input'
xpath_sex_male2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[5]/td/div/ul/li[1]/label/input'
xpath_year2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[6]/td/div/input' # Female
xpath_month2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[6]/td/div/select[1]'
xpath_day2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[6]/td/div/select[2]'
xpath_nationality2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[7]/td/div/select'
xpath_tel_num1 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[8]/td/div/input[1]'
xpath_tel_num2 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[8]/td/div/input[2]'
xpath_tel_num3 = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[8]/td/div/input[3]'
xpath_mail_address_confirm = '//*[@id="memBlock"]/div[2]/div[1]/table/tbody/tr[9]/td/div/ul/li[2]/input'
name_card_holder = 'cardholder'
xpath_card_expiration_month = '//*[@id="payCredit"]/div[1]/table/tbody/tr/td/div[2]/dl/dd[3]/select[1]'
xpath_card_expiration_year = '//*[@id="payCredit"]/div[1]/table/tbody/tr/td/div[2]/dl/dd[3]/select[2]'
xpath_mail_address = '//*[@id="str-contents-wrap"]/div[3]/div[1]/div[4]/div/div[2]/div/dl/dd/input'
xpath_registry_button = '//*[@id="str-contents-wrap"]/div[3]/div[1]/div[4]/div/div[1]/p[2]/a' # xpath button to login
xpath_username = '//*[@id="input_member_mail"]/input'
xpath_password = '//*[@id="member_pass"]/input'
name_password = 'password'
name_password_confirm = 'passwordConfirm'
name_card_security_code = 'cardSecurityCode'
id_card_number = 'cardNumberNew'
id_submit_input = 'submitInput'
id_agree_payment = 'agree_payment'
id_agree_travel_conditions = 'agree_travel_conditions'
id_agree_cancel = 'agree_cancel'
id_confirm_passenger = 'confirm_passenger'
id_confirm_itinerary = 'confirm_itinerary'
port_depart_default = 'NRT' # Narita
abroad_area_default = '0'  # Asia
abroad_country_default = '18' #Viet Nam
abroad_port_default = 'SGN' #ho chi minh
adult_num_default = '1' # 1 -> 9
total_child_num_default = '0' # 0  -> 1
seat_class_default = 'Y' # Y ||  C || F
carrier_default = 'NH'
email_default = 'hxtin002@evo.vn'
# To set up card infomation
# card_number_default = '1234567890'
card_holder_name_default = 'MIMI MIMI'
# card_expiration_month_default = '02'
card_expiration_year_default = '2017'
card_security_code_default = '123'

# To set up new member infomation
# 藤田　泉岐             mizuki fujita
# family_name_kanji_default = '藤田'.decode(sys.stdin.encoding)     # Just accept japanese
# family_name_kana_default = 'ミズキ'.decode(sys.stdin.encoding)   #Mizuki
# first_name_kanji_default =  '泉岐'.decode(sys.stdin.encoding)
# first_name_kana_default = 'フジタ'.decode(sys.stdin.encoding)    #fujta
year_of_birth_default = '1990'
month_of_birth_default = '06' # February, month from 01, 02 to 12
day_of_birth_default = '02' # Day from 01 to 31
nationality_default = 'VNM' # Vietnam
tel_num1_default = '03'
tel_num2_default = '6866'
tel_num3_default = '5956'
password_default = '123456'

#initial
def init(driver, web_address):
    driver.get(web_address)
    driver.implicitly_wait(100)

#Select oneway or round, xpath = xpath_oneway or xpath = round
def select_oneway_or_round(driver, xpath):
    # Click choose oneway or round
    driver.find_element_by_xpath(xpath).click()

#get a city from list
def select_city_value(listx, id):
    return listx[id]

#select a value from element
def select_value_by_id(driver, element_id, value):
    select = Select(driver.find_element_by_id(element_id))
    select.select_by_value(value)

#Select value by xpath
def select_value_by_xpath(driver, xpath, value):
    select = Select(driver.find_element_by_xpath(xpath))
    select.select_by_value(value)

#Select date depart
def select_datepicker(driver, yearx, monthx, dayx, xpath):
    #Click to show calendar
    driver.find_element_by_xpath(xpath_calendar).click()
    xpath = xpath.replace("YEAR", yearx)
    xpath = xpath.replace("MONTH", monthx)
    xpath = xpath.replace("DAY", dayx)
    #Find a date
    driver.find_element_by_xpath(xpath).click()

# Display none
# display = Display(visible=False, size=(screen_width_default, screen_height_default))
# display.start()

# For firefox
# binary = FirefoxBinary(path_firefox)
# caps = DesiredCapabilities.FIREFOX.copy()
# caps[marionette] = True
# driver = webdriver.Firefox(firefox_binary=binary, capabilities=caps, executable_path=path_geckodriver)

# For chrome
path_chromedriver = '/home/hxtin001/Documents/Project/software/chromedriver'
driver = webdriver.Chrome(path_chromedriver)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# log_handle = logging.handlers.TimedRotatingFileHandler('application.log', when='midnight')
log_handle = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] - [%(filename)s:%(lineno)s]- %(levelname)s - %(message)s')
log_handle.setFormatter(formatter)
logger.addHandler(log_handle)

#initial
init(driver, web_address)
logger.info("Connected to {}".format(web_address))

#Select oneway or round, xpath = xpath_oneway or xpath = round
select_oneway_or_round(driver, xpath_oneway)
logger.info("Selected: {} successful".format(xpath_oneway))

# Select port depart
select_value_by_xpath(driver, xpath_selectDomesticAirport, port_depart_default)
logger.info('Selected port depart: {}'.format(port_depart_default))
time.sleep(2)

# Select abroad area
select_value_by_xpath(driver, xpath_abroad_area, abroad_area_default)
logger.info('Selected abroad area: {}'.format(abroad_area_default))
time.sleep(2)

# Select abroad country
select_value_by_xpath(driver, xpath_abroad_country, abroad_country_default)
logger.info('Selected abroad country: {}'.format(abroad_country_default))
time.sleep(2)

# Select abroad port
select_value_by_xpath(driver, xpath_abroad_port, abroad_port_default)
logger.info('Selected abroad port: {}'.format(abroad_port_default))
time.sleep(2)

# Add search criteria
driver.find_element_by_xpath(xpath_search_criteria).click()
logger.info('Click criteria successful')
time.sleep(2)

#Choose depTimes
driver.find_element_by_xpath(xpath_depTime1).click() # 04:00 - 06:59
logger.info('Choose dep time: 04:00 - 06:59')
driver.find_element_by_xpath(xpath_depTime2).click() # 07:00 - 11:59
logger.info('Choose dep time: 07:00 - 11:59')
driver.find_element_by_xpath(xpath_depTime3).click() # 12:00 - 17:59
logger.info('Choose dep time: 12:00 - 17:59')
time.sleep(2)

#Choose date dapart
select_datepicker(driver, '2017', '1', '15', xpath_datepicker) # 2017-01-31
logger.info('Select date depart: {} successful'.format('2017-01-15'))
time.sleep(2)

# Select adult number
select_value_by_xpath(driver, xpath_adult_num, adult_num_default)
logger.info('Select adult number: {} successful'.format(adult_num_default))
time.sleep(2)

# Select child number
select_value_by_xpath(driver, xpath_total_child_num, total_child_num_default)
logger.info('Select total child number: {} successful'.format(total_child_num_default))
time.sleep(2)

# Select seat class
select_value_by_xpath(driver, xpath_seat_class, seat_class_default)
logger.info('Select seat class: {} successful'.format(seat_class_default))
time.sleep(2)

# Select carriers
select_value_by_xpath(driver, xpath_carriers, carrier_default)
logger.info('Select carriers: {} successful'.format(carrier_default))
time.sleep(2)

# Click button search
driver.find_element_by_xpath(xpath_btn_search).click()
logger.info('Click button search successful')
time.sleep(2)

# Select an air flight
driver.implicitly_wait(30)
try:
    driver.find_element_by_xpath(xpath_check_flight_btn).click()
    logger.info('Choose a flight successful')
    time.sleep(2)
    driver.find_element_by_xpath(xpath_select_air).click()
    logger.info('Select a flight successful')
    time.sleep(2)
# Re choose if an axcept occur
except:
    logger.info('Error')
    driver.find_element_by_xpath(xpath_check_flight_btn).click()
    logger.info('Re choose a flight successful')
    time.sleep(2)
    driver.find_element_by_xpath(xpath_select_air).click()
    logger.info('Re select a flight successful')
    pass

# STEP 2
# login with account
driver.implicitly_wait(30)
driver.find_element_by_xpath(xpath_username).send_keys(email_default)
logger.info('Input email: {} succesful'.format(email_default))
time.sleep(1)
ele = driver.find_element(By.XPATH, '//*[@id="member_pass"]/input[contains(@class, "password")]')
ele.click()
ele.send_keys(password_default)
logger.info('Login password: {} successful'.format(password_default))
# Click button register to login
driver.find_element(By.XPATH, xpath_registry_button).send_keys(Keys.ENTER)
logger.info("Clicked registry button successful")

# STEP 3
# Set up user infomation

# Input family name (Alphabet)
# driver.find_element_by_xpath(xpath_family_name1).send_keys(family_name_alphabet_default)
driver.implicitly_wait(50)
familyName = constants.list_alphabet_name[common.select_random_num()]
ac = webdriver.ActionChains(driver)

element = driver.find_element_by_xpath(xpath_family_name1)
element.clear()
ac.key_down(familyName, element)
ac.perform()
logger.info('Input family name: {} successful'.format(familyName))
time.sleep(1)

# Input first name (Alphabet)
firstName = constants.list_alphabet_name[common.select_random_num()]
ele = driver.find_element_by_xpath(xpath_first_name1)
ele.clear()
ac.key_down(firstName, ele)
ac.perform()
logger.info('Input first name: {} successful'.format(firstName))
time.sleep(1)

# # Choose gender = female
# driver.find_element_by_xpath(xpath_sex_female1).click()
# logger.info('Choose gender: {}'.format(xpath_sex_female1))
# time.sleep(1)

# # Input year of birth
# driver.find_element_by_xpath(xpath_year1).send_keys(year_of_birth_default)
# select_value_by_xpath(driver, xpath_month1, month_of_birth_default)
# select_value_by_xpath(driver, xpath_day1, day_of_birth_default)
# logger.info('Input date of birth successful')

# Select user's nationality
select_value_by_xpath(driver, xpath_nationality1, nationality_default)
logger.info('Select nationality: {} successful'.format(nationality_default))
time.sleep(1)


# Set up card infomation
# For login without password
# driver.find_element_by_id(id_card_number).send_keys(card_number_default)
# time.sleep(2)
# Input card holder name
driver.find_element_by_name(name_card_holder).send_keys(card_holder_name_default)
logger.info("Inuput card holder name: {}".format(card_holder_name_default))
time.sleep(1)
# For login without password
# select_value_by_xpath(driver, xpath_card_expiration_month, card_expiration_month_default)
# select_value_by_xpath(driver, xpath_card_expiration_year, card_expiration_year_default)
# Input card security code
driver.find_element_by_name(name_card_security_code).send_keys(card_security_code_default)
logger.info('Input card security code: {}'.format(card_security_code_default))

#### FOR LOGIN WHITHOUT PASSWORD
# # Input family name
# driver.find_element_by_xpath(xpath_family_name2).send_keys(family_name_kanji_default)
# logger.info('Input family name (kanji): {} successful')
# time.sleep(1)

# Input first name
# driver.find_element_by_xpath(xpath_first_name2).send_keys(first_name_kanji_default)
# time.sleep(1)
# logger.info('Input first name (kanji): {} successful')
#
# # Input family name (Katakana)
# driver.find_element_by_xpath(xpath_family_name_kana2).send_keys(family_name_kana_default)
# logger.info('Input family name (katakana) successful')
# time.sleep(1)
#
# # Input fist name (katakana)
# driver.find_element_by_xpath(xpath_first_name_kana2).send_keys(first_name_kana_default)
# logger.info('Input first name (katakana) successful')
# time.sleep(1)
#
# # Input family name by alphabet
# driver.find_element_by_xpath(xpath_family_name_alphabet2).send_keys(family_name_alphabet_default)
# logger.info('Input family name: {} successful'.format(family_name_alphabet_default))
# time.sleep(1)
#
# # Input first name by alphabet
# driver.find_element_by_xpath(xpath_first_name_alphabet2).send_keys(first_name_alphabet_default)
# logger.info('Input first name: {} successful'.format(first_name_alphabet_default))
# time.sleep(1)
#
# # Choose gender = xpath_sex_female2 or gender = xpath_sex_male2
# driver.find_element_by_xpath(xpath_sex_female2).click()
# logger.info('Choose gender: {} successful'.format(xpath_sex_female2))
# time.sleep(1)
#
# # Input year of birth, month of birth, day of birth of the new member
# driver.find_element_by_xpath(xpath_year2).send_keys(year_of_birth_default)
# driver.find_element_by_xpath(xpath_month2).send_keys(month_of_birth_default)
# driver.find_element_by_xpath(xpath_day2).send_keys(day_of_birth_default)
# logger.info('Input date of birth successful')
# time.sleep(1)
#
# # Select nationality
# select_value_by_xpath(driver, xpath_nationality2, nationality_default)
# logger.info('Select nationality: {} successful'.format(nationality_default))
# time.sleep(1)
#
# # Input telephone number
# driver.find_element_by_xpath(xpath_tel_num1).send_keys(tel_num1_default)
# driver.find_element_by_xpath(xpath_tel_num2).send_keys(tel_num2_default)
# driver.find_element_by_xpath(xpath_tel_num3).send_keys(tel_num3_default)
# time.sleep(1)
#
# # Input email
# driver.find_element_by_xpath(xpath_mail_address_confirm).send_keys(email_default)
# logger.info('Input email: {} successful'.format(email_default))
# time.sleep(1)
#
# # Input password
# driver.find_element_by_name(name_password).send_keys(password_default)
# logger.info('Input password: {} successful'.format(password_default))
# time.sleep(1)
#
# # Re input password
# driver.find_element_by_name(name_password_confirm).send_keys(password_default)
# logger.info('Re input password: {} successful'.format(password_default))
# Click to submit input
time.sleep(10)
driver.find_element_by_id(id_submit_input).click()
logger.info('Click to submit successful')

# Conform infomation input

# Re Input family name (Alphabet)
# ele = driver.find_element_by_xpath(xpath_family_name1)
# ele.click()
# ele.clear()
# ele.send_keys(family_name_alphabet_default)
# logger.info('Re input family name: {} successful'.format(family_name_alphabet_default))
# time.sleep(1)
#
# # Re Input first name (Alphabet)
# ele = driver.find_element_by_xpath(xpath_first_name1)
# ele.click()
# ele.clear()
# ele.send_keys(first_name_alphabet_default)
# logger.info('Re input first name: {} successful'.format(first_name_alphabet_default))
# time.sleep(1)

# Re Input card holder name
# driver.find_element_by_name(name_card_holder).send_keys(card_holder_name_default)
# logger.info('Re input card holder name: {}'.format(card_holder_name_default))
# time.sleep(1)
#
# # Re Input card security code
# driver.find_element_by_name(name_card_security_code).send_keys(card_security_code_default)
# logger.info('Re input card security code: {}'.format(card_security_code_default))

# STEP 4
# Click checkbox agree payment
# try:
driver.implicitly_wait(50)
time.sleep(10)
driver.find_element(By.ID, id_agree_payment).click()
logger.info('Go to step 4 successful')
logger.info('Click checkbox: {} successful'.format(id_agree_payment))
time.sleep(2)
# Click checkbox agree travel conditions
driver.find_element_by_id(id_agree_travel_conditions).click()
logger.info('Click checkbox: {} successful'.format(id_agree_travel_conditions))
time.sleep(2)
# Click checkbox agree cancel
driver.find_element_by_id(id_agree_cancel).click()
logger.info('Click checkbox: {} successful'.format(id_agree_cancel))
time.sleep(2)
# Click checkbox confirm passenger
driver.find_element_by_id(id_confirm_passenger).click()
logger.info('Click checkbox: {} successful'.format(id_confirm_passenger))
time.sleep(2)
# Click checkbox confirm itinerary
driver.find_element_by_id(id_confirm_itinerary).click()
logger.info('Click checkbox: {}'.format(id_confirm_itinerary))
time.sleep(2)
# Click to submit
id_submit_booking = 'submit_booking_enabled'
driver.find_element_by_id(id_submit_booking).click()
logger.info('Click to submit booking successful')
logger.info('-------------------END---------------')
# except:
#     logger.info('Error step 4')
#     pass