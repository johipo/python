#A = [4, 5, 3, 8, 7, 1, 10, 2]
A = [-2, -3, -4, 0, 1, -6, 2, 3, -10, 14, 5, -290]

def lista(A):
    print(f"O numero de elem: {len(A)}")


def solution(A):
    i = 0
    if 1 not in A or max(A)<=0:
        return 1
    else:
        newA = sorted(A)
        for i in range(i,len(newA)):
            if(newA[i] >= 0):
                if((i == len(newA)-1)) or ((newA[i+1] - newA[i]) > 1):
                    return newA[i] +1 
                    
print(solution(A))