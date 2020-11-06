def fine():
    actual=input().split()
    fine = 0
    a_d= int(actual[0])
    a_m= int(actual[1])
    a_y= int(actual[2])
    expected= input().split()
    e_d= int(expected[0])
    e_m= int(expected[1])
    e_y= int(expected[2])
    if(a_y>e_y):
        fine = 10000
    elif a_y==e_y:
        if a_m>e_m:
            fine = (a_m-e_m)*500
        elif a_m==e_m and a_d>e_d:
            fine = (a_d-e_d)*15
    print(fine)

fine()