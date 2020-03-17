from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.display,name='Student-display'),    
    path('Print/',views.Print,name='Student-print'),
	
]   