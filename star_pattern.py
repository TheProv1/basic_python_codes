#Method 1
n = int(input("Enter the number of rows: "))

for i in range(0,n+1):
	print('*'*i)

#Method 2
n = int(input("Enter the number of rows: "))
for i in range(n+1):
	for j in range(i+1):
		print('* ',end='')
	print("\n")
