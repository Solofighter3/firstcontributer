from list import views
from django.urls import path

urlpatterns = [
        path('',views.Login,name="Login"),
        path('index',views.index,name="index"),
        path('about',views.about,name="about"),
        path('Logout',views.Logout,name="Logout"),
        path('Signup',views.Signup,name="Signup"),
       path('delete_todo/<int:id>',views.delete_todo,name="Delete"),
       path('update_todo/<int:id>',views.update_todo,name="Update"),

     ]
