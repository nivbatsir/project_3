from django.urls import path
from . import views

urlpatterns = [
    path('',views.main,name="main-page"),
    path('user/login',views.login_user,name="login"),
    path('user/signup/',views.signup,name="signup"),
    path('user/logout/',views.logout_user,name="logout"),
    path('user/change_details',views.edit_user,name="change-user-details"),
    path('user/user_info',views.show_user,name="user-info"),
    path('manager/login',views.login_manager,name="login-manager")
]