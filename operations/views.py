from django.shortcuts import render

# Create your views here.
def index(request):
    context = {}
    context['title'] = 'OManager'
    context['label'] = 'Hello, operations index'
    return render(request, 'index.html', context)