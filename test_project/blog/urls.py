from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='blog-home'),
    path('about/',views.about,name='blog-about'),
    path('display/',views.display,name='blog-display'),
    path('display/Print/',views.Print,name='blog-print'),
	
]   