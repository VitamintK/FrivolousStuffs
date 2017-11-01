def caesarify(inp, shift):
	output = ""
	for c in inp:
		output+=(' ' if c == ' ' else chr((ord(c)-ord('a')+shift)%26 + ord('a')))
	return output
