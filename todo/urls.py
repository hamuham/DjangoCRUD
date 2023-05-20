from django.urls import path, include
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete

urlpatterns = [
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'),
    path('create/', TodoCreate.as_view(), name='create'),
    PATH('delete/<int:pk>', TodoDelete.as_view(), name='delete')
]
