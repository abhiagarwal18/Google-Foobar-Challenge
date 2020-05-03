def digit_count(x):
    return len(str(x))
    
def get_digits(x, init_k):
    k = digit_count(x)
    digits = []
    while x > 0:
        digits.append(x%10)
        x = int(x) // 10
    for i in range(k, init_k):
        digits.append(0)
    return digits
    
def form_number(digits,b):
    result = 0
    for i in range(0, len(digits)):
        result = result * b + int(digits[i])
    return result
    
def kaprekar_map(x, b, init_k):
    digits = []
    digits = get_digits(x, init_k)
    #print(digits)
    digits.sort();  
    asc = 0;  
    for i in range(init_k): 
        asc = asc * b + digits[i];  
    #print(asc)
    # Get all four dgits in descending order  
    # in the form of number "desc"  
    digits.sort();  
    desc = 0;  
    for i in range(init_k-1, -1, -1): 
        desc = desc * b + digits[i]; 
    #print(desc)
    temp = desc - asc
    if temp == 0:
        return 0
    d = []
    while temp:
        d.append(int(temp % b))
        temp /= b
    return int(''.join(map(str,d[::-1])))
    
def solution(n, b):
    init_k = digit_count(n)
    #print(n)
    seen = []
    count =0
    while n not in seen:
        prev = n
        seen.append(n)
        #print(n)
        n = kaprekar_map(n, b, init_k)
        count = count+1
    temp = kaprekar_map(n, b, init_k)
    if(temp == seen[len(seen)-1]):
        return 1
    else:
        return len(seen) - seen.index(n)

        
def main(): 
    print(solution(1211,10)) 
  
  
# Using the special variable  
# __name__ 
if __name__=="__main__": 
    main() 