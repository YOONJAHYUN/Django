# 어무해 키우기

---

<커뮤니티 웹 사이트 생성하기>

- 메인 페이지 : 전체 글 목록 확인
- 상세 페이지 : 글 하나의 내용 및 정보 확인
- 글 작성/수정 페이지 : 글 작성 및 수정
- 기능
  - 메인 → 글 상세보기, 글 작성
  - 상세 → 글 삭제, 글 수정, 목록보기
  - 유저 테이블 먼저

---

---

# 1. 장고 프로젝트 환경 설정하기

### 프로젝트 폴더 생성

```bash
$ mkdir Journal_PJT
```

### 프로젝트 폴더에 가상환경 생성 및 활성화

```bash
$ cd Journal_PJT
$ python -m venv venv
$ source ./venv/Scripts/activate
```

- 프로젝트 폴더로 이동한다.
- 파이썬의 `venv` 모듈을 사용하여 venv라는 가상환경을 생성한다.
- (venv)가 뜨면 가상환경 활성화된 상태

### 가상환경에 프로젝트에 필요한 모듈 설치

```bash
$ pip install django==3.2.18
$ pip freeze > requirements.txt
```

- 필요한 모듈을 직접 설치
- 현재 가상환경의 모듈 버전을 업데이트

```bash
$ pip install -r requirements.txt
```

- 다른 컴퓨터에서 프로젝트를 진행했었다면, 기존에 설치된 모듈들을 한꺼번에 설치

### .gitignore 파일 생성하기

[gitignore.io](https://www.toptal.com/developers/gitignore)

- `python` 입력하여 gitignore 파일 생성
- 생성된 파일의 내용을 복사하여 프로젝트 파일에 `.gitignore` 만들고 붙여넣기
- 이렇게 해야 가상환경 등의 불필요한 내용은 git add에서 제외된다.

---

# 2. 장고 프로젝트/애플리케이션 생성

### 장고 프로젝트 생성

```bash
$ django-admin startproject Journal_PJT .
```

- 현재 폴더에 `Journal_PJT` 프로젝트 생성
  - `manage.py` 가 현재 폴더에 바로 생성된다.
  - . 을 찍지 않으면 현재 폴더에 프로젝트와 동명의 폴더가 하나 더 생성되고, 그 폴더 안에 `manage.py` 가 생성된다.

### 장고 프로젝트의 애플리케이션 생성 및 등록하기

```bash
$ python manage.py startapp articles
```

- articles 애플리케이션 생성

![](https://petal-backpack-f24.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F36c754ef-be8e-4c63-b035-4b6d9f4a2751%2F%25ED%2599%2594%25EB%25A9%25B4_%25EC%25BA%25A1%25EC%25B2%2598_2023-03-21_105719.png?id=0b854bd9-d8d4-4be8-b1d5-d4db2318e696&table=block&spaceId=3c719d41-4b60-4bfa-92bf-9c2c30e30c7f&width=1190&userId=&cache=v2)

[settings.py](http://settings.py)

- 프로젝트의 `settings.py` 의 `INSTALLED_APPS` 에 `articles` 등록

### 서버 연결 확인하기

```bash
$ python manage.py runserver
```

![](https://petal-backpack-f24.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F0b1cdae0-718f-494c-a665-d98d7001837d%2FUntitled.png?id=50938b0f-a590-46f5-a1a4-f3e6964ec0f2&table=block&spaceId=3c719d41-4b60-4bfa-92bf-9c2c30e30c7f&width=2000&userId=&cache=v2)

서버 생성 성공 시 결과화면

---

# 3. 기본 세팅하기

### 기본 템플릿 base.html 생성

- 모든 html파일에서 공통적으로 가지는 구조를 한 번만 정의해둔 채로 가져와서 쓴다는 개념

```bash
$ mkdir templates
$ code templates/base.html
```

- templates 폴더 생성 후 해당 폴더 내에 base.html 파일 생성

![](https://petal-backpack-f24.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F62dc2892-4603-467e-8939-59e941b8be67%2F%25ED%2599%2594%25EB%25A9%25B4_%25EC%25BA%25A1%25EC%25B2%2598_2023-03-21_110400.png?id=7acdca0b-54ba-42e9-a55a-1cb7d5c9e2fd&table=block&spaceId=3c719d41-4b60-4bfa-92bf-9c2c30e30c7f&width=2000&userId=&cache=v2)

base.html

- `!` 입력해서 html 기본 구조 잡기
- block 태그 → content입력하여 다른 템플릿에서 내용 입력할 부분 지정해주기
  - title, footer, content1, content2 등 block의 이름은 자유롭게 지정할 수 있다.

![](https://petal-backpack-f24.notion.site/image/https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2F1d503a28-66c1-4270-9f4f-5a35c6e28c43%2F%25ED%2599%2594%25EB%25A9%25B4_%25EC%25BA%25A1%25EC%25B2%2598_2023-03-21_112625.png?id=669cef20-7cbc-4284-9602-c527bbca4275&table=block&spaceId=3c719d41-4b60-4bfa-92bf-9c2c30e30c7f&width=2000&userId=&cache=v2)

[settings.py](http://settings.py)

- 장고가 인식하는 BASE_DIR에 내가 생성한 templates 폴더를 추가해주어야 이 폴더 안에서 html파일을 찾을 수 있다.

### 앱 별로 urls 따로 관리하도록 설정해주기

- 프로젝트의 urls로 관리해주는 것이 기본이지만 애플리케이션이 많아지면 너무 복잡해짐.
- 애플리케이션 별로 자기 url은 자기가 관리하도록 **urls.py를 앱별로 따로 만들어준다.**
- 그러기 위해서는 프로젝트 urls.py에 “xx 앱 url로 들어오면 그건 xx앱의 urls.py에서 처리해줘라.” 하고 지정해줘야한다.

![Journal_PJT > urls.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9150e473-979a-4630-a647-6f8e1aa388c2/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-21_110812.png)

Journal_PJT > [urls.py](http://urls.py)

- 프로젝트의 urls.py에 들어간다.
- include 함수를 import한다.
- path로 ‘articles/’로 시작하는 url이면, articles의 urls.py에서 작업하도록 경로를 지정해준다.

![폴더 구조](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/12c68403-f59d-4fbd-857b-b035a3e419d1/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-21_111532.png)

폴더 구조

- articles 폴더에는 기본적으로 urls.py가 없기 때문에 직접 생성해준다.

---

# 4. 메인 페이지 생성하기

### urls → views → templates 순서로 요청에 따른 응답 정의하기

![articles > urls.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bce2f4c4-9bf4-4f4a-9261-2f79c12a2048/Untitled.png)

articles > [urls.py](http://urls.py)

- path 함수를 import 한다.
- app_name을 지정한다. **app_name 오타나면 서버 실행했을 때 오류난다.**
- urlpatterns에 모든 경로를 정의한다.
  - index/ url로 들어오면, views 모듈의 index함수를 실행한다.
  - 이 경로를 index라고 부른다.

![articles > views.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ff1a1047-1471-44af-9473-854ffa344d8f/Untitled.png)

articles > [views.py](http://views.py)

- index 함수를 정의한다.
  - request가 들어오면, articles 폴더의 index.html을 응답한다.

![articles > templates > articles > index.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f098df19-f4b1-49c8-a0cc-a09058fe2dd5/Untitled.png)

articles > templates > articles > index.html

- articles 폴더 안에 templates 폴더를 생성하고, 그 안에 다시 articles 폴더를 생성한다.
- 가장 하위 articles 폴더에 index.html을 생성한다.
  - `extends` 태그로 base.html을 상속받는다.
  - `block` 태그로 내용을 입력한다.

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2959ee56-6830-4019-971f-d25afa339c74/Untitled.png)

서버 실행 결과

---

# 5. 데이터베이스 테이블, 모델 생성하기

- 사용자에게 웹 페이지 상에서 데이터를 입력받는 경우, 해당 데이터를 DB에 저장해야한다.
- 장고의 [models.py](http://models.py) == 데이터베이스 스키마, 각 클래스 == 테이블
- models모듈의 Model클래스를 상속받아 클래스를 정의한다.
- 내가 models.py에 정의한 Model 클래스대로 데이터베이스의 테이블이 생성된다.

### 모델 클래스 정의하기

![articles > models.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b86a20b4-2157-4c1f-bfb2-30561469862d/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_110431.png)

articles > [models.py](http://models.py)

- models 모듈의 Model 클래스를 상속받아 Article 클래스를 생성한다.
- Article 클래스 안에 title, content, created_at, updated_at 필드를 생성한다.
  - max_length : 입력할 수 있는 최대값을 지정하는 CharField의 속성
  - auto_now_add : 사용자가 입력하는 값이 아니라 **글(Article 클래스의 인스턴스)이 add될 때** 자동으로 현재 날짜와 시각이 저장된다.
  - auto_now : 사용자가 입력하는 값이 아니라 글을 수정했을 때 자동으로 현재 날짜와 시각이 저장된다.

### 생성된 클래스를 실제 DB에 반영하기

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

- 테이블 설계도 생성하기
- 생성한 설계도를 실제 DB에 올리기
- 기존 모델에 변경사항이 있을 때에도 migration 과정을 거쳐야한다.

![db.sqlite3 > Open Database](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/30ea8360-7d23-4032-9f9f-a6580479cf1a/Untitled.png)

db.sqlite3 > Open Database

![SQLITE EXPLORER > db.sqlite3 > articles_article > Show Table](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/95383c69-4a3c-47b9-bca9-e7d4a03d4b00/Untitled.png)

SQLITE EXPLORER > db.sqlite3 > articles_article > Show Table

![테이블 실행창](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d2b7a412-7603-416f-800b-5cbd43856447/Untitled.png)

테이블 실행창

- 아직 사용자로부터 입력받은 데이터가 없기 때문에 빈 테이블을 보여준다.

---

# 6. 관리자 페이지

- 장고는 관리자가 데이터에 쉽게 접근하고 데이터를 조작할 수 있는 관리자 페이지를 제공한다.
- 내가 생성한 모델을 관리자 페이지에 등록해주어야 해당 모델 (테이블) 데이터를 관리자 페이지에서 관리할 수 있다.
- 선택사항) **모델을 생성하면 바로 admin.py에 등록해주기**

### 관리자 계정 생성하기

```bash
$ python manage.py createsuperuser
```

- Username : admin
- Password : pass1234 (임의)

![관리자계정 생성 Bash 창](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04982d94-fcde-46ba-92f3-60e22983dd4a/Untitled.png)

관리자계정 생성 Bash 창

- 관리자 계정 생성 완료

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0f670e59-eb9b-4f24-8fbe-31fdde7d79d7/Untitled.png)

서버 실행 결과

![생성한 superuser 계정으로 로그인한 후](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c247fac3-80da-4727-8fc2-7bb86dfce978/Untitled.png)

생성한 superuser 계정으로 로그인한 후

- /admin/ 으로 들어가면 장고가 제공하는 관리자 페이지를 확인할 수 있다.

### 생성한 모델을 관리자 페이지에 등록하기

![articles > admin.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d1ade068-a26c-46e1-93fa-936c1fe208d9/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_121305.png)

articles > [admin.py](http://admin.py)

- articles의 admin.py에 모델을 등록한다.
  - models에서 Article 클래스를 import한다.

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1fc51eb5-41a2-4de4-8f90-20aaddfc057a/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_121456.png)

서버 실행 결과

- admin 사이트에 articles 애플리케이션의 Articles 모델이 등록된 것을 확인할 수 있다.
- Add, Change 기능을 사용해서 DB를 직접 조작할 수 있다.

---

# 7. 사용자가 입력한 데이터를 DB에 저장하기

- 웹에서 사용자가 데이터를 입력할 수 있는 방법 : form
- 그 중에서 ModelForm은 내가 정의한 모델을 토대로 form을 생성해주기 때문에 보다 쉽게 데이터를 입력받고, DB에 저장할 수 있다.

### 모델 폼 생성하기

- 사용자가 데이터를 입력하는 ‘form’을 forms 모듈의 ModelForm 클래스를 사용하여 쉽게 생성할 수 있다.
- ModelForm을 사용하면 내가 생성한 모델을 토대로 form을 생성해준다.

![articles > forms.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df703cbb-8b0f-44ce-aceb-a8816835e1ad/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_115326.png)

articles > [forms.py](http://forms.py)

- articles 폴더 안에 forms.py를 생성한다.
- 장고에서 forms 모듈을 불러온다.
  - forms 모듈의 ModelForm클래스를 상속받아 ArticleForm을 생성한다.
- 이 ArticleForm에 대한 정보를 Meta 클래스로 정의한다.
  - 내가 정의한 Article 모델을 ArticleForm의 기준으로 한다.
  - Article 모델에 있는 모든 필드를 폼에서 입력받을 값으로 정한다.

### 사용자가 데이터를 입력할 웹 페이지 생성하기

![articles > urls.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e5d185b9-c22c-4aa4-9c0e-3d21e8bd91a5/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_151322.png)

articles > [urls.py](http://urls.py)

- 게시글을 작성하는 create 페이지를 만들기 위해 urls.py에 새로운 create 경로를 만들어준다.

![articles > views.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f1c33e0f-94a3-4260-a0d6-8e1db5c2305b/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_133816.png)

articles > [views.py](http://views.py)

- request의 method에 따라 다르게 처리한다.
  
  - GET인 경우, 내용을 작성하기 위한 빈 폼을 불러온다.
  - POST인 경우, 작성한 내용을 불러오고 해당 내용의 유효성 검사를 한 후, DB에 저장한다. 내용을 DB에 저장한 뒤 다시 메인 페이지를 보여준다. ArticleForm의 첫 번째 인자는 request.POST

- 1. GET요청이 들어왔거나 2) POST요청에서 유효성 검사를 통과하지 못한 경우 폼을 보여준다.
  - GET인 경우, 불러온 빈 폼을 보여준다.
  - POST인 경우, 이때까지 작성한 내용을 보여준다.

![articles > templates > articles > create.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b12a2bb0-a0ed-4d29-b750-8f84a34f9337/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_172657.png)

articles > templates > articles > create.html

- create.html 파일을 생성한다.
- base.html을 상속받고, content 블록안에 내용을 작성한다.
  - 내용을 입력받을 form을 넣어준다. 이때 form의 구조는 forms.py에서 이미 정의되었고, views.py의 create함수에서 context를 통해 받아온 form을 가져오기만 하면 입력창이 만들어진다.
  - 단, 제출 버튼은 form에 없으므로 따로 만들어주기~
- POST요청을 처리할 때는 반드시 crsf_token을 함께 받아서 검증한다.
  - 내가 만든 HTML파일에서 온 요청인지 확인한다.

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1aede100-5a96-4eed-bfce-42a7061e8c22/Untitled.png)

서버 실행 결과

![내용 작성](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e89aacf3-a43a-4d31-8288-cae12b6c93bf/Untitled.png)

내용 작성

![제출 버튼 누른 후](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a61991c4-2f12-4ea0-a099-9b152584614a/Untitled.png)

제출 버튼 누른 후

![화면 캡처 2023-03-22 154841.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/93a25e64-3edd-4939-ba34-e498e0332eca/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_154841.png)

- 데이터베이스의 article 테이블을 실행시키면 웹 페이지에서 입력한 데이터가 DB에 정상적으로 저장된 것을 확인할 수 있다.

### 추가작업 : 사용자 편의를 위한 기능 추가

1. 메인 페이지에 글 작성하기 링크 추가
   
   ![articles > index.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e1142441-af38-4095-b98a-3acf59b449bc/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_160857.png)
   
   articles > index.html
   
   - url 태그를 사용한다.
     - articles 애플리케이션의 create 경로로 이동한다.
     - articles의 urls.py에 정의한 app_name과 path의 name을 활용하여 링크 연결을 간단하게 작성할 수 있다.

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/79d848e4-c1c5-444c-9ce6-4ce0873ba5fa/Untitled.png)

서버 실행 결과

![글 작성하기 클릭 시](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/06d6a35d-4ddf-4ece-a5ea-cae62cd1c1d2/Untitled.png)

글 작성하기 클릭 시

1. 메인 페이지에서 전체 글 목록 확인하기

![articles > views.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7f9fbab8-f001-4cb4-96a9-1b9afd6dd233/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_161421.png)

articles > [views.py](http://views.py)

- articles의 models.py에서 Article 클래스를 불러온다.
- index 함수에서 작업한다.
  - Article 클래스 (DB의 aritcle 테이블) 의 모든 인스턴스를 가져와서 articles 변수에 담는다.
  - context 딕셔너리에 ‘articles’ 키 값에 articles를 값으로 저장한다.
  - 렌더링하여 index.html에 context를 넘겨준다.

![화면 캡처 2023-03-22 162911.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/aed48d6b-a4f9-4657-a0cd-1faecad49c4d/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_162911.png)

- articles에 담긴 값을 차례로 순회하면서 해당 ar 속성들을 보여준다.

![실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6c8da373-19b7-4450-9285-ba3e9db4309a/Untitled.png)

실행 결과

---

# 8. 상세 페이지 만들기

### urls → views → templates 순서로 요청에 따른 응답 정의하기

![articles > urls.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e0998fd7-1bf8-4d35-9323-f641068329fb/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_165302.png)

articles > [urls.py](http://urls.py)

- 모든 게시글에 각각 페이지를 만드는건 에바다.
- variable routing을 사용하여 각 게시글의 상세페이지로 연결한다.
  - url : articles/정수/ → url에서 articles/뒤에 오는 정수를 article_pk 변수에 저장한다.
  - 가변형 라우팅

![articles > views.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2014ac85-da09-45e5-acc5-0ad3b25bf7f0/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_171409.png)

articles > [views.py](http://views.py)

- url을 통해 받은 article_pk를 detail함수의 인자로 받는다.
- Article 클래스에서 pk가 article_pk와 일치하는 인스턴스를 가져와서, article변수에 저장한다.
- context에 담아서 detail.html로 넘긴다.

![articles > templates > articles > detail.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e13db02d-7c16-4273-b36a-e374ae78ac87/Untitled.png)

articles > templates > articles > detail.html

- detail.html을 생성하고, base.html을 상속받는다.
- content 블록에 내용을 작성한다.
  - a태그에 url 태그를 사용하여, 상세 페이지에 메인 페이지 링크를 연결한다.

![서버 실행 화면](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/6dc30293-a8c3-46ee-ac30-7d29c0da71f0/Untitled.png)

서버 실행 화면

### 추가작업 : 사용자 편의를 위한 기능 추가

1. 메인 페이지에서 글 제목을 클릭하면 해당 글의 상세 페이지로 이동하기

![articles > templates > articles > index.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0ab46caf-1535-450e-8f11-847a9f4e6543/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-22_175718.png)

articles > templates > articles > index.html

- index.html에서 제목을 a태그에 담아준다.
  - url 태그를 사용하여 articles의 detail로 연결한다.

![서버 실행 화면](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/92c90041-ca73-4f52-8cec-043c00b27c24/Untitled.png)

서버 실행 화면

---

# 9. 게시글 수정 페이지 생성하기

### urls → views → templates 순서로 요청에 따른 응답 정의하기

![articles > urls.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/593012af-45ea-413f-b7b9-be1af9c0eda1/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_090503.png)

articles > [urls.py](http://urls.py)

- articles/정수/update/ → pk가 정수와 일치하는 게시글의 수정 페이지를 보여준다.

![articles > views.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1f0dd501-b306-4e28-830f-7b62ae73ecb5/Untitled.png)

articles > [views.py](http://views.py)

- Article 클래스의 인스턴스 중, article_pk와 pk가 일치하는 인스턴스 하나를 찾아와서 article 변수에 담는다. : 특정 pk의 게시글을 불러오는 것은 GET이든 POST든 똑같기 때문에 나누지 않고 실행

- request의 method에 따라 다르게 처리한다.
  
  - GET인 경우, ArticleForm 클래스에서 article 인스턴스의 폼을 찾아와서 해당 내용을 보여준다.
  - POST인 경우, 수정한 내용을 불러오고 해당 내용의 유효성 검사를 한 후, DB에 저장한다. 내용을 DB에 저장한 뒤 다시 상세 페이지를 보여준다. ArticleForm의 첫 번째 인자는 request.POST

- 1. GET요청이 들어왔거나 2) POST요청에서 유효성 검사를 통과하지 못한 경우 폼을 보여준다.
  - GET인 경우, 불러온 폼을 보여준다.
  - POST인 경우, 이때까지 수정한 내용을 보여준다.

![articles > templates > articles > update.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ba8140f9-0ae1-4bec-a366-e75e78ab8b57/Untitled.png)

articles > templates > articles > update.html

- update.html 을 생성하고 base.html을 상속받는다.
- create.html과 동일한 구조로 작성한다.

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ddb651b4-f6bc-4002-9ce6-aea63042bf76/Untitled.png)

서버 실행 결과

![수정 성공](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e3654d49-7e07-4913-80f0-58618e958b58/Untitled.png)

수정 성공

### 추가작업 : 사용자 편의를 위한 기능 추가

1. 게시글 상세 페이지에 수정하기 링크 추가하기

![articles > templates > articles > detail.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/0d104e85-482d-422e-9e0a-d608c8ea5d03/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_093050.png)

articles > templates > articles > detail.html

- url 태그를 사용하여 update 경로로 연결한다.

- update 경로는 variable routing을 사용하였기 때문에 특정 article 인스턴스의 pk가 필요하다. 따라서 article.pk를 함께 넣어준다.
  
  - **article_pk가 아니라 article.pk인 이유** : detail.html을 views.py의 detail함수에서 요청과 데이터를 받아온다. detail함수는 article_pk와 pk가 일치하는 Aritcle의 인스턴스 하나를 context에 담아서 detail.html로 보내준다. 따라서 detail.html이 가지고 있는 정보는 article_pk변수가 아닌 article인스턴스에 대한 정보다. 즉, article.pk를 사용하여 article 인스턴스의 pk속성을 받아와 사용하는 것이다.
    
    ![articles > views.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dbf14f2b-bbd8-405c-b03f-eaa6ee47d805/Untitled.png)
    
    articles > [views.py](http://views.py)

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c9e279ee-8467-45cf-90db-3c1022245920/Untitled.png)

서버 실행 결과

---

# 10. DB에서 데이터 삭제하기

- 사용자가 작성한 게시글을 웹 페이지에서 삭제한다.

→ DB의 게시글 테이블에서 해당 게시글을 삭제한다.

### urls → views → templates 순서대로 요청에 대한 응답 처리하기

![articles > urls.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d06a3db8-1e21-46ca-901c-edfb57c7413e/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_094419.png)

articles > [urls.py](http://urls.py)

- urls.py에 delete 경로를 생성한다.

![arrticles > views.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/36d859ff-148b-42bb-94b9-e5e7ab9fb793/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_094808.png)

arrticles > [views.py](http://views.py)

- views.py에 delete 함수를 정의한다.
- Article클래스에서 variable routing으로 받은 article_pk와 pk가 일치하는 인스턴스를 찾아 article 변수에 담는다.
- (요청이 오면) article을 삭제한다.
- 삭제 후 메인 페이지를 보여준다.

![articles > templates > articles > detail.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c4732808-f91e-44f8-8d97-2132f1720a92/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_100313.png)

articles > templates > articles > detail.html

- 게시글 삭제는 따로 페이지가 필요할 것 같진 않다.
- 게시글 상세 페이지에서 바로 삭제할 수 있도록, detail.html에 링크만 추가해준다.

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/88cb40ca-cf2e-4fd7-9f82-f1f6641035c8/Untitled.png)

서버 실행 결과

![삭제 후 메인 페이지 응답](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fd2d830d-f2fc-4f28-b39f-3bf582f4706a/Untitled.png)

삭제 후 메인 페이지 응답

![삭제 후 articles 테이블](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d5c85d83-ac76-4868-ad57-f500f84c3176/Untitled.png)

삭제 후 articles 테이블

- 게시글을 삭제 한 후, DB에서 해당 게시글 데이터가 사라진 것을 확인할 수 있다.

---

# [CRUD 결과 총 정리]

### CREATE

- 게시글 작성

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5a8ccffa-5180-48e1-a21a-eed0e6b33f86/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/22647140-d9d7-47d0-959f-1fefe4baf85f/Untitled.png)

### READ

- 게시글 작성 폼을 조회한다.
- 작성한 게시글을 조회한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/853b2d0c-9f15-418b-a864-a40dc856e67f/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/3f48bdba-9e80-4191-949f-79730424d862/Untitled.png)

### UPDATE

- 작성한 글을 수정한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b9db2a68-91a0-426e-b66f-329a0563591d/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1a88dd32-17ca-4747-9a16-4ed10f4d0feb/Untitled.png)

### DELETE

- 게시글을 삭제한다.

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2e883b70-d9bd-4c07-ae9e-88c4d9146936/Untitled.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ea4be330-1729-480b-b703-fc6bd7646004/Untitled.png)

---

# 11. User 모델 생성하기

### accounts 애플리케이션 생성하기

- startapp명령어로 애플리케이션 생성
- settings.py에 애플리케이션 등록
- 프로젝트 urls.py에 accounts/ 경로 accounts의 urls.py로 넘김
- accounts 폴더에 [urls.py](http://urls.py) 생성하고 app_name 및 urlspattern 정의

### User 모델 생성하기

![accounts > models.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/228b091c-23e0-4794-9497-f07dd49c99b3/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_150821.png)

accounts > [models.py](http://models.py)

- 장고에는 User 모델을 위한 모델 클래스가 따로 있다.
  - Model의 하위 클래스 AbstractUser 클래스
- django.contrib.auth.models에서 AbstractUser 클래스를 import 한다.
- AbstractUser를 상속받아 User 클래스를 생성한다.

### 기본 User 모델을 내가 생성한 Custom User Model로 변경하기

- 장고는 기본적으로 auth_user 테이블을 유저 테이블로 한다.
- 내가 만든 User 모델을 유저 테이블로 사용하기 위해서는 settings.py에 따로 명시해주어야한다.

![setting.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/f2e91364-0416-40cd-83f9-e73c8c0ed5c4/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_151410.png)

[setting.py](http://setting.py)

- settings.py에 `AUTH_USER_MODEL` 을 내가 생성한 accounts의 User클래스로 지정한다.

### 관리자 페이지에 User 모델 등록하기

![화면 캡처 2023-03-23 151804.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a0d5db79-6165-4c07-b6f9-f4e20da3863b/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_151804.png)

- 다른 모델과 달리 인자에 **UserAdmin**을 넣어줘야한다.
  - UserAdmin은 django.contrib.auth.admin 모듈에서 import 할 수 있다.

### migration 초기화

- 기존에 auth_user가 유저 테이블로 설정되어 있기 때문에 이를 초기화한 후, 다시 migrate해주어야 내가 만든 User 모델에 유저 데이터가 정상적으로 저장된다.

![화면 캡처 2023-03-23 152104.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/30533072-eda4-457e-ac67-20b15706c822/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_152104.png)

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bacd8797-d43a-44d1-820c-cd35677afb95/Untitled.png)

- DB를 삭제한다.
- `Alt` 누른 채로 db.sqlite3 우클릭 → Delete Permanently

![화면 캡처 2023-03-23 152829.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/bf846e19-78a2-4cf3-9faf-557ec1b809d8/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_152829.png)

- 모든 애플리케이션의 migrations 지우기
- `__init__` 파일은 지우면 안된다.

### migration하여 DB에 User 모델 반영

![기존의 장고 기본 유저 모델](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5bcb443c-22d2-494a-93e2-909373020e64/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_153304.png)

기존의 장고 기본 유저 모델

![Custom User Model](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/dad9d555-e26f-4eaf-bb71-5957d0f40b0b/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_153704.png)

Custom User Model

- migrate 후, admin 계정 다시 생성해야함

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a4760e67-7bd0-4bb8-afb3-0c83dfa58356/%ED%99%94%EB%A9%B4_%EC%BA%A1%EC%B2%98_2023-03-23_154053.png)

서버 실행 결과

- 관리자 사이트에 accounts 애플리케이션의 Users모델이 생성된 것을 확인할 수 있다.

<aside>
💡 모델명에 왜 s 붙는거? Articles 모델 만들어서 등록해보자 ㅋ

</aside>

---

# 12. 로그인/로그아웃 기능 추가하기

- 로그인 : 세션을 create하는 과정
- 로그아웃 : 클라이언트와 서버 DB에 있는 세션을 delete하는 과정
- 장고의 built-in form을 사용하여 로그인 기능을 구현한다.

### 로그인 기능 구현하기

- 마찬가지로 urls → views → templates 순서로 구현한다.

![accounts > urls.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/1754cfbe-405b-4996-99f2-97fcc1c82181/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2023-03-23_231438.png)

accounts > [urls.py](http://urls.py)

- login 경로를 생성한다.

![accounts > views.py](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b4d70160-f84d-4fbf-bdbe-cecf332620cc/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2023-03-23_231355.png)

accounts > [views.py](http://views.py)

- 기본적으로 create함수와 구조가 같다.
- 로그인은 장고의 built-in form을 사용하므로 따로 forms.py에 정의해줄 필요없이 **AuthenticationForm 클래스를 import해서 바로 사용한다.**
  - 메서드가 POST인 경우는, 일단 내가 로그인 폼에 적은 내용을 받아와야한다. 이 때 원래 create에서는 인자로 `request.POST` 만 받는데, 로그인 폼은 첫 번째 인자로 `request` 를 받아야 한다. 왠진모름;
- 유효성 검사 후, 로그인 처리하는 것도 마찬가지로 장고의 built-in function, **login**을 사용한다. 내가 정의한 login 함수와 이름이 겹치므로 auth_login으로 받아 사용한다.
  - auth_login은 인자로 `request` 와 `form.get_user()` 를 받는다. 기본적으로 요청을 일단 받아야하고, form의 정보를 토대로 user를 get하여 로그인 처리한다는 듯.

![accounts > templates > accounts > login.html](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/76d9bdef-648d-4931-999f-5f70886e55a9/Untitled.png)

accounts > templates > accounts > login.html

- login.html을 생성한다.

<aside>
💡 form의 action? 데이터를 받아올 링크를 지정해주는 것. 안적어주면 현재 페이지에서 받아온다. 그래서 사실상 적으나마나인데 명시성을 위해 작성해준다.

</aside>

![서버 실행 결과](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7990deaa-878c-43f1-979a-d60578648f52/%EC%8A%A4%ED%81%AC%EB%A6%B0%EC%83%B7_2023-03-23_232643.png)

서버 실행 결과

그리고 로그인 해보면?

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/50dc74bf-d065-4868-955b-1513a999d121/Untitled.png)

토큰 안넣음;

- views에 토큰 넣고 다시

---

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a5934120-d925-46cb-b4da-9b0ee176f887/Untitled.png)

- 미디어 파일을 serving해줄 경로
- 실제파일이 저장될인 위치

---

# 권한

`- 사용자 정보 테이블 만들기

1. accounts 어플 생성
2. models.py에 User모델 정의
3. settings에 User 모델 설정
4. migration
