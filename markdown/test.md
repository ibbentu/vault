# 제목1
내용1
## 제목2
내용2
### 제목3
내용3
#### 제목4
##### 제목5
내용5
###### 제목6

**굵은글씨**, __굵은글씨__
*기울임 글씨*, _기울임 글씨_
~~취소선~~
***굵은 기울임 글씨***

- 1
- 2
- 3
    - 1
    - 2
- 1
- 2
- 1
* 1
* 2
+ 1
+ 2
+ 1

1. 순서1
2. 순서2
5. 순서가 틀려도 자동으로 변경

- [링크 이름](https://www.naver.com)
- [제목이 있는 링크](https://www.naver.com, "네이버")
- [참조 링크][ref]
- [ref]: https://www.naver.com "참조: 네이버"

```
c++
std::cout << "Hello" << std::endl;
```
문장 안 `인라인 코드`
`

``` c++
#include <iostream>

int main() 
{
    std::cout << "hello" << std::endl;
    return 0;
}

```

> 인용문.
> 추가.
> - 추가

> 인용문
>> 인용문 중첩1
>>> 인용문 중첩2

|이름 |나이 |번호 |
|--:|:--:|:--|
|홍길동|20|1|
|김철수|30|2|

---
***
___

줄바꿈1
줄바꿈2
줄바꿈3(공백 두개로)  
줄바꿈4(백슬래시로)\
줄바꿈5

- [ ] 체크박스
- [x] 체크박스
- 체크박스가 vscode에서는 미리보기로 지원되지 않음

각주[^1].
[^1]: 각주 내용

<img src="https://avatars.githubusercontent.com/u/240755087?v=4" alt="설명" width="105" height="105">

![제목이 있는 이미지](https://avatars.githubusercontent.com/u/240755087?v=4, "프로필")
![대체 텍스트](https://avatars.githubusercontent.com/u/240755087?v=4)

[![링크가 있는 이미지](https://avatars.githubusercontent.com/u/240755087?v=4, "github 저장소")](https://github.com/ibbentu?tab=repositories)
