# -*- coding:utf-8 -*-

import re
import time
from WorkLog.Repositories.WorkLogRepository import WorkLogRepository
from WorkLogSystem import settings
from django.http import HttpResponse
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
import json
from django.core import serializers

__author__ = 'JRoger'


def debug(request):
    #path = settings.BASE_DIR
    #path = settings.STATIC_DIRS
    path = settings.STATICFILES_DIRS
    return HttpResponse(path)