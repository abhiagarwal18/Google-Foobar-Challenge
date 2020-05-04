def solution(s):
    # Your code here
    count = 0;
    arr = []
    for i in range(len(s)):
        if(s[i] == ">"):
            arr.append("r")
        elif s[i]=="<":
            arr.append("l")
        else :
            continue
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if( arr[i] == "r" and arr[j] =="l"):
                count = count + 1
                
    return count*2
