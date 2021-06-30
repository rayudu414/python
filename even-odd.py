for i in range(1,10):
    if i%2==0:
        if i==4:
            continue
        print(i, "is even number")
    elif i%2!=0:
        print(i,"is odd number")
