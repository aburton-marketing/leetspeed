import re
import regexp as rp

# extracts only the variables
def getparams(s):
	x = rp.params_c.findall((s[s.index("(")+1:s.index(")")]))
	for i in range(len(x)):
		if len(x) > 1 and i < len(x)-1 and x[i]:
			x[i] = str(x[i])
			x[i] += ','
		else:
			x[i] = str(x[i])
	# adds a space if there is a comma (optional)
	def listToString(s):
		str1 = " "
		print(str1)
		return (str1.join(s))
	# replaces everything inbetween paranthesis. i.e def(.......)
	s = s.replace(s[s.index("(")+1:s.index(")")],listToString(x))
	# replaces everything after parenthesis. i.e int ->:
	s = s.replace(s[s.index(")")+1:len(s)],':')
	return s
	
# renames the file
def setName(f_name):
	str1 = ""
	de = rp.defname_c.findall(f_name)[0][:-1]
	str1 = str(de) + ".py" 
	return str1

if __name__ == "__main__":
	pass

