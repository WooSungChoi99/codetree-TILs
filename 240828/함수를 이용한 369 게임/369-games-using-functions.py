#1. a<n<b+1 사이를 도는 코드를 만든다.
#2. 조건에 맞는 숫자를 찾을 때 마다 count에 +1 을 해준다.
    #2-1. 조건1 = 3, 6, 9 중 하나가 있다
    #2-2. 조건2 = 숫자 자체가 3의 배수이다.
#3. count를 출력해준다.


a, b = tuple(map(int, input().split()))

#조건 2
def mult_three(n) :
    return n % 3 == 0

def thr_six_nine(n) :
    while n > 0 :
        if n%10 == 3 or n%10 == 6 or n%10 == 9 :
            return True
        n = n // 10
    return False


def correct_num(a, b) :
    count = 0
    for i in range (a, b+1) :
        if mult_three(i) or thr_six_nine(i) :
            count += 1
    return count


print(correct_num(a, b))