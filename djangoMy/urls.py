"""djangoMy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from MilitaryShow import views

urlpatterns = [
    url(r'^admin', admin.site.urls),

    #登录界面url
    url(r'^login', views.Login),

    #注册界面url
    url(r'^register',views.Register),

    #查询关键词图谱界面url
    url(r'^graph',views.ShowKG),

    #查询相关新闻界面
    url(r'^key',views.ShowNews),

]
