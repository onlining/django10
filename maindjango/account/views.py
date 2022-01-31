from django.shortcuts import render,redirect
from argon2 import PasswordHasher
from .models import User
from django.db import transaction
from .forms import RegisterForm

def signup(request):
    register_form=RegisterForm()
    #지금까지작성한 RegsiterForm을 가져옵니다
    context={'forms': register_form}
    #아무런 값도 입력하지 않은 빈폼을 register_form이라는 변수에 할당합니다.context변수에 dict타입으로 register_form객체를 넣습니다.
    if request.method =='GET':
        return render(request, 'account/signup.html' , context)
        #렌더링함수에 context를 전달합니다. 이 과정을 통해 render함수는 accounts/sign.html 파일을 렌더링할때 context에 대한 정보도 같이 전달하게 됩니다
    elif request.method =='POST':
        register_form=RegisterForm(request.POST)
        if register_form.is_valid():
            user=User(
                user_id=register_form.user_id,
                user_pw=register_form.user_pw,
                user_name=register_form.user_name,
                user_email =register_form.user_email
            )
            user.save()
            return redirect('pagedjango/index.html')
        else:
            context['forms']=register_form
            if register_form.errors:
                for value in register_form.errors.values():
                    context['error']=value
        return render(request, 'account/signup.html',context)