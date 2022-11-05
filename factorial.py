num = int(input('Enter the number whose factorial must be calculated: '))
factorial = 1

for i in range(0, num+1):
	factorial*=i

print("The factorial of",num,"is:", factorial)
