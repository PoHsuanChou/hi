import random
r = random.randint(1, 100)
while True:
	num = input('請輸入')
	num = int(num)
	if num == r:
		print('你猜中了')
		break
	elif num > r:
		print('太大')
	elif num < r:
		print('太小')