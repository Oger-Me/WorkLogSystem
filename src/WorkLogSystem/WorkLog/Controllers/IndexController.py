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


def index(request):
    t = get_template("Views/Index.html")
    html = t.render(RequestContext(request, {"Title": "个人日志系统 v1.0",
                                             "Path": settings.TEMPLATE_DIRS[0],
                                             "StaticPath": settings.STATICFILES_DIRS[0],
                                             "BaseDir": settings.BASE_DIR}))

    return HttpResponse(html)


def worklog(request):
    if request.method == 'POST':
        if 'act' in request.POST:
            result = process_post_request(request)
            return HttpResponse(result)
        else:
            page_index = request.POST['page']
            page_size = request.POST['rows']
            keyword = None
            if 'keyword' in request.POST:
                keyword = request.POST['keyword']
            repository = WorkLogRepository()
            record = repository.find(int(page_size), int(page_index), keyword)
            users = []
            for user in record[0]:
                _id = ('%s' % user['_id'])
                users.append({
                    "_id": _id,
                    "title": get_value(user, 'title'),
                    "category": get_value(user, 'category'),
                    "content": get_value(user, 'content'),
                    "date": get_value(user, 'date')
                })
            result = {'total': record[1], 'rows': users}
            data = json.dumps(result, ensure_ascii=False)
            response = JsonResponse(result)
            #response["Content-Type"] = "application/json; charset=utf-8;"

            return response
    else:
        response = HttpResponse('非法操作')

        return response


def get_value(user, column_name):
    if column_name in user:
        return user[column_name]
    else:
        return ""


def process_post_request(request):
    act = request.POST["act"]
    title = request.POST["title"]
    category = request.POST["category"]
    content = request.POST["content"]
    date = request.POST["date"]
    creationdate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    repository = WorkLogRepository()

    if act == 'add':
        item = {'title': title, 'category': category, 'content': content, 'date': date, 'creationdate': creationdate}
        try:
            repository.add(item)
            return 1
        except IOError:
            return -1
        finally:
            repository.disconnection()
    elif act == 'modify':
        _id = request.POST["id"]
        item = {'title': title, 'category': category, 'content': content, 'date': date}
        try:
            result = repository.update(_id, item)
            return result
        except IOError:
            return -1
        finally:
            repository.disconnection()
    elif act == 'delete':
        return -1
    else:
        return -1