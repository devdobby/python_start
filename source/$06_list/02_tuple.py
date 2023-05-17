# 튜플 : 읽기 전용 리스트. 요소 변경, 추가, 삭제 안 됨
a = (11, 22, 33)
print(a)
a = 11, 22, 33, 44  # 괄호로 안 묶어줘도 됨
print(a)

b = 11, True, 3,3, "Test"   # 내가 파이썬을 싫어하는 이유
print(b)

# 요소가 한 개 있는 튜플
c = (3.3)   # 이건 걍 값임
c = 3.3, # 내가 파이썬을 싫어하는 이유
print(c)

# tuple(), range() 활용
d = tuple(range(0, 5))
print(d)

# tuple <-> list
e = list(range(-4, 10, 2))
print(e)
f = tuple(e)
print(f)
g = list(f)
print(g)