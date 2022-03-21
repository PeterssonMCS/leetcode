class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        k = []
        while(n != 0):
            r = n % 10
            n = int(n/10)
            k.append(r)
        k.reverse()
        s = 0
        for i in range(0,len(k)):
            s = s + k[i]*pow(10,i)
        
        if x - s == 0:
            return True
        else:
            return False
