from django.urls import path
from composter.views import index

app_name = 'composter'
urlpatterns = [

    path('', index.as_view(), name='index')
]