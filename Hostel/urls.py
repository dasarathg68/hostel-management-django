from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.home_view),
   path('Database/',views.index,name='index'),## This url returns the index view 
   path('createnew/',views.create_form_view), ## url returns the create object view
   path('search/',views.search_view) ## url returns the search using mobile number view

]