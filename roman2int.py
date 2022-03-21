class Solution:
    def romanToInt(self, s: str) -> int:
        su = 0
        k = []
        for i in s:
            if i =="I":
                k.append(1)
            if i =="V":
                k.append(5)
            if i =="X":
                k.append(10)
            if i =="L":
                k.append(50)
            if i =="C":
                k.append(100)
            if i =="D":
                k.append(500)
            if i =="M":
                k.append(1000)
        
        su = 0
        for j in range(0,len(k)-1):
            if k[j] < k[j+1]:
                su = su - k[j]
            else:
                su = su + k[j]
        
        return su + k[len(k)-1]
