from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def login(request):
     #데이터베이스를 조작하므로 post
    if request.method == 'POST':
        # 로그인 처리를 해줌 쿠키담아서 응답줘야되자나용
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            # 있으면 유저 나에게 돌려줘
            # 아이디 패스워드 체크, 세션만들고, 쿠키 세션 담기 다한거임
            auth_login(request, form.get_user())
            # 이제 응답해
            return redirect('articles:index')

    else:
        # 비어있는 로그인 페이지를 제공
        form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')