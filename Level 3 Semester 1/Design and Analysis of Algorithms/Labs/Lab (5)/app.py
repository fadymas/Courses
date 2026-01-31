def count(arr):
    if arr == []:
        return 0
    return  count(arr[1:])+1

arr=[1,2,3,4,6,20]
print(count(arr))

def count_digit(n):
    if n < 10:
        return 1
    return 1+count_digit(n//10)
n=12345
print(count_digit(n))

def findmax(arr):
    if len (arr)==1:
        return arr[0]
    max = findmax(arr[1:])
    return arr[0] if arr[0]>max else max
arr=[3,9,1,4,7]
print(findmax(arr))

def pal(n):
    if len(n) ==1 or 0:
        return True
    if n[0] != n[1]:
        return False
    return pal(n[1:-1])
print(pal("level"))

def is_palindrome(s, left=0, right=None):    
	if right is None:        
		right = len(s) - 1    
	if left >= right:        
		return True    
	if s[left] != s[right]:        
		return False    
	return is_palindrome(s, left + 1, right - 1)
print(is_palindrome("level",0,None))

def min_cost(cost,i):
    if i == 0:
        return 0
    highest=float('inf')
    if i-1>=0:
        highest=min(highest, min_cost(cost,i-1)+cost[i]+[1**2])
    if i-2>=0:
        highest=min(highest, min_cost(cost,i-2)+cost[i]+[2**2])
    if i-3>=0:
        highest=min(highest, min_cost(cost,i-3)+cost[i]+[3**2])
    return highest