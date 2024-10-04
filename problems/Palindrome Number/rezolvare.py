class Solution():
	def isPalindrome(self, x: int):
		if x < 0 or x % 10 == 0 and x != 0:
			return False

		ogl = 0
		c = x

		while c != 0:
			ogl = ogl * 10 + c % 10
			c //= 10

		return ogl == x





s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))

