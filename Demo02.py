i = 0
while i < 5:
    print("当前是第%d次执行循环" % (i + 1))
    print("i=%d" % i)
    i += 1

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("* ", end='')
        j += 1
    print()
    i += 1

i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d*%d=%-2d " % (j, i, i * j), end='')
        j += 1
    print()
    i += 1

name = 'laoyan'
for x in name:
    print(x + " ", end="")

name = 'yanGe'
for x in name:
    print('----')
    if x == 'n':
        break
    print(x)

i = 0
while i < 10:
    i = i + 1
    print('----')
    if i == 5:
        break
    print(i)

mystr = 'hello world bigdata and bigdataNiu'
print(mystr.split(" ",2))

print(mystr.partition('bigdata2'))