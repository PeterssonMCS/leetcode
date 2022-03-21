class Solution:
    
    def convert(self, s: str, numRows: int) -> str:
        T = 2*numRows - 2
        if T<1:
            T = 1
        t2 = int(T/2)
        r = []
        for j in range(0,len(s)):
            if j%T > t2:
                r.append(t2 -j%t2)
            else:
                r.append(j%T)
        stw = ""        
        for i in range(0,numRows):        
            for j in range(0,len(s)):
                if r[j] == i:
                    stw = stw + s[j]
        return stw
