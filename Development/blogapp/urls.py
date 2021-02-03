
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('<str:class_name>',views.classsubject),
    path('<str:class_name>/<str:sub_name>',views.subjectquestion),
    path('<str:class_name>/<str:sub_name>/<str:chapter_name>',views.question_list),
    path('<str:classes_name>/<str:sub_name>/<str:chapter_name>/<str:type_name>/<int:id>',views.question),
    path('user-reg/', views.user_reg),
    path('login/', views.login),
    path('logout/',views.logout),

    
    #........ Admin Urls..........
    path('dashboard/', views.dashboard),
    path('user-history/', views.history),
    path('sub-list/', views.subjectresult),
    path('sub-result/<str:class_name>/',views.subjectlist),
    path('sub-result/<str:class_name>/<str:sub_name>/',views.subjectperform),
    path('class-list-improvement/', views.classlistimprove),
    path('sub-list-improvement/<str:class_name>/',views.subjectlistimprovement),
    path('chapter-list-improvement/<str:class_name>/<str:sub_name>/',views.chapter_list_improvement),
    path('improvement/<str:class_name>/<str:sub_name>/<str:chapter_name>/',views.improvement),
    path('edit-profile/', views.edit_profile),
]
