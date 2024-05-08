506. Relative Ranks
'''
en an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. 
The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.
'''
Solution:

Approach 1: Using Priority Queue
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        l=[]
        res=['']*len(score)
        position=0
        for i in range(len(score)):
            heapq.heappush(l,(-score[i],i))
        while position <len(score):
            index=heapq.heappop(l)[1]
            if position ==0:
                res[index]='Gold Medal'
            elif position==1:
                res[index]='Silver Medal'
            elif position==2:
                res[index]='Bronze Medal'
            else:
                res[index]=str(position+1)
            position+=1
        return res

Approach 2:
Based on Sorting

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ans=[]
        res=[""]*len(score)
        for i in range(len(score)):
            ans.append((score[i],i))
        ans.sort(key=lambda x:x[0],reverse=True)
        for i in range(len(score)):
            if i==0:
                res[ans[i][1]]="Gold Medal"
            elif i==1:
                res[ans[i][1]]="Silver Medal"
            elif i==2:
                res[ans[i][1]]="Bronze Medal"
            else:
                res[ans[i][1]]=str(i+1)
        return res


        


        
