import random
start = input('初始值')
end = input('結束值')
start = int(start)
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	count += 1 
	num = input('請輸入')
	num = int(num)
	if num == r:
		print('你猜中了')
		break
	elif num > r:
		print('太大')
	elif num < r:
		print('太小')
	print('這是你猜的地', count ,'次' )