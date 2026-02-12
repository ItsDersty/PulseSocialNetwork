from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request,"pages/index.html")