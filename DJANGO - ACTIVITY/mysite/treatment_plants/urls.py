from django.urls import path

from . import views

app_name = 'treatment_plants'
urlpatterns = [
 #   path('list_1', views.TreatmentPlantList.as_view(), name='index'),
 #   path('create_1', views.TreatmentPlantCreate.as_view(), name='treatment_plants_form'),
 #   path('list_2', views.TreatmentPlantList2.as_view(), name='index2'),
 #   path('create_2', views.TreatmentPlant2Create.as_view(), name='treatment_plants_form2')

    path('greentech/', views.ActivityView.as_view(), name='greentech_list'),
    path('greentech/create', views.CreateActivityView.as_view(), name='greentech_create'),
    path('greentech/upload', views.UploadCSV, name='greentech_upload'),





#    path('', index.as_view, name='index'),
]