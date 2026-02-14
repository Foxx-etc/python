
# fibonacci Series Generation Using List 
def fibonacci(n):
	n = 7int(n)
	a = [0,1]
	if n<0 or n==0:
		return "Number Cannot be Negative!" if n<0 else "Number Cannot be 0!"
	elif n==1:
		return a[0]
	else:
		for i in range(n-2):
			a.append(a[-1] + a[-2])
	return a
	
if __name__ == '__main__':
	user = input("Enter nth Number To Generate fibonacci Series : ")
	print(fibonacci(user))
