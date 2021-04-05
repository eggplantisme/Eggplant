from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse
import platform
import os
import urllib, urllib.request
import json


def index(request):
    context = dict()
    # context['hello'] = 'Hello World!'
    return render(request, 'index.html', context)


def image(request):
    context = dict()
    return render(request, 'image.html', context)


def about(request):
    context = dict()
    return render(request, 'about.html', context)


@ensure_csrf_cookie
def music(request):
    if request.method == 'POST':
        if platform.system() == 'Windows':
            music_dir = os.getcwd() + "\\static\\music"
        else:
            music_dir = os.getcwd() + "/static/music"
        return HttpResponse(json.dumps(os.listdir(music_dir)), content_type="application/json")
    elif request.method == 'GET':
        return render(request, 'music.html', dict())


@ensure_csrf_cookie
def talk(request):
    # 看板娘的聊天机器人暂时使用图灵机器人
    if request.method == 'POST':
        data = request.POST
        print(data)
        url = "http://openapi.tuling123.com/openapi/api/v2"
        post_data = {
            "perception": {
                "inputText": {
                    "text": data['info']
                }
            },
            "userInfo": {
                "apiKey": "233162b4566b4a9f9533c8fb8e1ed89f",
                "userId": "443412"
            }
        }
        print(post_data)
        req = urllib.request.Request(url, data=json.dumps(post_data).encode('utf-8'))
        req.add_header('Content-type', 'application/json')
        res = urllib.request.urlopen(req)
        res_str = res.read().decode()
        print(res_str)
        res_json = json.loads(res_str)
        if 'results' in res_json:
            results = res_json['results']
            return HttpResponse(results[0]['values']['text'])


def login_view(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if request.GET.get('from_page') == '':
                return render(request, 'index.html', context=dict())
            else:
                return HttpResponseRedirect(request.GET.get('from_page'))
        else:
            return render(request, 'login.html', {"error": "authenticate failed"})


def register_view(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {"error": "name exists"})
        else:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            if request.GET.get('from_page') == '':
                return render(request, 'index.html', context=dict())
            else:
                return HttpResponseRedirect(request.GET.get('from_page'))


def logout_view(request):
    logout(request)
    # print(request.path)
    if request.path == "/logout/":
        return HttpResponseRedirect(reverse('login'))
    else:
        return HttpResponseRedirect(request.get_full_path())
