import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestStep1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_step1(self):
        # Test name: step1
        self.driver.get("https://wwws.palermo.edu/cgi-bin/inscripcion/form.pl")
        self.driver.set_window_size(1382, 736)
        self.driver.find_element(By.ID, "nombre").click()
        self.driver.find_element(By.ID, "nombre").send_keys("Cristian Camilo")
        self.driver.find_element(By.ID, "apellido").click()
        self.driver.find_element(By.ID, "apellido").send_keys("Reyes Rodri")