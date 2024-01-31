print("Введите число.")

n = int(input())
a = []
start = ""
finish = ""

for i in range(1, n+1):
    start += str(i)
    a.append(start+finish[::-1])
    finish += str(i)

for k in a:
    print(k)
