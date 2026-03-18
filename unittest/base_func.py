#홀수 짝수 판별하기 - 주어진 값이 짝수이면 True, 홀수이면 False를 반환하는 함수
#평균 구하기 - 주어진 정수 list내의 값들의 평균을 반환하는 함수
#최댓값 구하기 - 주어진 정수 list내의 최댓값을 반환하는 함수
#최솟값 구하기 - 주어진 정수 list내의 최솟값을 반환하는 함수


def list_TF(num):
    if num % 2 == 0:
        return True
    else :
        return False
    

def list_N(l):
    l_sum = sum(l)
    l_num = l_sum / len(l)
    return l_num

def list_H(l_max):
    l_Hlen = len(l_max)
    for num in l_max:
        if num > l_Hlen:
            l_Hlen = num


def list_L(l_min):
    l_Llen = len(l_min)
    for num in l_Llen:
        if num > len:
            l_Llen = num