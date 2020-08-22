from django.urls import path
from . import views

urlpatterns = [
    path('', views.AccountCreate.as_view(), name=views.AccountCreate.name),

    # api/v1/users/<uuid>:
    # Can call GET, PUT, PATCH and DELETE. GET returns a detailed view of the user with primary key <uuid>.
    path('users/', views.UserList.as_view(), name=views.UserList.name),


    # /api/v1/users/<uuid>:
    # Can call GET, PUT, PATCH and DELETE. GET returns a detailed view of the user with primary key <uuid>.
    path('users/<uuid:pk>', views.UserDetail.as_view(), name=views.UserDetail.name),

    path('company', views.CompanyDetail.as_view(), name=views.CompanyDetail.name),
]