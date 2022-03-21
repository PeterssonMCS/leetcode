class Solution:
    def intToRoman(self, num: int) -> str:
        n = num
        k = []
        i = 0
        while(n != 0):
            r = n%10
            n = int(n/10)
            k.append(r)
            i = i+1
            
        str = ""
        
        for i in range(0,len(k)):
            if i == 0:
                if k[i] == 4:
                    str = "IV" + str
                if k[i] == 9:
                    str = "IX" + str
                if k[i] >= 1 and k[i] <= 3:
                    str = "I"*k[i] + str
                if k[i] >= 5 and k[i] <= 8:
                    str = "I"*(k[i]%5) + str
                    str = "V" + str
            elif i == 1:
                if k[i] == 4:
                    str = "XL" + str
                if k[i] == 9:
                    str = "XC" + str
                if k[i] >= 1 and k[i] <= 3:
                    str = "X"*k[i] + str
                if k[i] >= 5 and k[i] <= 8:
                    str = "X"*(k[i]%5) + str 
                    str = "L" + str   
            elif i == 2:
                if k[i] == 4:
                    str = "CD" + str
                if k[i] == 9:
                    str = "CM" + str
                if k[i] >= 1 and k[i] <= 3:
                    str = "C"*k[i] + str
                if k[i] >= 5 and k[i] <= 8:
                    str = "C"*(k[i]%5) + str 
                    str = "D" + str
            elif i == 3:
                if k[i] >= 1 and k[i] <= 3:
                    str = "M"*k[i] + str             
        return str
