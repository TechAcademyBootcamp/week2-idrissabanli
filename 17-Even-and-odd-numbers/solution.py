a = input('A-ni daxil edin: ')
b = input('B-ni daxil edin: ')
c = input('C-ni daxil edin: ')

a = int(a) # 6
b = int(b) # 4
c = int(c) # 5

if abs(a) < 10000 and abs(b) < 10000 and abs(c) < 10000:
    if (a % 2 == 1 or b % 2 == 1 or c % 2 == 1) and (a % 2 == 0 or b % 2 == 0 or c % 2 == 0):
        print('Yes')
    else:
        print('No')
else:
    print('a,b,c mutleq qiymetce 10000-den kicik olmalidir')
