
def recursion(n,fr,to,between):
    if(n == 0):
        return
    recursion(n - 1,fr,between,to)
    print("Chuyển đĩa: " + str(n) + " từ cột " + fr + " sang cột " + to)
    recursion(n - 1,between,to,fr)

if __name__ == "__main__":
    n = int(input())
    recursion(n,"A","C","B")