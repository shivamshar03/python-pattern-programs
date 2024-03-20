import time
t=float(input())
n=4
def space():
    k = 1
    a = 1
    while (a <= 2 * (n - k)):
        print("   ", end="")
        a += 1
def star():
    j = 4
    while (j >= n):
        time.sleep(t)
        print(" * ", end="")
        j -= 1
while(n>=1):
    star()
    space()
    star()

    print("")
    n-=1

n=2
while(n<=4):
    star()
    space()
    star()

    print("")
    n+=1
