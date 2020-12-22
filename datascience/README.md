list 내포(list comprehension)랑, dictionary 내포(dictionary comprehension).<br>
lambda x: x+4 ,list.sort(,key = lambda)<br>

dictionary를 이용하면 data를 좀 더 빨리 찾을 수 있다. -> 정형된 데이터를 간단히 나타냄<br>
in 연산자를 통해, key 값을 반환 할 수 있다. get을 통해 오류없이 Value를 가져올 수 있다<br>

* defaultdict
    * 문서의 빈도수를 세는법 -> 없으면, for문으로 돌려서 하면됨. 
    - I think : dictionary에서, key가 없으면 만들어지고, 있으면 value가 영향을 받는다.
    * 이용법 : from collections import defaultdict
* counter 
    * 연속된 값을 defaultdict(int)와 유사한 객체로 변환시켜준다.
