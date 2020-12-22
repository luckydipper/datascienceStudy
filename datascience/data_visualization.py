# AIM 1.exploration, 2.communication
# 막대 그래프 히스토그램 선그래프 산점도
import matplotlib.pyplot as plt
from typing import List, get_args
Vector = List[float]


def graph():
    year = [2019, 2020, 2021, 2022]
    gdp = [300.2, 456.2, 162.3, 551.4]

    plt.plot(year, gdp, color='green', marker='o', linestyle='solid')
    plt.title("Nominal GDP")
    plt.show()


def add_vector(v1: Vector, v2: Vector) -> Vector:
    assert len(v1) == len(v2), "Vector should be same demension"
    return [vec1+vec2
            for vec1, vec2 in zip(v1, v2)]

def linear_alegebra():
    #linear alegbra 중에서 네트워크를 나타낼 수 있음. 나머진 아는거.
    return None

def main():
    graph()
    hight_weight_age = [70, 170, 40, 56]
    grade = [95, 80, 75, 62]
    print(add_vector(hight_weight_age, grade))


if __name__ == "__main__":
    main()
