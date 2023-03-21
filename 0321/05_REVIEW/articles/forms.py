from django import forms
from .models import Article


# 내가 처음부터 다 만드는게 아니다
# 모델에 대한 정보를 토대로 Form을 생성할 수 있는 class
class ArticleForm(forms.ModelForm):

    # Model에 대한 정보를 토대로
    # Meta? class?
    class Meta:
        # 내가 정의한 class Article을 토대로 Form을 생성
        model = Article
        # Article 클래스에는 field들이 정의되어 있는데
        # field -> table의 각 column을 정의한 것
        # database에 만들어진 table에 저장할 값들으ㅡㄹ
        # 모두 form으로 만들어야

        fields = '__all__'