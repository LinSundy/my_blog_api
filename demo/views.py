from rest_framework.views import APIView
from django.http import HttpResponse


# Create your views here.
class LoginView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hello')


def hello(request):
    return HttpResponse('hello')
