from behave import *
import test_methods as tm


@given(u'that I am logged in')
def step_impl(context):
	driver = tm.setup_webdriver()
	tm.load_heroku(driver)
	tm.login(driver)
	context.driver = driver
	print(context.table)
	pass

@when(u'I select the task manager')
def step_impl(context):
	context.task = "manager"
	tm.select_task(context.driver, context.task)
	assert True is not False

@when(u'I select the task staff')
def step_impl(context):
	context.task = "manager"
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
