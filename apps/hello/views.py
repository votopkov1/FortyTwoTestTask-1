# -*- coding: utf-8 -*-
from django.core import serializers
from django.http.response import HttpResponse
from django.shortcuts import render
from models import Profile
from models import Requests


def main(request):
    profile = Profile.objects.first()
    context = {'profile': profile}
    return render(request, 'hello/index.html', context)


def request_list(request):
    requests = Requests.objects.all()[:10]
    context = {'requests': requests}
    if request.is_ajax():
        data = serializers.serialize("json", Requests.objects.all()[:10])
        return HttpResponse(data, content_type="application/json")
    return render(request, 'hello/request_list.html', context)
