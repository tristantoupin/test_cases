from behave import *
import test_methods as tm


@given(u'that I am logged in')
def step_impl(context):
	driver = tm.setup_webdriver()
	tm.load_heroku(driver)
	tm.login(driver)
	context.driver = driver
	pass

@when(u'I select the task manager')
def step_impl(context):
	context.task = "manager"
	tm.select_task(context.driver, context.task)
	assert True is not False

@when(u'I select the task staff')
def step_impl(context):
	context.task = "staff"
	tm.select_task(context.driver, context.task)
	assert True is not False

@when(u'I select the task customer')
def step_impl(context):
	context.task = "customer"
	tm.select_task(context.driver, context.task)
	assert True is not False

@then(u'the landing page of that task is open')
def step_impl(context):
	assert (tm.verify_task_page(context.driver, context.task))

@given(u'that I am logged in as a custumer and browsing a categorie of items')
def step_impl(context):
	driver = tm.setup_webdriver()
	tm.load_heroku(driver)
	tm.login(driver)
	context.driver = driver
	context.task = "customer"
	tm.select_task(context.driver, context.task)
	tm.select_table(context.driver)
	assert (tm.select_category(context.driver))

@when(u'I select an item from the menu to add to my card')
def step_impl(context):
	assert (tm.create_order(context.driver))

@when(u'navigate to the cart')
def step_impl(context):
	assert (tm.navigate_to_cart(context.driver))

@when(u'submit the order')
def step_impl(context):
	assert (tm.submit_order(context.driver))

@then(u'the staff receives a new oder')
def step_impl(context):
	context.driver.quit()
	driver = tm.setup_webdriver()
	context.driver = driver
	tm.load_heroku(context.driver)
	tm.login(context.driver)
	tm.select_task(context.driver, "staff")
	assert (tm.verify_new_order(context.driver))

@given('that I am logged in as a custumer')
def step_impl(context):
    driver = tm.setup_webdriver()
    tm.load_heroku(driver)
    tm.login(driver)
    context.driver = driver
    tm.select_task(context.driver, "customer")
    tm.select_table(context.driver)
    pass

@when('I request the staff for help')
def step_impl(context):
	tm.request_service(context.driver)
	assert True is not False

@when('the staff receives a new help request')
def step_impl(context):
	tm.back_to_log_in(context.driver)
	tm.login(context.driver)
	tm.select_task(context.driver, "staff")
	assert(tm.check_help_requests(context.driver))

@then('the staff clears the request')
def step_impl(context):
	tm.clear_help_request(context.driver)
	assert True is not False

@when('I select a category to browse')
def step_impl(context):
    tm.select_category(context.driver)

@when('selects an item of the menu')
def step_impl(context):
    tm.select_item(context.driver)

@then('I see a description of the item')
def step_impl(context):
    tm.verify_description(context.driver)

@when('I navigate to the bill')
def step_impl(context):
	tm.navigate_to_bill(context.driver)
	assert True is not False

@when('submit a request to the staff to pay the bill')
def step_impl(context):
	tm.submit_bill_request(context.driver)
	assert True is not False

@when('the staff receives a new bill request')
def step_impl(context):
	tm.back_to_log_in(context.driver)
	tm.login(context.driver)
	tm.select_task(context.driver, "staff")
	assert(tm.check_bill_requests(context.driver))

@then('the staff clears the bill request')
def step_impl(context):
	tm.clear_bill_request(context.driver)
	assert True is not False

@given('that I am logged in as a staff')
def step_impl(context):
    driver = tm.setup_webdriver()
    tm.load_heroku(driver)
    tm.login(driver)
    context.driver = driver
    tm.select_task(context.driver, "staff")
    pass

@when('I navigate the orders')
def step_impl(context):
    tm.select_all_orders(context.driver)

@when('the customer submits and order')
def step_impl(context):
    tm.customer_submits_order(context.driver)
"^today is \"([^\"]*)\"$"
@when('changes the status of the order to {status}')
def step_impl(context, status):
    tm.staff_changes_status(context.driver, status)

@then('the status persists')
def step_impl(context):
    tm.check_status(context.driver)

@when('I select to delete a menu item')
def step_impl(context):
	context.menu_item = tm.get_top_menu_item(context.driver)
	tm.delete_menu_item(context.driver)

@then('the menu item is removed')
def step_imple(context):
	assert (tm.check_menu_item_removed(context.driver, context.menu_item))
	
@given(u'that I am logged in as a manager')
def step_impl(context):
	driver = tm.setup_webdriver()
	tm.load_heroku(driver)
	tm.login(driver)
	context.driver = driver
	context.task = "manager"
	tm.select_task(context.driver, context.task)
	assert True is not False

@when(u'I enter the price of an item {price}')
def step_impl(context, price):
	assert (tm.enter_item_price(context.driver, price))

@when(u'I enter the name of an item {name}')
def step_impl(context, name):
	assert (tm.enter_item_name(context.driver, name))

@when(u'I enter the description of an item {description}')
def step_impl(context, description):
	assert (tm.enter_item_description(context.driver, description))
	
@when(u'I enter the inventory of an item {inventory}')
def step_impl(context, inventory):
	assert (tm.enter_item_inventory(context.driver, inventory))

@when(u'I enter the tag of an item {tag}')
def step_impl(context, tag):
	assert (tm.enter_item_tag(context.driver, tag))

@when(u'submits the item')
def step_impl(context):
	assert (tm.submit_item(context.driver))

@then(u'the item with name {name} persists')
def step_impl(context, name):
 	assert (tm.item_persists(context.driver, name))

@when('I select to update a menu item')
def step_impl(context):
	context.top_menu_item = tm.get_top_menu_item(context.driver)
	assert (tm.select_update_item(context.driver, context.top_menu_item))
	
@when('I submit a valid new quantity')
def step_impl(context):
	context.new_quant = tm.input_new_quantity(context.driver, context.top_menu_item)

@then('the menu item quantity is changed')
def step_impl(context):
	assert (tm.check_menu_item_quant_updated(context.driver, context.top_menu_item, context.new_quant))
	

