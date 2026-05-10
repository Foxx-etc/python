"""The program takes Input Value, Compute it until the computed
value not repeating twice, if so then Terminates.

IDEA came from Kaprekar's Constant:
	Kaprekar's constant is the four-digit number 6174, discovered
	by Indian mathematician D. R. Kaprekar. It is a unique number
	in mathematics (base 10) known for its remarkable stability: 
	if you perform a specific routine on almost any four-digit
	number, you will reach 6174 in at most seven steps.

Works with:
	4 digit number, answer always lands at 6174;
	
	3 digit number, answer always lands at 495 but required
	some adjusment during input value."""


def ascen(num: int) -> int:
	num = str(num)
	temp = []
	
	for i in num:
		temp.append(i)
	
	temp.sort()
	return int(''.join(temp))


def descen(num: int) -> int:
	num = str(num)
	temp = []
	
	for i in num:
		temp.append(i)
	
	temp.sort(reverse=True)
	return int(''.join(temp))


def subtract(num2: int, num1: int) -> int:
	return num2 - num1

# -------
num = input("Enter a four didgit number : ")

if len(num) != 4:
	raise ValueError("four digit number required")
# -------

results: list[int, ...] = [num]
	
while True:
	des: int = descen(results[-1])
	asc: int = ascen(results[-1])
	
	answer = subtract(des, asc)
	
	results.append(answer)
	
	if results[-1] == results[-2]:
		break
		
print(results[-1])
