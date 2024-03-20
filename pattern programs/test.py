import pattarn_program
t=float(input())
n=4
def shortcut():
    pattarn_program.star()
    pattarn_program.space()
    pattarn_program.star()
    print("")
while (n >= 1):
    shortcut()
    n -= 1
n = 2
while (n <= 4):
    shortcut()
    n += 1
