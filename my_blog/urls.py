

"""定义my_blog的URL模式"""

from django.conf.urls import url

from . import views

urlpatterns = [
      # 主页
      url(r'^$',views.index,name='index'),
      
      # 显示所有的主题
      url(r'^topics/$',views.topics,name='topics'),

      # 显示主题对应的详细页面
      url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),

      # 用于添加新主题的网页
      url(r'^new_topic/$', views.new_topic, name='new_topic'),
      
      # 用于添加新条目的页面
      url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

      # 用于编辑条目的页面
      url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),

      url(r'^file_input/',views.file_input,name="file_input"),
      
      # 代码雨网页
      url(r'^code_wall/',views.codeWall,name="code_wall"),
    
      # 代码雨网页
      url(r'^code_wall2/',views.codeWall2,name="code_wall2"),


]










