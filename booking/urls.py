from django.urls import path
from . import views

app_name="book"
urlpatterns = [
    #http://localhost:8000/book
    path('',views.index,name="index"),
    path('create/',views.create,name="create"),
    path('update/<int:id>',views.update,name="update"),
    path('delete/<int:id>',views.delete,name="delete")
]