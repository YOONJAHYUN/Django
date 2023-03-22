from django import forms
from .models import Article
# 이 파일의 이름은 반드시 forms.py 여야 한다? X


# 내가 처음부터 다 만드는게 아니다.
# Model에 대한 정보를 토대로 Form을 생성할 수 있는 class
class ArticleForm(forms.ModelForm):
    # Model에 대한 정보를 토대로
    # Meta? class?
    class Meta:
        # 내가 정의한 class Article을 토대로 Form을 생성
        model = Article
        # Ariticle 클래스에는 field들이 정의 되어있는데
        # field -> table의 각 column을 정의 한것.
        # database에 만들어진 table에 저장할 값들
        # 내 article table에 저장해야하는 값들을 
        # 모두 form으로 만들어야
        fields = '__all__'
