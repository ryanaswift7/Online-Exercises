encflag = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸彥㜰㍢㐸㙽'

flag = ''
for i in range(0, len(encflag), 1):
	evenflagchar = chr(encflag[i].encode('utf-16be')[0]) # pcCF1_isis3do__7346
	# also evenflagchar = ''.join(chr(ord(encflag[i]) >> 8))
	oddflagchar = chr(encflag[i].encode('utf-16be')[-1])
	flag += evenflagchar
	flag += oddflagchar
	
print("Flag is " + flag)


# p = 112
# i = 105
# c = 99

# flag[0] = 28777
# flag[1] = 25455
# flag[2] = 17236

# Code to generate encflag (Reverse this)
#''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1]))
#		for i in range(0, len(flag), 2)])

# 2 things are happening
# each character in encflag contains 2 characters in flag
# each character in encflag is 2 bytes
# the first byte is the first char, bc the char has been shifted left/up 8 bits/1 byte
# the second byte is the second char
# can encode in 16 bit, which reformats the encflag char into a 2 element array
# the first element in the array is the first byte, which is always at [0]
# the last element is the second byte, which is always at index [-1]
# flag = sequential concatenation of the first and second bytes for each character in encflag
