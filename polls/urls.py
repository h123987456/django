from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    # 首页 http://ip:port/polls/
    path('', views.index, name='index'),
    # 首页 问题列表 /polls/index/
    path('index/', views.index),
    # 问题详情页 ex: /polls/1/
    path('<int:question_id>/', views.detail, name='detail'),
    # 投票结果页  /polls/2/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # 去投票，选项计数加一   /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # 通用视图示例
    path('simple/', views.SimpleView.as_view(), name='simple')
]


# (注意)django1.x路由写法是 正则风格
# from django.conf.urls import url
# urlpatterns = [
#     # /polls/
#     url(r'^$', views.index, name='index'),
#     # /polls/index/
#     url(r'^index$', views.index),
#     # /polls/5/
#     url(r'^(?P<question_id>[0-9]+)/$'),
# ]



# 与flask对比
# @app.route('/')
# def index():
#     pass

# 先引入视图函数
# path()函数定义的路由最终都会在项目启动时加载
# path(路由规则，)