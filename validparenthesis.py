class Solution:
    def isValid(self, s: str) -> bool:
        s1 = 0
        s2 = 0
        s3 = 0
        seq = []
        for i in s:
            if i =='(':
                s1 = s1+1
                seq.append(1)
            elif i ==')':
                if seq == []:
                    return False
                if seq[-1] == 1:
                    seq.pop(-1)
                else:
                    return False
                s1 = s1-1
            if i =='[':
                s2 = s2+1
                seq.append(2)
            elif i ==']':
                if seq == []:
                    return False
                if seq[-1] == 2:
                    seq.pop(-1)
                else:
                    return False
                s2 = s2-1
            if i =='{':
                s3 = s3+1
                seq.append(3)
            elif i =='}':
                if seq == []:
                    return False
                if seq[-1] == 3:
                    seq.pop(-1)
                else:
                    return False
                s3 = s3-1
            if s1 < 0 or s2 < 0 or s3 < 0:
                return False
        if s1 == 0 and s2 ==0 and s3 == 0:
            return True
