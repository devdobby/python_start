print(True and False)   # 당연한거고
print(True or False)    # 앞에서 True 라서 걍 True 로 빠져나감
print(False or True)    # 앞에서 False 였지만 뒤가 True 라서 True
print(not False)    # not 은 반대 논리값

# 논리 연산자와 비교 연산자 함께 사용
print(10 == 10 and not 10 > 2)