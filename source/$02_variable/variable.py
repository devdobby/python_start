x = 10
y = 'test str'

print(x)
print(y)

print(type(x))
print(type(y))

x,y,z=10,20,30
print(x, y, z)

x=y=z=20
print(x, y, z)

# 변수 삭제하기
del x
# print(x, y, z)

# 빈 변수 생성. None 으로 대문자 신경써서 해야 함. Null 을 뜻함
x = None
print(x, y, z)