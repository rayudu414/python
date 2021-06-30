number=int(input("enter a number : "))
for num in range(2,number):
    if number%num == 0:
        print("given number is not prime")
        break
else:
    print("given number is prime") 


num=int(input("enter a range : "))

for i in range(1,num):
    

    for j in range(2,i):
        if i==1:
            print(i,"given number is not prime")
           

        elif i%j==0:
            print(i,"given number is not prime")
            break
    else:
        print(i,"given number is prime")
