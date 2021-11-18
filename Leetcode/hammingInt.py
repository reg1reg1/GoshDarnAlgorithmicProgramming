class Solution:
	def hammingDistance(self, x: int, y: int) -> int:
		xor = x ^ y  
		oneBits = 0
		while (xor > 0): 
			oneBits += xor & 1
			xor >>= 1
		return oneBits