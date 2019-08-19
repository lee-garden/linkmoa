# linkmoa
### Django Project

###### ※링크모아는 멋쟁이 사자처럼 7기 해커톤프로젝트로 코드 리팩토링이 필요합니다.

## Description
- 링크모아는 '서로의 지식을 연결하다' 라는 모토로 대학생들이 힘든 전공 공부 등에 대한 자료를 공유하기 위한 목적으로 만든 커뮤니티 사이트입니다.
- 사이트는 크게 마이페이지, 공유게시판의 두 부분으로 나뉠 수 있습니다.
- 사용자는 마이 페이지에서 '링크를 담고있는 메모'(이하 메모) 를 작성, 수정, 삭제, 디렉토리로 관리, 태깅, 공유 등을 할 수 있습니다.
- 사용자는 공유 게시판에서 메모를 다운로드, 검색, 정렬, 태그클라우드 기능을 사용 할 수 있습니다.
- 해커톤당일 놀이용으로 자유게시판을 만들었으며 게시글 작성, 댓글기능 등을 임시로 추가하였습니다.

#### 링크모아만의 특별한 기능 소개
###### 링크모아는 각각의 URL 들에 들어갈 필요 없이 URL과 키워드만으로 해당 키워드를 포함하는 URL을 필터링 해줍니다.
<img src="https://user-images.githubusercontent.com/41745717/63235505-ac0c6880-c274-11e9-9efe-01c34ac92194.PNG" width="90%"></img>
1. 위 사진은 링크모아의 자유게시판으로 크게 검색창, 컨텐츠 창으로 나뉩니다.
2. 사용자는 URL 리스트에 자신이 저장해놓은 URL 들, 키워드창에 찾고자 하는 키워드를 입력합니다.
<img src="https://user-images.githubusercontent.com/41745717/63235506-add62c00-c274-11e9-8758-8e63d1c5a790.PNG" width="90%"></img>
3. 위와같이 입력을 하고 검색을 하면 JVM 단어를 포함한 URL만을 추출 해 줍니다.
<img src="https://user-images.githubusercontent.com/41745717/63235509-af9fef80-c274-11e9-970f-8815eac846d1.PNG" width="90%"></img>

4. https://github.com/97e57e/linkmoa_chrome_extension 크롬 익스텐션을 통해 더 쉽게 사용가능합니다.

## 기술 
- Front End
~~~
- 아직 SPA에 대한 지식이 부족하여 SPA는 도입하지 못함
- 대부분 Django template과 Jquery 이용
- Bootstrap의 Modal과 Carousel 사용

- 추후 React.js 또는 vue.js 도입 
~~~

- Back End
~~~
- Python Django Framework
- 마이페이지, 공유게시판, 자유게시판, Accounts등 기능 단위로 각각의 앱 작성
- URL 필터링 기능을 위해 urllib 사용
- Tag 기능을 위해 Django-tagging 라이브러리 사용
- 처음에는 헤로쿠 배포를 시도 했으나 헤로쿠에서 tagging의 최신 버전이 잘 안불러와져서 실패.
- 이후 AWS EC2를 이용한 배포 성공

- Nginx Uwsgi와의 연동 필요
~~~

## ToDo
### 크롤링 개선
- 처음엔 URL의 HTML을 BeautifulSoup를 이용해 파싱해여 필요 부분만 추출하여 검색했지만 시간이 오래 걸려 단순 urlopen 으로 방식 변경
- 변경된 방식에서 크롤링 속도 향상했지만 검색결과의 정확도가 떨어짐.
- 따라서 정확도를 위한 알고리즘 개선과 성능 향상을 위해 파이썬 멀티프로세싱을 도입해야할것으로 보임.

### 페이지네이션 개선
- 현재 페이지네이션 기능 중 검색 후 페이지네이션 혹은 게시글 정렬 후 페이지네이션 기능에서 매번 데이터 요청이 너무 많음.
- 더 효율적인 방법을 찾거나 ajax와 같은 비동기 통신을 통해 성능개선 필요

### 클래스형 뷰 도입
- 현재는 뷰의 모든 파트가 함수형 뷰로 작성되어있음.
- 필요에 따라 가독성 향상을 위해 클래스형 뷰에 대해 공부하고 도입 할 예정.

### 코드 리팩토링
- 인덴테이션 맞추기
- 변수명등 정리
- 반복되는 코드 함수화
- 주석 정리
- css파일 분할


## License
The MIT License (MIT)

Copyright (c) 2019 JeongWon Lee

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
