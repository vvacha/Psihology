from django.conf.urls import url

from home import views
# from lesson.views import TeamCreate

urlpatterns = [
	url(r'^$', views.HomeView.as_view()),
# 	url(r'teamcreate^$', views.TeamCreate.as_view(), name='TeamCreate'),

]