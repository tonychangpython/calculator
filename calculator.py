# 輸入+ - * / 模式運算
x = input('請輸入數字: ')
y = input('請輸入數字: ')
name = input('請輸入您要計算的模式: ')
x = float(x)
y = float(y)
if name == '1': # 加運算
	mode1 = x + y
	print(x, '+', y, '=', mode1)
elif name == '2': # 減運算
	mode2 = x - y
	print(x, '-', y, '=', mode2)
elif name == '3': # 乘運算
	mode3 = x * y
	print(x, '*', y, '=', mode3)
elif name == '4': # 減運算
	mode4 = x / y
	print(x, '/', y, '=', mode4)	
else:
	print('只能輸入 1 : 加運算 / 2 : 減運算 / 3 : 乘運算 / 4 : 除運算')