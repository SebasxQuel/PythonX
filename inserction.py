def inserction(s1,s2):
	res = []
	for i in s1:
		if i in s2:
			res.append(i)
	return res

inserction([1,3,5,7],[1,2,4,6])s