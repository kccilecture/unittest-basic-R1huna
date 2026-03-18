#홀수 짝수 판별하기 - 주어진 값이 짝수이면 True, 홀수이면 False를 반환하는 함수
#평균 구하기 - 주어진 정수 list내의 값들의 평균을 반환하는 함수
#최댓값 구하기 - 주어진 정수 list내의 최댓값을 반환하는 함수
#최솟값 구하기 - 주어진 정수 list내의 최솟값을 반환하는 함수
# TODO: 사용자 모듈 import

from base_func import list_TF, list_N, list_H, list_L

# TODO: 아래의 코드를 삭제하고 unittest를 작성하세요.
# def test_always():
#     assert False, "Remove me!"

def test_list_TF():
    assert True == list_TF(20)
    assert False == list_TF(21)


def test_list_N():
    assert 3 == list_N(l = [1, 2, 3, 4, 5])


def test_list_H():
    assert 5 == list_H(l_max = [1, 2, 3, 4, 5])


def test_list_L():
    assert 1 == list_L(l_min = [1, 2, 3, 4, 5])
