print(1,2,3)

# 구분자
print(1,2,3,sep=',')

# 줄바꿈도 sep 로 가능
print(1, 2, 3, sep='\n, ')

# print(1, None, 3, sep=', ', end=';')
# end에 공값 넣어주면 붙여서 써줌
print(1, end='');print(2, end='');print(3, end='')