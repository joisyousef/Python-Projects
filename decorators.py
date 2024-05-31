from datetime import datetime
import time

def logger(func):
	def wrapper():
		print("-"*50)
		print("> Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
		func()
		print("> Execution finished {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
		print("-"*50)
	return wrapper

@logger
def demo_func():
	print("Execution task!")
	time.sleep(3)
	print("task completed!")

#demo_func()

def logger_args(func):
	def wrapper(*args,**kwargs):
		print("-"*50)
		print("> Execution started {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
		func(*args,**kwargs)
		print("> Execution finished {}".format(datetime.today().strftime("%Y-%m-%d %H:%M:%S")))
		print("-"*50)
	return wrapper

@logger_args 
def demo_func_args(sleep_time):
	print("Execution task!")
	time.sleep(sleep_time)
	print("task completed!")

demo_func_args(1)	
