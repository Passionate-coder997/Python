def factorial():
    n=input()
    fact=1
    for i in range(1,int(n)+1):
        fact=fact*i
    print(fact)


factorial()