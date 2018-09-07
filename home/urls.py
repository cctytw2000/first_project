from django.urls import path
from . import views

app_name="home"
urlpatterns = [
    #http://localhost:8000/product
    path('',views.index,name="index"),

]
