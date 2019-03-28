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

@then('behave will test it for us!')
def step_impl(context):
	assert context.failed is False
