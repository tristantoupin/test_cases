from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

def setup_webdriver():
	driver = webdriver.Chrome(ChromeDriverManager().install())
	driver.implicitly_wait(15)
	return driver

def load_heroku(driver):
	driver.get('http://localhost:8080/')

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

# def select_table(driver):
# 	tables = None
# 	# wait for tables to be loaded
# 	time.sleep(2)
# 	table_select = driver.find_element_by_css_selector(".submit-stn")
# 	table_select.click()

# def select_category(driver):
# 	categories = None
# 	start_time = time.time()
# 	# wait for tables to be loaded
# 	while (categories is None or time.time() - start_time > 10000):
# 		categories = driver.find_element_by_class_name("internal")
# 	category = driver.find_element_by_class_name("internal")[0]
# 	category.click()
# 	on_page = driver.find_element_by_class_name("back")
# 	if on_page:
# 		return True
# 	else:
# 		print("Did not reach the category page!")

def navigate_to_cart(driver):
	back_btn = driver.find_element_by_css_selector(".back")
	back_btn.click()
	while(True):
		try:
			btn_cart = driver.find_elements_by_class_name("landing-page-button")[2]
			btn_cart.click()
			break
		except Exception as e:
			continue
	btn_in_cart = driver.find_elements_by_class_name("cart-help-button")[0]
	if btn_in_cart:
		return True
	else:
		print("Did not reach the cart page!")
		return False

def submit_order(driver):
	btn_cart = driver.find_elements_by_css_selector(".cart-help-button")[2]
	btn_cart.click()
	
	list_items = driver.find_elements_by_class_name("number-input")
	num_list_items = len(list_items)
	while(num_list_items >= 1):
		list_items = driver.find_elements_by_class_name("number-input")
		num_list_items = len(list_items)
	return True
	

def create_order(driver):
	wait = WebDriverWait(driver, 10)
	add_item_to_cart_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button")))
	try:
		add_item_to_cart_button.click()

		return True
	except Exception as e:
		return False

def verify_new_order(driver):
	# driver.get("https://ecse428-potatopeeps.herokuapp.com/#/staff")
	order_numbers = driver.find_elements_by_css_selector(".staff-notification")[2]
	num_orders = int(order_numbers.text.split()[1].strip())
	if(num_orders == 1):
		return True
	else:
		return False


def select_table(driver):
	wait = WebDriverWait(driver, 10)
	table_select = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".submit-stn")))
	table_select.click()

def request_service(driver):
	wait = WebDriverWait(driver, 10)
	service_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Request Service')]")))
	service_btn.click()

def back_to_log_in(driver):
	wait = WebDriverWait(driver, 10)
	icon = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id=\"wrapper\"]/main/header/a/img")))
	icon.click()

def check_help_requests(driver):
	wait = WebDriverWait(driver, 10)
	all_requests_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'All Requests')]")))
	all_requests_btn.click()
	wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Service Request')]")))
	return True

def clear_help_request(driver):
	wait = WebDriverWait(driver, 10)
	request = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Service Request')]")))
	request.click()
	answer_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Answer')]")))
	answer_btn.click()

def select_category(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".internal")))
    categories = driver.find_elements_by_css_selector(".internal")
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".internal")))
    try:
    	categories[0].click()
    	return True
    except Exception as e:
    	return False
    
def select_item(driver):
    wait = WebDriverWait(driver, 10)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".overlay")))
    items = driver.find_elements_by_css_selector(".overlay")
    ActionChains(driver).move_to_element(items[0]).perform()

def verify_description(driver):
	wait = WebDriverWait(driver, 10)
	wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Roasted snap peas with sea salt')]")))
	return True

def navigate_to_bill(driver):
	wait = WebDriverWait(driver, 10)
	bill_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Review Bill')]")))
	bill_btn.click()

def submit_bill_request(driver):
	wait = WebDriverWait(driver, 10)
	request_bill_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Request Bill')]")))
	request_bill_btn.click()
	back_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[@id=\"wrapper\"]/main/header/a")))
	back_btn.click()
	
def check_bill_requests(driver):
	wait = WebDriverWait(driver, 10)
	all_requests_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'All Requests')]")))
	all_requests_btn.click()
	wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Bill Request')]")))
	return True

def clear_bill_request(driver):
	wait = WebDriverWait(driver, 10)
	request = driver.find_element_by_xpath("//*[contains(text(),'Bill Request')]")
	request.click()
	answer_btn = wait.until(ec.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Answer')]")))
	answer_btn.click()

def select_all_orders(driver):
    wait = WebDriverWait(driver, 5)
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".staff-nav-btn")))
    navs = driver.find_elements_by_css_selector(".staff-nav-btn")
    navs[1].click()
    wait.until(ec.visibility_of_any_elements_located((By.CSS_SELECTOR, ".gridViewItem")))

def customer_submits_order(driver):
    back_to_log_in(driver)
    login(driver)
    select_task(driver, "customer")

def staff_changes_status(driver, status):
    back_to_log_in(driver)
    login(driver)
    select_task(driver, "staff")
    select_all_orders(driver)

def check_status(driver):
    status = ["in progress" ,"served", "ready"]
    # check the status in the browser is in status list














