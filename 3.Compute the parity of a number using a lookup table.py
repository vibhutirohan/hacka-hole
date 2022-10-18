# Compute parity of a number `x` using the lookup table
def findParity(x):

	# recursively divide the (32–bit) integer into two equal
	# halves and take their XOR until only 1 bit is left

	x = (x & 0x0000FFFF) ^ (x >> 16)
	x = (x & 0x000000FF) ^ (x >> 8)
	x = (x & 0x0000000F) ^ (x >> 4)
	x = (x & 0x00000003) ^ (x >> 2)
	x = (x & 0x00000001) ^ (x >> 1)

	# return true if the last bit is set
	return (x & 1) == 1


if __name__ == '__main__':

	x = 127

	print(f'{x} in binary is {bin(x)}')

	if findParity(x):
		print(x, 'contains odd bits')
	else:
		print(x, 'contains even bits')
