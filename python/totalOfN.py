import sys
def recursion(n):
    if n == 1:
        return 1
    return n*recursion(n-1)
sys.setrecursionlimit(1000)
n = 1
while True:
    try:
        print(str(recursion(n)))
        n += 1
    except(RecursionError):
        print("Đã vượt quá giới hạn")
        break
# def tong(n):
#     result = 0
#     for i in range(1,n + 1):
#         result += i
#     return result
#
# print(tong(100000))