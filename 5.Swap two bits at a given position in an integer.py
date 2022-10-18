# Function to swap bits at position `p` and `q` in integer `n`
def swap(n, p, q):

	# if bits are different at position `p` and `q`
	if (((n & (1 << p)) >> p) ^ ((n & (1 << q)) >> q)) == 1:
		n ^= (1 << p)
		n ^= (1 << q)

	return n


if __name__ == '__main__':

	n = 31

	# swap 3rd and 7th bit from the right
	p = 2
	q = 6

	print(n, "in binary is", bin(n)[2:].zfill(8))
	n = swap(n, p, q)
	print(n, "in binary is", bin(n)[2:].zfill(8))
