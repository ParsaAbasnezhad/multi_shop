from django.urls import path
from .views import HomePageView
from home.views import CategoryListView

app_name = 'home'
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('category/',CategoryListView.as_view(), name='category-list'),
]
