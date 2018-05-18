# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from pyvirtualdisplay import Display
import logging.handlers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import common
import constants
import selenium.common.exceptions
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


xpath_one_way  = '//*[@id="searchcondition-container"]/ul/li[1]/section/div/div[1]/ul/li[2]'
web_address = "http://uat001:YQNeuFbadirY@au-uat2.dev.skygate-global.com/"
id_from_input = "from_input"
id_to_input = "to_input"
id_search_btn = 'search-button'
xpath_suggest_city = 'ui-id-124'


# For display none
# display = Display(visible=False, size=(constants.screen_width_default, constants.screen_height_default))
# display.start()

# For chrome
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_handle = logging.handlers.TimedRotatingFileHandler(constants.path_application_log, when='midnight')
# log_handle = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] - [%(filename)s:%(lineno)s]- %(levelname)s - %(message)s')
log_handle.setFormatter(formatter)
logger.addHandler(log_handle)
logger.info('-----------START-----------')

#initial
try:
    driver = webdriver.Chrome(constants.path_chromedriver)
    common.init(driver, web_address)
    logger.info("Connected to {}".format(web_address))
except Exception as e:
    logger.info('Can not connect to website. Error: {}.'.format(e))
    raise e

try:
    driver.find_element_by_xpath(xpath_one_way).click()
    ele = driver.find_element_by_id(id_from_input)
    ele.send_keys('Sydney (AU)')
    driver.find_element_by_id('ui-id-4').click()

    driver.find_element_by_id(id_to_input).send_keys('Melbourne Avalon')
    driver.find_element_by_id('ui-id-5').click()

    time.sleep(5)
    driver.find_element_by_id(id_search_btn).click()
except Exception as e:
    pass