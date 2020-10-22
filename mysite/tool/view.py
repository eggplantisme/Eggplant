from django.shortcuts import render

app_name = 'tool'


def tool(request):
    context = dict()
    context['hello'] = 'Hello World!'
    return render(request, 'tool/tool.html', context)

