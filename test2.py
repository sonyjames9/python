"""
Each interval is a tuple
(4,6),(0,2),(1,3),(2,5),(7,9)
overlapping merge tuple
(0,2) -> (1,3) = (0,3)
(0,3) -> (2,5) = (0,5)
(0,5) -> (4,6) = (0,6)
Result : (0,6),(7,9)
"""

b = (0, 2)
a = (10, 11)
c = (2, 5)
d = (4, 6)
e = (7, 9)
f = a, b, d, c, e

f = sorted(f)
print(f)
res = f[0]
final_op = ()

for tup_ctr in range(1, len(f)):
	res2 = f[tup_ctr]
	if res2[0] <= res[1] <= res2[1]:
		res = res[0], res2[1]
	else:
		final_op += (res2,)

# print(final_op+(res,))
print(sorted(final_op+(res,)))
