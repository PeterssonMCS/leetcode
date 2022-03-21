class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return ""
        
        n = int(digits)
        k = []
        while(n > 1):
            r = n % 10
            n = int(n/10)
            k.append(r)
        k.reverse()
        w = []
        for i in k:
            if i == 2:
                w.append("abc")
            if i == 3:
                w.append("def")
            if i == 4:
                w.append("ghi")
            if i == 5:
                w.append("jkl")
            if i == 6:
                w.append("mno")
            if i == 7:
                w.append("pqrs")
            if i == 8:
                w.append("tuv")
            if i == 9:
                w.append("wxyz")
        
        m = []
        
        if len(w) == 1:
            for i in w[0]:
                m.append(i)
        elif len(w) == 2:
            for i in w[0]:
                for j in w[1]:
                    m.append(i+j)
        elif len(w) == 3:
            for i in w[0]:
                for j in w[1]:
                    for k in w[2]:
                        m.append(i+j+k)
        elif len(w) == 4:
            for i in w[0]:
                for j in w[1]:
                    for k in w[2]:
                        for y in w[3]:
                            m.append(i+j+k+y)          
        return m
