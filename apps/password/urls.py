#!/usr/bin/env python
# encoding: utf-8
from django.http import HttpResponse
from django.urls import path

from password.views import PwdView

app_name = "pwd"

urlpatterns = [
    path(r'', PwdView.as_view(), name='enter'),

]
