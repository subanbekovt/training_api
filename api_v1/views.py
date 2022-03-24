import json
from http import HTTPStatus

from django.http import JsonResponse, HttpResponseNotAllowed


def add_view(request):
    if request.method == 'POST':
        a, b = json.loads(request.body).values()
        a, b = int(a), int(b)
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
        a, b = json.loads(request.body).values()
        a, b = int(a), int(b)
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
        a, b = json.loads(request.body).values()
        a, b = int(a), int(b)
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
        a, b = json.loads(request.body).values()
        a, b = int(a), int(b)
        try:
            value = a / b
            return JsonResponse(
                {
                    "value": value,
                },
                status=HTTPStatus.OK
            )
        except ZeroDivisionError as e:
            value = str(e)
            return JsonResponse(
                {
                    "value": value,
                },
                status=HTTPStatus.BAD_REQUEST
            )

    return HttpResponseNotAllowed(["GET", "POST"])
