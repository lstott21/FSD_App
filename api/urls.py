from django.urls import path
from .views import ItemList, CustomLoginView, UpdateItem, DeleteItem, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', ItemList.as_view(), name='main'),
    path('delete/<int:pk>', DeleteItem.as_view(), name='delete'),
    path('update/<int:pk>', UpdateItem.as_view(), name='update'),
    # path('auth/<slug:slug>', UpdateItem.as_view(), name='update'),
]
