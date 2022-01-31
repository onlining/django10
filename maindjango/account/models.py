from django.db import models

# Create your models here.
class User(models.Model):
    user_id=models.CharField(max_length=32, unique=True, verbose_name="유저 아이디")
    user_pw=models.CharField(max_length=128, verbose_name="유저 비밀번호")
    user_name=models.CharField(max_length=16, unique=True, verbose_name="유저 이름)")
    user_email=models.EmailField(max_length=128, unique=True, verbose_name="유저 이메일")
    user_register_dttm=models.DateTimeField(auto_now_add=True, verbose_name="계정 생성시간")
    
    def __str__(self):
        return self.user_name
    #생성된 객체의 이름을 지정하는 메서드입니다. 이름에서도 알수 있뜻이 str타입을 리턴합니다. 등록해야한다.
    class Meta:
        #db테이블명을 지정해주는 옵션
        db_table="user"
        #테이블명을 지정하는 옵션
        verbose_name="유저"
        #해당테이블의 닉네임
        verbose_name_plural="유저"