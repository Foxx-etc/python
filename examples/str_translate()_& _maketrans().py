t = [
"at",
"by",
"cu",
"di",
"er",
"fe",
"gw",
"ho",
"iq",
"jp",

"kg",
"lf",
"md",
"ns",
"oa",
"ph",
"qj",
"rk",
"sl",

"tv",
"ux",
"vc",
"wb",
"xz",
"yn",
"zm",
]

d = dict(t)

while True:
	user = input("Enter : ")
	convert  = user.maketrans(d)
	
	result = user.translate(convert)
	print(result)
