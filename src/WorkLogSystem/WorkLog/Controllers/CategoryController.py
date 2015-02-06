# -*- coding:utf-8 -*-

import re
import time
from WorkLog.Repositories.WorkLogRepository import WorkLogRepository
from WorkLogSystem import settings
from django.http import HttpResponse, JsonResponse
from django.template import RequestContext, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response, render
import json
from django.core import serializers

__author__ = 'JRoger'


def get_category(request):
    categories = [
        {'text': '正常的工作'},
        {'text': '插队的工作'},
        {'text': '提前的工作'},
        {'text': '延期的工作'}
    ]
    category_json = json.dumps(categories, ensure_ascii=False)

    response = HttpResponse(category_json)
    response["Content-Type"] = "application/json"

    return response