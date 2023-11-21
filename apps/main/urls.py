from django.urls import path
from .views import TodoView, EditView, DeleteView

urlpatterns = [
    path('', TodoView.as_view(), name='home'),
    path('task/<int:pk>/', EditView.as_view(), name='edit'),
    path('task/delete/<int:pk>/', DeleteView.as_view(), name='delete')
]
