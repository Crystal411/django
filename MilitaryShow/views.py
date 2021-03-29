# Create your views here.

from rest_framework.decorators import api_view
import json
from django.forms.models import model_to_dict
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.shortcuts import render  # 导入render模块
from.models import UserInfo
from.models import KGStore
import military_qa
import showdata

'''-----登录-----'''


@api_view(['POST'])
def Login(request):
    # 对登录信息做校验
    jsonRequest = json.loads(request.body)
    username = jsonRequest['username']
    password = jsonRequest['password']

    if UserInfo.objects.filter(userName=username, password=password).exists():
        info = {
            "status": 200,
            "data": {
                "message": "success",
                "user_id": 1
            }
        }
    else:
        info = {
            "status": 200,
            "data": {
                "message": "failure",
            }
        }
    return JsonResponse(info)


'''----注册----'''


@api_view(['POST'])
def Register(request):
    jsonRequest = json.loads(request.body)
    newName = jsonRequest['username']
    password = jsonRequest['password']

    # 对注册信息进行校正
    if UserInfo.objects.filter(userName=newName).exists():
        info = {
            "status": 200,
            "data": {
                "message": "failure",
            }
        }
    else:
        UserInfo.objects.create(userName=newName, password=password)
        info = {
            "status": 200,
            "data": {
                "message": "success",
            }
        }
    
    return JsonResponse(info)


'''----图谱展示----'''
@api_view(['POST'])
def ShowKG(request):
    print(request.body)
    jsonRequest = json.loads(request.body)
    search = jsonRequest['search']

    # handler = military_qa.MilitaryGraph()
    #
    #
    # result=handler.qa_main(search)
    # print(result)



    kg = KGStore.objects.filter(fromId=search)

    if kg.exists():
        # kg_s=serializers.serialize('json',kg);
        data_list = [{'rel': i.rel, 'toId': i.toId} for i in kg]
        info = {"status": 200, "data": {"message": "success",
                                            "graph": {"fromId": kg[0].fromId, "nodes": data_list}}}
        return JsonResponse(info)
        # return render(request, 'show3.html', {'kgList': json.dumps(kg_s), })
    else:
        info = {
            "status": 200,
            "data": {
                "message": "key is't found"
            }
        }
        return JsonResponse(info)


'''------相关新闻展示------'''
@api_view(['POST'])
def ShowNews(request):
    jsonRequest = json.loads(request.body)
    search = jsonRequest['search']
    # 利用key去数据库中去查找
    handler = military_qa.MilitaryGraph()

    # question = input("用户：").strip()
    result = handler.qa_main(search)
    print(result)


    if 1:
        dataNews = showdata.getlist(search, result)
        # dataNews = [{
        #     "title": search,
        #     "description": result,
        #     "keywords": "共搜索到"+str(len(result))+"个答案",
        #     "origin": "google"
        # },
        # ]

        info = {
            "status": 200,
            "data": {
                "message": "success",
                "list": dataNews
            }
        }
    else:
        info = {
            "status": 200,
            "data": {
                "message": "key is't found"
            }
        }
    
    return JsonResponse(info)

