def add(x, y):
	return x + y
	
def substract(x, y):
	return x - y
    


# 取出所有物件的名稱，排除 magic object	
dir = dir()
__objname__ = [o for o in dir if not '__' in o]

if __name__ == '__main__':
	print(globals())