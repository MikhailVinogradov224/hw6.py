# print('Введите координаты x1')
# x1 = int (input())
# print('Введите координаты x2')
# x2 = int (input())
# print('Введите координаты y1')
# y1 = int (input())
# print('Введите координаты y2')
# y2 = int (input())
# dist = ( (y1 - x1)**2 + (y2 - x2)**2 )**0.5
# print(dist)

print('Введите координаты через пробел')
data = list(map(int,input().split()))
x,y,z,c = data[0],data[1],data[2],data[3],
dist = ( (z - x)**2 + (c - y)**2 )**0.5
print(dist)