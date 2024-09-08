from django.urls import path

from . import views

urlpatterns = [
    path('login/',views.login_page, name="login_page"),
    path('register/',views.register_page, name="register_page"),
    path('logout/',views.logout_page,name="logout_page"),

    path('',views.index, name="index"),
    path('addtask/',views.addTask, name="addTask"),
    path('tasklist/<filter>',views.taskList, name="taskList"),
    path('taskDetails/<int:task_id>/',views.taskDetails,name="taskDetails"),
    path('update_task/<int:task_id>/',views.update_task,name="update_task"),
    path('delete_task/<int:task_id>/',views.del_task,name="del_task"),

]
