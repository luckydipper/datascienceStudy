밑바닥부터 시작하는 데이터 사이언스
===================================

"밑바닥부터 시작하는 데이터 사이언스" 2판의 코드 저장소입니다.
파이썬 3.6 이상을 필요로 합니다.

책에 오타나 오류가 있는 경우, [우측의 위키(Wiki)](https://github.com/Insight-book/data-science-from-scratch/wiki/Errata-(2nd-Edition))에 해당 내용을 기록해주시기 바랍니다.

(만약 1판의 코드와 예시를 찾고 계신다면 `first-edition-ko` 폴더를 참고하시기 바랍니다.)

코드를 사용하고 싶다면 레포지토리를 클론한 뒤 다음과 같이 사용할 수 있습니다.

```
In [1]: from scratch.linear_algebra import dot

In [2]: dot([1, 2, 3], [4, 5, 6])
Out[2]: 32
```

위와 같이 라이브러리를 사용하기 위해서는 루트 디렉토리(`scratch` 폴더를 담고 있는 디렉토리)에 위치해야 합니다. 만약 `scratch` 디렉토리 내부에 위치하면 임포트가 동작하지 않습니다.

위의 코드가 곧바로 수행될 수도 있지만 아닐 경우 `PYTHONPATH`에 루트 디렉토리를 추가해줘야 할 수도 있습니다. 만약 리눅스나 맥을 사용하고 있다면 다음과 같은 명령을 활용하면 됩니다.

```
export PYTHONPATH=/이/레포지토리를/추가한/경로
```

(물론 실제 경로를 입력으로 넣어줘야 합니다.)

만약 윈도우에서 수행하고자 한다면 [더 복잡할 수도](https://stackoverflow.com/questions/3701646/how-to-add-to-the-pythonpath-in-windows-so-it-finds-my-modules-packages) 있습니다.


## 책의 목차

1. 들어가기
2. 파이썬 속성강좌
3. [데이터 시각화](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/visualization.py)
4. [선형대수](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/linear_algebra.py)
5. [통계](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/statistics.py)
6. [확률](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/probability.py)
7. [가설과 추론](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/inference.py)
8. [경사 하강법](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/gradient_descent.py)
9. [파이썬으로 데이터 수집하기](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/getting_data.py)
10. [데이터 다루기](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/working_with_data.py)
11. [기계학습](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/machine_learning.py)
12. [k-NN](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/nearest_neighbors.py)
13. [나이브 베이즈](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/naive_bayes.py)
14. [단순 회귀 분석](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/simple_linear_regression.py)
15. [다중 회귀 분석](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/multiple_regression.py)
16. [로지스틱 회귀 분석](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/logistic_regression.py)
17. [의사결정나무](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/decision_trees.py)
18. [신경망](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/neural_networks.py)
19. [딥러닝](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/deep_learning.py)
20. [군집화](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/clustering.py)
21. [자연어 처리](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/nlp.py)
22. [네트워크 분석](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/network_analysis.py)
23. [추천 시스템](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/recommender_systems.py)
24. [데이터베이스와 SQL](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/databases.py)
25. [맵리듀스](https://github.com/insight-book/data-science-from-scratch/blob/master/scratch/mapreduce.py)
26. 데이터 윤리
27. 본격적으로 데이터 과학하기
