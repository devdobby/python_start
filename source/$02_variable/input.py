# x = None
# x = input('숫자 입력하쇼 : ')
# print(x)
# print(type(x))
# print(int(x))

# 한 번의 입력으로 여러 개 저장. split
x, y, z = input('정수 세 개 입력 : ').split()
# 근데 이게 맞는겨? 코드가 더러운데
print('x+y+z = ' + str(int(x)+int(y)+int(z)))