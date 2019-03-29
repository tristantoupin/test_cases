from behave import *
import test_methods as tm

@given('we have logged in')
def step_impl(context):
	driver = tm.setup_webdriver()
	tm.load_heroku(driver)
	tm.login(driver)
	context.driver = driver
	pass

@when('we select staff task')
def step_impl(context):
	tm.select_task(context.driver, "staff")
	assert True is not False

@when('we select customer task')
def step_impl(context):
	tm.select_task(context.driver, "customer")
	assert True is not False

@when('we select manager task')
def step_impl(context):
	tm.select_task(context.driver, "manager")
	assert True is not False

@then('we verify we are on staff landing')
def step_impl(context):
	assert (tm.verify_task_page(context.driver, "staff"))

@then('we verify we are on customer landing')
def step_impl(context):
	assert (tm.verify_task_page(context.driver, "customer"))

@then('we verify we are on manager landing')
def step_impl(context):
	assert (tm.verify_task_page(context.driver, "manager"))