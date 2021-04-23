from django.http import HttpResponse
from django.shortcuts import render


# 将请求返回到index.html中
def index(request):
    return render(request, 'index.html')


# 直接返回数据
def hello_world(request):
    return HttpResponse("hello world!!! this is a python web application")


# 页面参数替换
def replace(request):
    """
    # 模板语法：
    变量
    view:{"HTML变量名":"views变量名"}
    HTML:{{变量名}}
    """
    context = {'hello': 'hello world'}
    return render(request, 'replace.html', context)


# 模板语法(列表)
def replace_1(request):
    views_list = ["hello_world_1", "hello_world_2", "hello_world_3"]
    return render(request, "replace.html", {"views_list": views_list})


# 模板语法字典(字典)
def replace_2(request):
    views_dict = {"name": "hello_world"}
    return render(request, "replace.html", {"views_dict": views_dict})


# 过滤器({{变量名 | 过滤器：可选参数}})
def fil(request):
    import datetime
    li = ["akjsdhfkahkdfahkjfhkashfk", 0, 1024, datetime.datetime.now(), "<a href='https://www.runoob.com/'>点击跳转</a>"]
    return render(request, "replace.html", {"li": li})


def condition(request):
    return render(request, 'replace.html', {"condition": 80})


def cycle(request):
    view_list = [1, 2, 3, 4, 5, 6]
    return render(request, "replace.html", {"view_list": view_list})


def cycle_dict(request):
    view_dict = {"name": "小王", "age": 18}
    # view_dict = None
    return render(request, "replace.html", {"view_dict": view_dict})


def if_equal(request):
    user_dict = {"user": 1, "current_user": 1}
    return render(request, "replace.html", user_dict)
