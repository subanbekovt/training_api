from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseNotAllowed


@ensure_csrf_cookie
def get_csrf_token_view(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    return HttpResponseNotAllowed(['GET'])





