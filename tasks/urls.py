from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name="index"),
    path('addtask/',views.addTask, name="addTask"),
    path('tasklist/<filter>',views.taskList, name="taskList"),
    path('taskDetails/<int:id>/',views.taskDetails,name="taskDetails"),
    path('update_task/<int:id>/',views.update_task,name="update_task"),
    path('delete_task/<int:id>/',views.del_task,name="del_task"),

]
