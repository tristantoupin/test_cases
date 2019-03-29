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
	assert (tm.verify_new_order(context.driver))




