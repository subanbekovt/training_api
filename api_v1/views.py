import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponseNotAllowed


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
            status=HTTPStatus.OK
        )

    return HttpResponseNotAllowed(["GET", "POST"])


def subtract_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        a = int(data['a'])
        b = int(data['b'])
        value = a - b
        return JsonResponse(
            {
                "value": value,
            },
            status=HTTPStatus.CREATED
        )

    return HttpResponseNotAllowed(["GET", "POST"])


def multiply_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        a = int(data['a'])
        b = int(data['b'])
        value = a * b
        return JsonResponse(
            {
                "value": value,
            },
            status=HTTPStatus.CREATED
        )

    return HttpResponseNotAllowed(["GET", "POST"])


def divide_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        a = int(data['a'])
        b = int(data['b'])
        try:
            value = a / b
            return JsonResponse(
                {
                    "value": value,
                },
                status=HTTPStatus.OK
            )
        except ZeroDivisionError as e:
            return JsonResponse(
                {
                    "value": error,
                },
                status=HTTPStatus.BAD_REQUEST
            )

    return HttpResponseNotAllowed(["GET", "POST"])
