PYTHON ERRORS:
	- Syntax Errors
	- Exceptions

TRACEBACK: 
	- a summary that includes the exception type, a message,
	and the series of function calls preseding the exception,
	along with the file names and line numbers.

BUILT-IN EXCEPTION HIERARCHY:

BaseException
 +-- Exception
      +-- StopIteration
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- BufferError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError
      |    +-- KeyError
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError
      +-- ValueError
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError


- raise :Keyword used to raise exceptions at anytime we thin a mistake
has or will occur in our program.

- example: raise NameError('Custom Message')
- example: raise NameError
 
- TRY / EXCEPT:
	- Python will first attempt to execute code inside
	the try clause code block.
	- If no exception is encountered in the code,
	the except clause is skipped and the program continues normally.
	- If an exception does occur inside of the try code block,
	Python will immediately stop executing the code
	and begin executing the code inside
	the except code block (sometimes called a handler)

- example:

 colors = {
    'red': '#FF0000',
    'blue': '#0000FF',
    'yellow': '#FFFF00',
}

for color in ('red', 'green', 'yellow'):
  try:
    print('The hex value of ' + color + ' is ' + colors[color])
  except:
    print('An exception occurred! Color does not exist.')
  print('Loop continues...')


- example: as errorObject
- errorObject :arbitrary, can be named anything
- as :When we specify exception types, Python also allows us to capture the exception object using the 'as' keyword

try:
	print(undefined_var)
except NameError as errorObject:
	print('NameError Message')
	print(errorObject)


- MULTIPLE EXCEPTIONS:

	-list more than one exception type in a tuple with a
	single except clause

try:
	#code to try
except (NameError, ZeroDivisionError) as e:
	print('Error Message')
	print(e)


	- list any number of exceptions in this tuple format as long
	as it makes sense for the code in our try block

	- pair multiple except clauses with a single try clause,
	enabling specific exceptions to be handled differently

try:
	#code to try
exception NameError:
	print('Error Message')
exception KeyError:
	print('Error Message')
exception Exception:
	print('Error Message')

	- be cautious of the order of the exceptions, 
	cover all errors


-ELSE CLAUSE:

	- will only execute if no exception was encountered in the try claus.

try:
	check_password()
except ValueError:
	print('Wrong Password! Try again!')
else:
	login_user()
	# More code


FINALLY CLAUS:

- guarantees that a behavior will occur, regardless of whether an exception
occurs.

try:
	check_password()
except ValueError:
	print('Wrong PAssword! Try again!')
else:
	login_user()
	#more code
finally:
	load_footer() #footer loads reguardless of an exception


- finally can be used independently. 

try:
	check_password()
finally:
	load_footer()
	#other code that always run


- USER DEFINED EXCEPTIONS:

	- exceptions that are created to allow better readibility in our
	program errors

class CustomError(Exception):
	pass

- CustomError is arbitrary, name according to specific exceptions.
- to further build the custom exception:

class CustomError(Exception):
	def __init__(self, arg):
		self.arg = arg

	def __str__(self):
		return 'Error Message'+ str(self.arg)

- instantiate an argument to add into error message

def method(variable):
	if variable = 10:
		raise CustomError(variable)
	else:
		print('Message...')


