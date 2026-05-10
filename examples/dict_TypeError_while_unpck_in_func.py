

rrr = {
"a":1,
"b":2,
"c":3
}

"""
In here, the **kwargs will unpack a dictionary in f(),
in which the keys are : a, b, c.

If I try to place pos-or-key parameter as name : a, b, c
may raise an TypeError: f() got multiple values of argument 'b'

for e.g.
	f(b, *args, a, b, c)
"""

def f(b, *args, **kwargs):
	new = kwargs
	val = []	
	for i in new.values():
		val.append(i)

	return args + tuple(val)

print(f(7,8,9, **rrr))


