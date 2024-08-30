M, D = tuple(map(int, input().split()))

def last_day_number(M) :
    if M == 2 :
        return 28
    elif M == 4 or M == 6 or M == 9 or M == 11 :
        return 30
    return 31

if judge_day(M, D) :
    if M <= 12 and D <= last_day_number(M) :
        return True
    return False

if judge_day(M, D) :
    print("Yes")
else :
    print("No")


#1. M, D를 올바르게 입력받는데

#M, D = list(map(int, input().split()))

#2. M을 기준으로 D가 정해짐 
#--> M = {1, 3, 5, 7, 8, 10, 12} , D = 31일
#--> M = {4, 6, 9, 11} , D = 30일
#--> M = {2}, D = 28일.

#3. M을 판단하는 함수

# days_31 = [1, 3, 5, 7, 8, 10, 12]
# days_30 = [4, 6, 9, 11]
# days_28 = [2]

# def what_month(Month) :
#     if Month in days_31 :
#         return list(range(1, 32))
#     elif Month in days_30 :
#         return list(range(1, 31))
#     elif Month in days_28 :
#         return list(range(1, 29))
#     else :
#         return "No"

# #4. 최종함수

# def correct_date_2021(M, D) :
#     if what_month(M) == "No":
#         print("No")
#     elif D in what_month(M) :
#         print("Yes")
#     else : 
#         print("No")


# correct_date_2021(M, D)