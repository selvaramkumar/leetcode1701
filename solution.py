class Solution:
    def averageWaitingTime(self, customers) -> float:
        sum_of=0
        for i in range(0,len(customers)):
            if i==0:
                customers[i].append(customers[i][0]+customers[i][1])
                sum_of=sum_of+customers[i][2]-customers[i][0]
               
            else:
                if customers[i][0] <customers[i-1][2]:
                    customers[i].append(customers[i-1][2]+customers[i][1])
                    sum_of=sum_of+(customers[i][2]-customers[i][0])
                    
                else:
                    customers[i].append(customers[i][0]+customers[i][1])
                    sum_of=sum_of+(customers[i][2]-customers[i][0])       
        return  sum_of/len(customers) 

s=Solution()
a=[[1,2],[2,5],[4,3]]
print(s.averageWaitingTime(a))     