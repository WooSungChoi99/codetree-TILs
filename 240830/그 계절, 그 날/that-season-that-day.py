y, m, d = tuple(map(int, input().split()))

def is_leap_year(y) :
    if y % 4 != 0 :
        return False 
    # 4의 배수만 적용
    elif y % 100 != 0 :
        return True 
    # 4의 배수이면서 100의 배수만 적용
    elif y % 400 == 0 :
        return True
    
    return False

def last_day_number(y, m) :
    if m == 2 :
        if is_leap_year(y) :
            return 29
        else :
            return 28
    elif m == 4 or m == 6 or m == 9 or m == 11 :
        return 30

    return 31


def is_real_date(y, m, d) :
    return d <= last_day_number(y, m) 

def which_season(y, m, d) :
    if is_real_date(y, m, d) :
        if 3 <= m <= 5 :
            return "Spring"
        elif 6 <= m <= 8 :
            return "Summer"
        elif 9 <= m <= 11 :
            return "Fall" 
        else :
            return "Winter"
    else :
        return -1

print(which_season(y, m, d))



# #1. 정수 입력

# Y, M, D = list(map(int, input().split()))

# #2. Y가 윤년인지 아닌지 
# #1. 4로 나뉘고, 2. 100으로 안나뉘고, 3. 100으로 나뉘어도 400으로 나뉘고

# def leap_year (Year) :
#     if Year % 4 == 0:
#         if Year % 100 != 0 or (Year % 100 == 0 and Year % 400 == 0) :
#             return True
#         else : 
#             return False
#     else :
#         return False

# #3. M월 D일이 있는지(계절) 없는지(-1)

# def yes_leap_year (M) :
#     if M == 2 :
#         return 29
#     elif M == 4 or M == 6 or M == 9 or M == 11 :
#         return 30
#     else :
#         return 31

# def no_leap_year (M) :
#     if M == 2 :
#         return 28
#     elif M == 4 or M == 6 or M == 9 or M == 11 :
#         return 30
#     else :
#         return 31

# def yes_leap_date (D)
#     if 1 <= D <= yes_leap_year(M) :
#         return True
#     else : 
#         return False 

# def no_leap_date (D)
#     if 1 <= D <= no_leap_year(M) :
#         return True
#     else : 
#         return False 


# #4. 최종 함수

# def overall_date(Y, M, D) :
#     if leap_year(Y) :
#         if 1 <= D <= yes_leap_year(M) :
#             return True
#         else : 
#             return False 


# 1. 윤년인지 아닌지
# 2. 월/일이 맞는지
# 3. 계절