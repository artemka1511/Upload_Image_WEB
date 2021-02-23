from django.urls import path
from .views import FileFieldView

urlpatterns = [
    path('', FileFieldView.as_view()),
]