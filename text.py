data = []
count = 0
with open ('review.txt' , 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 2 == 0:
			print(len(data))
print(len(data))

print(data)
print(data[0])

new = []
for d in data:
	if len(d) < 2:
		new.append(d)
print('一共有',len(new), '比留言長度小於2')