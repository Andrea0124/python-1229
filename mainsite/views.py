from django.shortcuts import render, redirect
from django.http import HttpResponse
from mainsite.models import Post, Watch, WatchTW
import random
from datetime import datetime
from mainsite.models import AccessInfo

def homepage(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, "index.html", locals())

def Watchchart(request):
    now = datetime.now()
    hit_count = len(AccessInfo.objects.all())
    return render(request, "Watchchart.html", locals())

def WatchTWchart(request):
    now = datetime.now()
    hit_count = len(AccessInfo.objects.all())
    return render(request, "WatchTWchart.html", locals())

def showpost(request, slug):
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    try:
        post = Post.objects.get(slug=slug)
        return render(request, "post.html", locals())
    except:
        return redirect("/")

def globalviews(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    watchs = Watch.objects.all()
    now = datetime.now()
    return render(request, "globalviews.html", locals())

def showwatch(request, slug):
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    try:
        watch = Watch.objects.get(slug=slug)
        return render(request, "watch.html", locals())
    except:
        return redirect("/")

def ViewsInTaiwan(request):
    rec = AccessInfo()
    rec.save()
    hit_count = len(AccessInfo.objects.all())
    watchTWs = WatchTW.objects.all()
    now = datetime.now()
    return render(request, "ViewsInTaiwan.html", locals())

def showwatchTW(request, slug):
    hit_count = len(AccessInfo.objects.all())
    now = datetime.now()
    try:
        watchTW = WatchTW.objects.get(slug=slug)
        return render(request, "watchTW.html", locals())
    except:
        return redirect("/")