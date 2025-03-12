from django.urls import path
from .views import index, MenuItemsView, SingleMenuItemView

urlpatterns = [
    path('', index, name='index'),
    path('menu/', MenuItemsView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='menu-detail'),
]
