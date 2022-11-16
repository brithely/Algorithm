from typing import Iterable
import itertools


def batch_generator(iterable: Iterable, n: int):
    """
    :param iterable: Iterable한 객체
    :param n: 배치 사이즈
    :yield: 모든 iter가 끝날때 까지 반복
    """
    if not isinstance(iterable, Iterable):
        raise TypeError("iterable is Iterable object")
    max_length = len(iterable)
    for ndx in range(0, max_length, n):
        yield iterable[ndx : min(ndx + n, max_length)]


test_list = [i for i in range(1004)]

total_length = len(test_list)
batch_size = 10

for i in range(0, total_length, batch_size):
    print(test_list[i : min(i + batch_size, total_length)])

for batch_list in batch_generator(test_list, batch_size):
    print(batch_list)
