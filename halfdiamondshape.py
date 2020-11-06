def recursion(S):
    for i in range(S):
        for j in range(0,i+1):
            print('*',end=" ")
        print()
    for i in range(1,S):
        for j in range(i,S):
            print('*',end=" ")
        print()
#driver code
S=5
recursion(S)