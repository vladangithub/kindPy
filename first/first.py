# print('Hello Python!')
#
# print(125 + 7)
#
# qwerty = float(input('Число?:'))
# asdf = qwerty / 123
# print(f'{asdf:.2f}')

#3. Переменные, оператор присваивания, функции type и id

# a = 7
# print(a)
#
# a, b = 0, 12
# print(a, b)
# a, b = b, a
# print(a, b)
#
# print( id(a), id(b))

# q = 5.8
# w = 'Hello'
#
# print(type(q), type(w))

# var_a = 5

# d = int(input())
# print(abs(d))

# d1, d2, d3, d4, d5 = map(int, input().split())
# print(min(d1, d2, d3, d4, d5))

# d1, d2, d3, d4, d5 = map(int, input().split())
# print(max(d1, d2, d3, d4, d5))

# a, b = map(int, input().split())
# c = (a ** 2 + b ** 2) ** (1 / 2)
# print(f'{c:.1f}')

# print(f'{(a ** 2 + b ** 2) ** (1 / 2):.1f}')

#
# c = (a ** 2 + b ** 2) ** (1 / 2)
# print(round(c, 2))

# n, k = map(int, input().split())
# import math
# c = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
# print(int(c))


# n1 = math.factorial(n)
# k1 = math.factorial(k)
# nk = math.factorial(n - k)
#
# print(int(n1 / (k * nk)))

# n, m = map(int, input().split())
# import math
# print(math.ceil((n + m) / 20))

# x = int(input())
#
# print(int( 500 / ( x - (x * 0.1))))

# a = 7
# b = -4
# c = 3
# print(a, b, c, sep="\n")

# s1 = "Hello"
# s2 = "Balakirev"
# print("Hello", end=" ")
# print("Balakirev")

# s1, s2 = map(str.strip, input().split())
#
# print("Word 1:", s1, "|","Word 2:", s2)

# n, m = map(int, input().split())
# print(n ** m)

# q, w = map(float, input().split())
# print(q + w)

# X, Y = map(int, input().split())
# q = print(X + Y + (X * 2) + (Y * 4))

# q = float(input())
# # w = float(input())
# e = 2 * (q + w)
# print(f'{e:.1f}')

# import math
# print(f'{math.pi:.3f}')

# q = float(input())
# print("Вы ввели число ", q)

# q = abs(int(float(input()))) % 3 == 0
# print(q)

# import math
# q = float(input())
# w = round(q)
# print(w)
# e = w > q
# print(e)

# a, b = map(int, input().split())
# print(0 == a % b)

# a, b, c = map(int, input().split())
# print(a < (b + c) and b < (a + c) and c < (b + a))

# 8. String
# s1 = str(input())
# s2 = str(input())
# print(s1 + ' ' + s2)

# q = str(input())
# w = str(input())
#
# print((q + ' ') * 2 + (w + ' ') * 3, sep = ' ')


# q, w = map(str, input().split())
# 12.8 print((q + ' ') * 2 + (w + ' ') * 3, sep = ' ')

# 12.9  print("Переменная a =",a + ", переменная b =", b)

# 2.10 q = str(input())
# w = len(q)
# print("Строка:",q + ". Длина:",w )

# q, w = map(str, input().split())
# e = q in w
# r = q == w
# t = q > w
# y = q < w
# print(e, r, t, y)

# q, w = map(str, input().split())
# e = ord(q)
# r = ord(w)
# t = ', '
# print("Коды: ", q + ' = ', e, t, w + ' = ', r, sep='')

# q = str(input())
# w = q[0]
# e = q[-1]
# print(str(w + e))

# q = str(input())
# print(q[:4])

# q = str(input())
# print(q[-3:])

# q = str(input())
# print(q[1::2])

# q = str(input())
# e = str(input())
# print(q[::2] + " " + e[1::2])


# text = str(input())
# text_1 = text[:5]
# print(text_1[::-1])

# 3.2.10 q, w = map(str, input().split())
# e = int(len(q))
# print(w[:e])

# q, w = map(str, input().split())
# e = int(len(w))
# r = q[:e]
# t = r[1::2]
# y = w[1::2]
# print(t)
# print(y)
# print(t == y)

# msg = 'abracadabra'
# msg.count('ra')
# 2
# msg.count('ra', 4)
# 1
# msg.count('ra', 4, 10)
# 0
# msg.count('ra', 4, 11)
# 1
# msg.find('br')
# 1
# msg
# 'abracadabra'
# msg.find('br', 2)
# 8
# msg.find('brr', 2)
# -1
# msg.find('br', 2)
# 8
# msg.rfind('br', 2)
# 8
# msg.index('brr')
# Traceback (most recent call last):
#   File "C:\PyCharm 2023.1\plugins\python\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# ValueError: substring not found

# msg
# 'abracadabra'
# msg.replace('a', 'o')
# 'obrocodobro'
# msg.replace('ab', 'AB')
# 'ABracadABra'
# msg.replace('ab', '')
# 'racadra'
# msg.replace('a', 'o', 3)
# 'obrocodabra'
# msg.isalpha()
# True
# msg
# 'abracadabra'
# "hello world".isalpha()
# False
# '5.6'.isdigit()
# False
# '56'.isdigit()
# True














