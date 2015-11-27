def new_decorator_one(*args_de,**kw_de):
	def decorator(new_func):
		def wrapper(*args, **kw):
			#print('*args_de:',*args_de)
			print('call begin')
			new_func(*args, **kw)
			print('call end')
		return wrapper
	return decorator