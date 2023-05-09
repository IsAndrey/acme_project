from django.urls import path
from . import views

app_name = 'birthday'

urlpatterns = [
    path('', views.birthday, name='create'),
    path('new/', views.BirthdayCreateView.as_view(), name='new_create'),
    path('list/', views.birthday_list, name='list'),
    path('new/list/', views.BirthdayListView.as_view(), name='new_list'),
    path('<int:pk>/edit/', views.birthday, name='edit'),
    path('<int:pk>/delete/', views.birthday_delete, name='delete'),
    path('new/<int:pk>/', views.BirthdayDetailView.as_view(), name='new_detail'),
    path('new/<int:pk>/edit/', views.BirthdayUpdateView.as_view(), name='new_edit'),
    path('new/<int:pk>/delete/', views.BirthdayDeleteView.as_view(), name='new_delete')
]
