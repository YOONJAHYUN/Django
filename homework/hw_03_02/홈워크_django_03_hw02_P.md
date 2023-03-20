- 데일리 과제 3-2에서 작성한 모델 Article 모델을 참고하여 작성하시오.

- 설계도 생성
```bash
$ python manage.py makemigrations
```

- table 생성
```bash
$ python manage.py migrate
```

- 레코드 생성
```bash
# article instance를 생성해서 레코드 생성
article = Article()
article.title = '제목'
article.content = '내용'
article.save()
```
