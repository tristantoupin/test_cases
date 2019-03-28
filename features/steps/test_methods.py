from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_webdriver():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.implicitly_wait(15)
	return driver

def load_heroku(driver):
	driver.get('http://ecse428-potatopeeps.herokuapp.com')

def login(driver, username="user", password="password"):
	username_field = driver.find_elements_by_css_selector(".login-input")[0]
	username_field.send_keys(username)

	password_field = driver.find_elements_by_css_selector(".login-input")[1]
	password_field.send_keys(password)

	login_button = driver.find_element_by_css_selector(".btn.btn-outline-primary")
	login_button.click()

	# time.sleep(5)

def select_task(driver, task):
	task = task.strip().lower()
	tasks = driver.find_elements_by_css_selector(".select-task-columns.d-flex.justify-content-center.flex-column.h-100")
	if(task == "customer"):
		tasks[0].click()
	elif(task == "staff"):
		tasks[1].click()
	elif(task == "manager"):
		tasks[2].click()

	time.sleep(5)

