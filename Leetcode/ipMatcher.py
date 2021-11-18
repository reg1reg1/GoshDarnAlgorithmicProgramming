import re
class Solution:
	def validIPAddress(self, IP: str) -> str:
		
		ans= ["IPv4","IPv6","Neither"]	
		X =  IP.find('.') > 0
		Y =  IP.find(':') > 0

		if not(X^Y):
			return ans[3]

		else:
			if X:
				octets = IP.split('.')
				O = len(octets)
				if O!=4:
					return ans[2]
				else:
					#The first octet can be 0 only when the ip is 0.0.0.0
					#The other octets may be zero but 19.007.55.098 is not a valid IP
					if IP=='0.0.0.0':
						return ans[0]
					else:
						oct1="(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[1-9])"
						octR="(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])"
						_rex1 = re.compile(oct1)
						_rex2 = re.compile(octR)
						if not _rex1.fullmatch(octets[0]):
							#print("HERE")
							return ans[2]	
						for x in range(1,O):
							if not _rex2.fullmatch(octets[x]):
								#print("HERE-2")
								return ans[2]
						return ans[0]


			else:
				ipv6Rx = "([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}|(\d{1,3}\.){3}\d{1,3}"
				_rex3 = re.compile(ipv6Rx)
				if not _rex3.fullmatch(IP):
					return ans[2]
				return ans[1]

def main():
	s = Solution()
	x="193.234.213.105"
	print(s.validIPAddress(x))

if __name__ == '__main__':
	main()

