from django.urls import path
from firstapp.views import index_login, handledata, index_register, listAllData, index_register, index_logout
from firstapp.api import project


urlpatterns = [
    path('', index_login, name='login'),
    path('handle/', handledata, name='handle'),
    path('list/', listAllData, name='list'),
    path('register/', index_register, name="register"),
    path('logout/', index_logout, name="logout"),
    path('api/project/', project)
]