import time

@measure_elapsed_time
def my_fn1(arg1, arg2):
   time.sleep(0.5)
   return arg1 + arg2
