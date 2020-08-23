def trap(height):
        
    lst = []
    res = 0
        
    for i in range(len(height)):
            
        if len(lst) == 0:
            lst.append([height[i], i])
        else:
            if height[i] < lst[-1][0]:
                lst.append([height[i], i])
                    
            elif height[i] == lst[-1][0]:
                lst[-1][1] = i
                    
            else:
                while len(lst)>1 and lst[-1][0] <= height[i]:
                    if height[i] > lst[-2][0]:
                        res += (lst[-2][0] - lst[-1][0]) * (i - lst[-2][1] - 1)
                        lst.pop()
                    else:
                        res += (height[i] - lst[-1][0]) * (i - lst[-2][1] - 1)
                        lst.pop()
                    
                if lst[-1][0] <= height[i]:
                    lst.pop()
                        
                lst.append([height[i], i])
                    
    return res
                    
test = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(test))               
        
                
                    
        