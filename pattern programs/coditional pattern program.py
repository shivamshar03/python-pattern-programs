n=int(input("enter a no.:"))
b=input("Enter true or false :")
i=1
while (i<n):
    if b == "true":
        j=1
        while (i>=j):
            print("*",end=" ")
            j+=1
    else:
        j=5
        while (j>i):
            print("*",end=" ")
            j-=1
    print(" ")
    i+=1
