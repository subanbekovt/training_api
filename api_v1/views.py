import json
from http import HTTPStatus

from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse, HttpResponse, HttpResponseNotAllowed


def add_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        a = int(data['a'])
        b = int(data['b'])
        value = a + b
        return JsonResponse(
            {
                "value": value,
            },
            status=HTTPStatus.CREATED
        )

    return HttpResponseNotAllowed(["GET", "POST"])