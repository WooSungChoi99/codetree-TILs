#윤년이지 않은 조건
#1. 4로 나누어 떨어지지 않는 해
#2. 100으로 나누어 떨어지지만 400으로 나누어 떨어지지 않는 해

y = int(input())

def is_yunyear(year) :
    if year%4!=0 or (year%100==0 and year%400!=0) :
        return False
    return True

if is_yunyear(y) :
    print("true")
else :
    print("false")

















# year = int(input())

# def leap_year(year) : 
#     if year % 4 == 0 :
#         if year % 100 != 0 or year % 400 == 0 :
#             print('true')
#         else :
#             print('false')
#     else :
#         print('false')

# leap_year(year)