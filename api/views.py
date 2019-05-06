from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import UserInfo, UserToken


def md5(user):
    import hashlib
    import time
    ctime = str(time.time())
    m = hashlib.md5(bytes(user, encoding='utf-8'))
    m.update(bytes(ctime, encoding='utf-8'))
    return m.hexdigest()


# Create your views here.
class LoginView(APIView):

    def post(self, request, *args, **kwargs):
        ret = {'code': 1000, 'msg': None}
        try:
            print(request._request.POST.get(), '22')
            user = request._request.POST.get('username')
            password = request._request.POST.get('password')
            print(user, password, '1')
            obj = UserInfo.objects.filter(username=user, password=password).first()
            if not obj:
                ret['code'] = 1001
                ret['msg'] = "用户名密码错误"
            token = md5(user)
            print(token, 'hah')
            UserToken.objects.update_or_create(user=user, default={'token': token})
        except Exception as e:
            pass

        return JsonResponse(ret)
