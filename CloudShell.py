# -*- coding: utf-8 -*-
import time
from selenium import webdriver
# from pyvirtualdisplay import Display
import logging.handlers
from selenium.webdriver.common.keys import Keys
import constants
import json

# For display none
# display = Display(visible=True, size=(constants.screen_width_default, constants.screen_height_default))
# display.start()

# For chrome
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
log_handle = logging.handlers.TimedRotatingFileHandler(constants.path_application_log, when='midnight')
# log_handle = logging.StreamHandler()
formatter = logging.Formatter('[%(asctime)s] - [%(filename)s:%(lineno)s]- %(levelname)s - %(message)s')
log_handle.setFormatter(formatter)
logger.addHandler(log_handle)

class CloudShell:

    driver = None
    config = None
    cases = []

    def __init__(self):
        logger.info('----------------------------START--------------------------------')
        self.load_data_json()
        try:
            self.driver = webdriver.Chrome(self.config.get('DRIVER_PATH'))
            self.driver.get(self.config.get('WEB_URL'))
            self.driver.implicitly_wait(100)
            logger.info("Connected to {}".format(self.config.get('DRIVER_PATH')))
        except Exception as e:
            logger.info('Can not connect to website. Error: {}.'.format(e))
            raise e

    def load_data_json(self, fileName='data.json'):
        try:
            with open(fileName) as json_data:
                data = json.load(json_data)
            self.config = data.get("CONFIG")
            self.cases = data.get("CASE")
        except Exception as e:
            logger.error('Cannot load data from json. Error: {}.'.format(e))
            raise e

    def run(self):
        try:
            for case in self.cases:
                # Send username
                usernameEle = self.driver.find_element_by_css_selector("input[type='email']")
                usernameEle.send_keys(case.get('USERNAME'))

                # Click next button
                self.driver.find_element_by_css_selector("div#identifierNext span.RveJvd.snByac").click()
                time.sleep(2)

                # Sen password
                passEle = self.driver.find_element_by_css_selector("input[type='password']")
                passEle.send_keys(case.get('PASSWORD'))

                # Click next button to login
                self.driver.find_element_by_css_selector("div#passwordNext span.RveJvd.snByac").click()
                time.sleep(20)

                # Move to frame contain terminal
                frame = self.driver.find_element_by_css_selector("div.p6n-devshell-background.layout-column iframe.p6n-devshell-frame.layout-fill")
                self.driver.switch_to.frame(frame)

                # Move to frame terminal
                terminalFrame = self.driver.find_element_by_css_selector("body.dark-theme.iframed div#terminal iframe")
                self.driver.switch_to.frame(terminalFrame)

                # Send script
                terminal = self.driver.find_element_by_css_selector("textarea[tabindex='-1']")
                terminal.send_keys(case.get("COMMAND"))
                terminal.send_keys(Keys.RETURN)
        except Exception as e:
            logger.info('Step 1 error: {}'.format(e.message))
            raise e

def _main():
    CloudShell().run()

if __name__ == '__main__':
    _main()







