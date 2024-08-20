def print1toN(n):
    if n<=0:
        return

    print1toN(n-1)
    print(n)

n=int(input("Enter the number to print n natral "))
print1toN(n)


def print1toN(n):
    if n<=0:
        return
    print(n)
    print1toN(n-1)


n=int(input("Enter the number to print n natral "))
print1toN(n)