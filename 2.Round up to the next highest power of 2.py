# Compute power of two greater than or equal to `n`
def findNextPowerOf2(n):

	# decrement `n` (to handle cases when `n` itself
	# is a power of 2)
	n = n - 1

	# do till only one bit is left
	while n & n - 1:
		n = n & n - 1   	# unset rightmost bit

	# `n` is now a power of two (less than `n`)

	# return next power of 2
	return n << 1


if __name__ == '__main__':

	n = 127
	print('The next power of 2 is', findNextPowerOf2(n))
