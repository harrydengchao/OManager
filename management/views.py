# coding:utf-8
from django.shortcuts import render
from django import forms
from django.core.context_processors import csrf
# --------------------------
from management.models import ServerFunCateg

# Create your views here.
def index(request):
    context = {}
    context['title'] = 'OManager'
    context['label'] = 'Hello, management index'
    return render(request, 'index.html', context)

class ServerFunCategForm(forms.Form):
    """docstring for ServerFunCategForm"""
    server_categ_name = forms.CharField(max_length = 60, label = u'服务功能')

def addserverfun(request):
    if request.POST:
        form = ServerFunCategForm(request.POST)
        if form.is_valid():
            submitted = form.cleaned_data['server_categ_name']
            new_record = ServerFunCateg.objects.create(server_categ_name = submitted)
    form = ServerFunCategForm
    context = {}
    context.update(csrf(request))
    all_records = ServerFunCateg.objects.all()
    context['staff'] = all_records
    context['title'] = u"添加服务功能"
    context['form'] = form
    return render(request, 'addserverfun.html', context)

class ServerAppCategForm(object):
    """docstring for ServerAppCategForm"""
    app_categ_name = forms.CharField(max_length = 90, label = u'服务应用')
        

def demo(request):
    return render(request, 'demo.html')