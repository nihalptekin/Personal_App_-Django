from django.urls import path,include
from .views import PersonnelView,DepartmentView

urlpatterns = [
    path('department/',DepartmentView.as_view()),
    path('personnel/',PersonnelView.as_view()),
    # path('profile/<int:pk>',ProfileUpdateView.as_view()),
  
]