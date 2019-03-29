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

def select_task(driver, task):
	tasks = driver.find_elements_by_css_selector(".select-task-columns.d-flex.justify-content-center.flex-column.h-100")
	if(task == "customer"):
		tasks[0].click()
	elif(task == "staff"):
		tasks[1].click()
	elif(task == "manager"):
		tasks[2].click()
	else:
		print("Incorrect Task Selected! [customer, staff, manager]")
	
	time.sleep(1) # just proof it worked for the human eye


def verify_task_page(driver, task):
	if(task == "customer"):
		table_select = driver.find_element_by_css_selector(".submit-stn")
		if(table_select):
			return True
	elif(task == "staff"):
		staff_requests = driver.find_elements_by_css_selector(".staff-nav-btn")
		if(len(staff_requests) == 2):
			return True
	elif(task == "manager"):
		manager_button = driver.find_element_by_css_selector(".btn.btn-primary.btn-block.btn.btn-primary")
		if(manager_button):
			return True
	else:
		print("Incorrect Task Selected! [customer, staff, manager]")

def select_table(driver):
	tables = None
	# wait for tables to be loaded
	time.sleep(2)
	table_select = driver.find_element_by_css_selector(".submit-stn")
	table_select.click()

def select_category(driver):
	categories = None
	start_time = time.time()
	# wait for tables to be loaded
	while (categories is None or time.time() - start_time > 10000):
		categories = driver.find_element_by_class_name("internal")
	category = driver.find_element_by_class_name("internal")[0]
	category.click()
	on_page = driver.find_element_by_class_name("back")
	if on_page:
		return True
	else:
		print("Did not reach the category page!")

def navigate_to_cart(driver):
	btn_cart = driver.find_element_by_class_name("landing-page-button")[2]
	btn_cart.click()
	btn_in_cart = driver.find_element_by_class_name("cart-help-button")[0]
	if btn_in_cart:
		return True
	else:
		print("Did not reach the cart page!")

def submit_order(driver):
	btn_cart = driver.find_element_by_css_selector("cart-help-button.fas.fa-cart-arrow-down")[2]
	btn_cart.click()
	list_items = driver.find_element_by_class_name("customer-cart-table-rows")[0]
	if len(list_items) <= 1:
		return True
	else:
		print("Did not submit order!")

def create_order(driver):
	#TODO
	pass

def verify_new_order(driver):
	driver.get("https://ecse428-potatopeeps.herokuapp.com/#/staff")
	order_numbers = driver.find_element_by_css_selector(".staff-notification")
	print(order_numbers)
	print(order_numbers)
	print(order_numbers)
	print(order_numbers)
	print(order_numbers)
	print(order_numbers)














