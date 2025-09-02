from django.urls import path
from .import views
urlpatterns = [
    path('signup/',views.signup,name='signup')
    path('login/',views.login,name='login')
    path('admin-dashboard/',views.signup,name='admin_dashboard')
    path('student-dashboard/',views.signup,name='student-dashboard')
    
]
