class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        new=[]
        rem=[]
        for i in arr2:
            for j in arr1:
                if i==j:
                    new.append(j)
        for i in arr1:
            if i not in arr2:
                rem.append(i)
        rem.sort()
        new.extend(rem)
        return new
        