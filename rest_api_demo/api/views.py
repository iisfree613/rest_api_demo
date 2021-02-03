from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json


from .models import Book


@require_http_methods(['GET'])
def add_book(request):
    response = {}
    try:
        # book = Book()
        name = request.GET.get("name")
        if name:
            book = Book(name=name,
                    author=request.GET.get("author"))
            book.save()
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = "添加失败，书名不能为空！！！"
            response['error_num'] = 1
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(['GET'])
def show_book(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = "success"
        response["error_num"] = 0
    except Exception as e:
        response['msg'] = str(e)
        response["error_num"] = 1
    return JsonResponse(response)
