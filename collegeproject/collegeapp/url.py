from django.contrib import admin
from django.urls import path

from collegeapp import views

urlpatterns = [
    # path('display/',views.display),
    path('doc1/',views.doc1),
    path('status/',views.status,name='status'),
    path('update/<int:p>/',views.update,name='update'),
    path('delete/<int:p>/',views.deleteform,name="delete")
]