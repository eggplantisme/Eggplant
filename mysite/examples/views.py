from django.shortcuts import render


def button(request):
    return render(request, 'examples/button.html', {})


def video_3d(request):
    return render(request, 'examples/3d_video.html', {})


def loading(request):
    return render(request, 'examples/loading.html', {})
