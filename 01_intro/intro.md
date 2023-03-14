# 가상환경 설정

0. '.gitignore'
-vscode로 생성하기

1. 가상환경 설정
```bash
#파이썬아 모듈 중에 venv 모듈 써서
#venv라는 이름의 폴더에 가상환경을 만들어줘
#python -m venv {folder_name}
$ python -m venv venv
```

- 현재 진행할 프로젝트에서 사용할 환경을 구성하기 위해 만든다.
- 다른 환경, 혹은 해당 프로젝트를 실행하기 위해 필요한 모듈, 패키지
등등을 관리하기 위함이다.

2. 가상 환경 실행
```bash
 $ source venv/scripts/activate
```

git init 한 순간 .gitignore 위치 같이 잡기
.git 있는 최상단 폴더에

<혹시나 gitignore 하기전에 푸시를 해버렷다면..>
1. gitignore 삭제
2. venv (add) 햇엇던 venv 삭제
3. 깃애드커밋
4. 다시 gitignore 만듦

3. pip freeze
- 현재 pip가 관리중인 패키지의 버전을 포함한 내용을 txt로 작성
```bash
$ pip freeze > requirements.txt
```

4. pip install -r requirements.txt
- requirements.txt에 작성해 둔, 패키지 목록을 모두 읽어서 설치
```bash
$ pip install -r requirements.txt
```


django-admin startproject third_pjt . 
# 현재폴더에다 프로젝트 만들기

python manage.py runserver
# 서버