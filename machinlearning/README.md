# tensorflowStudy

## study 1일차

머신러닝은 supervised usupervised로 나뉘고<br>
regression 처럼 출력값이 연속적인 값중 하나일 수 있고,<br>
classification 처럼 출력 값이 구분되는 것일 수 있음.<br>

노드는 operation 행동하는 함수 같은 것이고,<br>
엣지는 tensor로 되서 데이터를 뜻 함<br>
<hr>

 ## study 2일차
 
 좀 더 체계적인 공부를 위해서 책을 빌렸다.<br>
 머신러닝 교과서 with python 엄청 좋은 것 같다. 👍 <br>
 머신 러닝의 종류를 3가지로 나누어서 설명하겠다. 

1. 지도 학습(supervised learning) - 사전에 옳고 그름을 알고 있음.

- labeled data, 직접 feed back, 출력&예측

* 분류(classification) - 불연속 이산적 discrete -> binary(맞거나 틀리거나) 
    * 결정의 경계(decision binary)를 기준으로 나뉨.
    * ex) 개 or 고양이
* 회귀(regression) - 연속
    * 예측변수,설명변수,입력(predict varialbe,explanation variable,input)
    * 반응변수,타깃,출력(respose variable,target,outcome)
    * ex)공부시간 -> 점수
2. 비지도학습(unsupervised learning) - 의미 있는 정보를 추출하기 위해 데이터구조 탐색

- labeled x, feedback x, 데이터의 숨겨진 구조 찾기 -> 고객 관심사로 그룹 나누기

* 군집(cluster)
    * 제일 이해안가... 정보를 조직화하고, 데이터에서 유사관계를 유도.
    * 사전정보 없는 그룹정보를 의미있는 subgroup으로 조직하는 탐색적 분석.
    * 분석 과정에서 어느정도 유사성을 공유하고 다른 클러스터랑은 비슷하지 않은 샘플그룹?
* 차원 축소(dimension reduction)
    * 관측 대상의 측정 지표가 많은 고차원 대상에게 사용
    * 정보를 대부분 유치하면서 더 작은 차원의 부분공간으로 데이터 압축, 특잇값 분해.
    * 잡음(noise) 데이터를 제거하는 전처리 단계에 적용
    * 시각화에 사용 1,2,3차원에 고유공간에 투영해서 산포도(scatter) 히스토그램에 사용.

3. 강화 학습 (reinforce learning)

- 결정과정, 보상 시스템, 연속된 행동을 학습, trial and error

* aim : 환경과 상호작용하여, 시스템(agent)의 성능을 향상시킴
* 보상(reward) : 환경의 현재 상태 정보가 포함해서 agent에 전달함.
* feedback이 보상함수로, label 되어있지 않음.
* 즉시 or 나중에 피드벡을 기초로 보상을 최대화 하는 것을 학습.


4. 머신러닝의 과정
* row에 instance를 ex) 분꽃 1개
* column에 feature attribute를 ex) target label, 꽃받침 길이 data,
X_n ->X의 n열 X^n -> n행

- 평가의 기준 정확도를 정해야함.
- test set과, traingin set을 나눠서
- 하이퍼파라미터 최적화 : 모델 성능을 상세하게 조절. 
- 교차 검증 : 훈련데이터를 훈련세트와 검증세트로 나눠서 일반화 성능 예측

<hr>

## study 3일차
수학적으로 :=는 정의한다는 뜻이다.<br>
퍼셉트론(perceptron)과, 아달린(Adaline)을 배웠다. ㅇㅁㅇ... 너무 어렵다.<br>
오늘은 퍼셉트론만 해도 벅차겠다.<br>

* 퍼셉트론 -> 집가서 필기를 정리해서 찍어서 올려야 겠다.
    * 가중치 w를 계속 수정해 나가는 것임.
    * 에포크(epoch) : 훈련의 반복 횟수

그리고 다른 모듈에 대해서 배운 것도 쓰겠다.

* numpy
    - ndarray가 주요 type이다. [a:b,c:d]를 통해 indexing slicing가능
    - ndarray <= np.array(list), list <= ndarray.tolist()
    - np.arange() => 정수로 된 것 return한다
    - ndarray.shape => 행렬의 (행 갯수,열 갯수)return한다
    - ndarray.reshape => (a,b,c) >>a*b*c의 수가 행렬의 크기(shape값 곱)와 같다. 앞에서 부터 차원이 올라간다.
     a가3차원 b가2차원 c가1차원 높이 행 열로 봐도 될 듯.
    - np.random : 임의의 수를 return하는데 쓰인다.
        - 임의의 수는 np내 함수로 만들어지는데 초기값인 seed가 필요하다. np.random.seed로 초기화가 가능하다. random.random
        - u = np.random.RandomState(seed)로 난수 생성기를 만든다. u.random(size)
         위와 같이 seed를 초기화하면, 코드 전체(global)하게 영향이간다.\
        - np.random.normal(loc=mean평균,roa표준편차,크기) 정규분포에서 크기가 n인 array return

    - 2개의 ndarray를 붇히는 법은 hstack 옆으로, vstack 위아래로.
    - zip으로 2개의 tuple로 묶는다. -> for로 반복 돌릴 수 있다.
    - np.where(ndarray객체를 for로 읽으면서 조건을 넣는다,옳은 경우, 틀린경우) 
     -> 뒤의 2개의 parameter 옳은case와 틀린case는 안 넣어도 됨. 안넣으면 조건의 index값이 나옴

* import pandas as pd
    - DataFrame(ndarray, dictionary, columms=[], index=[])가 main type인 듯
    - dataframe.values
    - pc.csv_read("link"or"directory")
    - loc & iloc loc는 열을 짜를때, loc[,'이름' 가능,step] iloc[:,:] 그냥 index으로만 짜르기
* import matplotlib.pyplot as plt
    - plt machinlearning 파일 참조!

* 아들린(Adalin) - 적응형 선형뉴런
활성화 함수가 연속함수를 이용함! <br>
pi(z) = z = W.T.dot(x) net funtion이 이와같이 선형 funtion임<br>

제곱 오차합, 이것을 미분해서 경사하강법을 씀.

특성화 스케일링의 여러종류 중 표준화를 통해서 데이터의 경사하강법 결과를 향상시킴.<br>

확률적 경사 하강법 : 모든 훈련 샘플에 대해서 누적된 오차합으로 하는 대신에 일부만 사용. <br>
이를 통해 온라인학습도 가능. 

확률적경사하강법과 배치경사 하강법을 적절히 섞어서 미니 배치 학습을 만듬.
그런데 아달린하고, 퍼셉트론의 첫번째 오퍼레이터, 즉 W_0가 update되는 것이 살짝 헷갈림 다시 해봐야 할 것

* 학습률
    학습률을 기반으로 목적 함수를 최적화(최소값,최대값 찾음) 보폭의 느낌임. 학습률이 낮으면, 최소값을 찾는데 여려번 해야하고,
    학습률이 높으면 오차가 증가할 수도 있음.
    