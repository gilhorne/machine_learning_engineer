UNIT TESTING


- MANUAL TESTING:
	- a physical person interacts with software.


- AUTOMATED TESTING:
	- tests are performed with code. (more efficient)


---


-assert Statment:
	- used to test that a condition is met.
	If the condition evaluates to False, 
	an AssertionError is raised with an optional error message.

	syntax: assert <condition>, 'Message if condition is not met'

#unit to test#

def times_ten(number):
	return number * 100

#test case 1#

result = times_ten(20)
assert result == 200, 'Expected times_ten(20) to return 200,
instead got ' + str(result)

- test case:

	- validates that a specific set of inputs produces an expected
	output for the unit getting tested.

	- test uniqe input types per unit.


---


- unittest Framework:
	#import unittest module#

	import unittest

	- unittest module provides a test runner,
	a component that collects and executes test,
	then provides resultes to the user.
	
-STEPS TO USE UNITTEST FRAMEWORK:

#1: Create a class which inherits from unittest.TestCase

import unittest

class TestTimesTen(unittest.TestCase):


#2: Create test functions as methods to the class

	def test_multiply_ten_by_zero(self):
		pass
	
	def test_multiply_ten_by_one_million(self):
		pass

	def test_multiply_ten_by_negative_number(self):
		pass


#3: Use assertEqual method of unittest.TestCase

	def test_multiply_ten_by_zero(self):
		self.assertEqual(times_ten(0), 0,
		'Expected times_ten(0) to return 0')

	def test_multiply_ten_by_one_million(self):
		self.assertEqual(times_ten(1000000), 10000000,
		'Expected times_ten(1000000) to return 10000000')

	def text_multiply_ten_by_negative_number(self):
		self.assertEqual(times_ten(-10), -100, 
		'Expected times_ten(-10) to return -100')


#4: Run unittest.main() to run tests

unittest.main()


---


- assertEqual syntax:

def test_method(self):
	self.assertEqual(unit(var), output, 'Test Message')


- ASSERT METHODS I :Equality and Membership

	- assertEqual() :takes two values as argumetns and checks that they are equal.
	If not, the test fails.

		- self.assertEqual(value1, value2)

	
	- assertIn() :takes two arguments. It checks that the first argument is found in the second atrgument,
	which should be a container. If it is not found in the container, the test fails.

		- self.assertIn(value1, container)

	
	- assertTrue() :takes a single argument and checks that the argument evaluates to True.
	If it does not evaluate to True, the test fails.

		- self. assertTrue(value)


- ASSERT METHODS II :Quantitative Methods

	- assertLess() :takes two argumetns and checks that the first argument is less than the second one.
	If it is not, the test will fail.

		- self.assertLess(value1, value2)


	- assertAlmostEqual() :takes two argumaents and checks that thier difference,
	when rounded to 7 decimal places, is 0. If values are not close enough to equality,
	the test will fail.

		- self.assertAlmostEqual(value1, value2)


- ASSERT METHODS III :Exceptions and Warning Methods

	- assertRaises() :takes an exception type as its first argument,
	a function reference as its second, and an arbitrary number of
	arguments as the rest.

	- It calls the function and checks if an exception is raised as
	as result.
 
	- the test passes if ana exception is raised or fails is no
	exception is raised,
	
	- This method can used with custom exceptions. 
	
  		- self.assertRaises(specificException, function,
		functionArguments...)


	- assertWarns() :takes a warning type as its first argument,
	a function reference as its second, and an arbitrary number
	of arguments for the rest.

	- it calls the function and checks that the warning occurs.
	the test passes if a warning is triggered ans fails if it isn't.

		- self.assertWarns(specificWarningExcpetion, function,
		functionArguments...)

## SAMPLE CODE 1 (alerts.py file)

``` python 
import warnings

class PowerError(Exception):
    pass

class WaterLevelWarning(Warning):
    pass

def power_outage_detected(outage_detected):
    if outage_detected:
        raise PowerError('A power outage has been detected somewhere in the system')
    else:
        print('All systems receiving power')

def water_levels_check(liters):
    if liters < 200:
        warnings.warn('Water levels have fallen below 200 liters', WaterLevelWarning)
    else:
        print('Water levels are adequate')
``` 


# SAMPLE CODE 2 (tests.py file)

import unittest
import alerts

### Write your code here:
class SystemAlertTests(unittest.TestCase):

  def tests_power_outage_alert(self):
    self.assertRaises(alerts.PowerError, alerts.power_outage_detected, True)

  def test_water_levels_warning(self):
    self.assertWarns(alerts.WaterLevelWarning, alerts.water_levels_check, 150)

unittest.main()


- PARAMETERIZING TESTS : subTest

	- test parameterization :leverage the functionality of a single test 
	to get a large amount of coverage of different inputs.


import unittest

### the function we want to test:

def times_ten(number):
	return number * 100 #(this will cause it to fail)

### our test class:

class TestTimesTen(unittest.TestCase):

	# test method:
	def test_times_ten(self):
		for num in [0, 1000000, -10]:
			with self.subTest(num):
				expected_result = num * 10
				message = 'Expected times_ten(' + str(num) + ') to
				return ' + str(expected_result)
				self.asserEqual(times_ten(num), expected_result,
				message)


- we can test a collection of inputs by using a loop
followed by a with statement and our subTest context manager

- by using subTest, each iteration of our loop is treated as an individual test. 

- Python will run the code inside of the context manager on each iteration, 
and if one fails, it will return the failure as a separate test case failure.


- TEST FIXTURES:

	- One of the most important principles of testing is that tests need to
	occur in a known state.

	- If the conditions in which a test runs are not controlled, then results
	could contain false negatives (invalid failed results) or false
	positives (invalid passed results)

	- test fixture is a mechanism for ensuring proper:
		
		- setup() :putting tests into a known state
 
		- teardown() :restoring the state prior to the test
		running

# SAMPLE CODE 1: setUp/tearDown 
- Runs setUp and tearDown after ever test.

def power_cycle_device():
	print('Power Cycling device...')

class DeviceTests(unittest.TestCase):
	def setUp(self):
		power_cycle_device()

	def test_feature_a(self):
		print('Testing feature A...')

	def test_feature_b(self):
		print('Testing feature A...')

	def tearDown(self):
		power_cycle_device()




### SAMPLE CODE 2: 
- Runs all tests within setUp before tearDown. 

def power_cycle_device():
	print('Power Cycling Device...')

class DeviceTests(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		power_cycle_device()

	def test_feature_a(self):
		print('Testing feature A...')

	def test_feature_b(self):
		print('Testing feature B...')

	@classmethod
	def tearDown(cls):
		power_cycle_device()



- SKIPPING TESTS: 

	- runs tests in particular context.
	

	- @unittest skip decorator

--- SAMPLE CODE 1: skip decorators:

- @unittest.skipUnless(condition, "string_message")
	:skips the test if the condition evaluates to False.

- @unittest.skipIf(condition, "string_message") 
	:skips the test if the condition evaluates to True.


	- skipTest() method

--- SAMPLE CODE 2: skipTest method:

- self.skipTest("string_message")
	:will always cause the test to skip.



- EXPECTED FAILURES:

	- mark test as expected failure, due to known bugs 
	or is designed to fail on purpose.

	- counted as passed in test results

	- if test passes when expected to fail, it is marked 
	as failed in test results


	- @unittest.expectedFailure

--- SAMPLE CODE 1:

class FeatureTests(unittest.TestCase):

	@unittest.expectedFailure
	def test_broken_feature(self):
		raise Exception('This test is going to fail')

