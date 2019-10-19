# 輸入+ - * / 模式運算
# 保留運算結果 加法 減法繼續運算
x = input('請輸入數字 x: ')
y = input('請輸入數字 y: ')
name = input('請輸入您要計算的模式: ')
x = float(x)
y = float(y)
name = int(name)
while name < 5 :
	if name == 1 :
		mode1 = x + y
		print(x, '+', y, '=', mode1)
		if mode1 > 0:
			x1 = input('請輸入數字 x1: ')
			x1 = float(x1)
			name1 = input('請輸入您要計算的模式: ')
			name1 = int(name1)
			if name1 < 5 :
				if name1 == 1 :
					mode2 = mode1 + x1
					print(mode1, '+', x1, '=', mode2)
					break
				elif name1 == 2:  
					mode2 = mode1 - x1
					print(mode1, '-', x1, '=', mode2)
					break
				elif name1 == 3 :
					mode3 = mode1 * x1
					print(mode1, '*', x1, '=', mode3)
					break
				elif name1 == 4 : 
					mode4 = mode1 / x1
					print(mode1, '/', x1, '=', mode4)
					break		
			elif name1 == 0:
				break
			else:
				print('只能輸入 = 1 : 加運算 / 2 : 減運算 / 3 : 乘運算 / 4 : 除運算')
				break			
	elif name == 2:  
		mode2 = x - y
		print(x, '-', y, '=', mode2)
		if mode2 > 0 or mode2 < 0:
			x1 = input('請輸入數字 x1: ')
			x1 = float(x1)
			name1 = input('請輸入您要計算的模式: ')
			name1 = int(name1)
			if name1 < 5 :
				if name1 == 1 :
					mode3 = mode2 + x1
					print(mode2, '+', x1, '=', mode3)
					break
				elif name1 == 2:  
					mode3 = mode2 - x1
					print(mode2, '-', x1, '=', mode3)
					break
				elif name1 == 3 :
					mode3 = mode2 * x1
					print(mode2, '*', x1, '=', mode3)
					break
				elif name1 == 4 : 
					mode4 = mode2 / x1
					print(mode2, '/', x1, '=', mode4)
					break		
			elif name1 == 0:
				break
			else:
				print('只能輸入 = 1 : 加運算 / 2 : 減運算 / 3 : 乘運算 / 4 : 除運算')
				break		
	elif name == 3 :
		mode3 = x * y
		print(x, '*', y, '=', mode3)
		break
	elif name == 4 : 
		mode4 = x / y
		print(x, '/', y, '=', mode4)
		break	
else:
	print('只能輸入 = 1 : 加運算 / 2 : 減運算 / 3 : 乘運算 / 4 : 除運算')