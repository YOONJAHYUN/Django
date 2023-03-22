from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout


# Create your views here.
def login(request):

    if request.method =='POST':

        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # Article -> for.save() db에 그 Article 생성
            # AuthenticationsForm -> ModelForm이 아니다. Model에 의한 정보는 없다.
            user = form.get_user()
            # session id 생성
            auth_login(request, user)
            return redirect('articles:index')

    else:   
        form = AuthenticationForm()


    context = {
        'form':form
    }
    return render(request, 'accounts/login.html', context)

# db에서 session 정보를 삭제 하는 행위: db를 변동시키는 요청
# POST 요청
# POST 요청에 대한 응답으로 session 정보 삭제 했으면 내 할일 끝
def logout(request):
    # 게시글 삭제 -> 특정 게시글을 찾아서 그 게시글을 삭제
    # 어떠한 유저의 로그인 정보를 삭제 -> 특정 유저
    if request.method == 'POST':
        auth_logout(request)
    # 다른 부서로 이관시켜준다.
        return redirect('accounts:login')
    