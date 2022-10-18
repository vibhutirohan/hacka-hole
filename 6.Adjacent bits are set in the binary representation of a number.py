# Returns true if adjacent bits are set in the binary representation of `n`
def check(n):
	return (n & (n << 1)) != 0


if __name__ == '__main__':

	n = 67
	print(f'{n} in binary is {bin(n)}')

	if check(n):
		print('Adjacent pair of set bits found')
	else:
		print('No adjacent pair of set bits found')
