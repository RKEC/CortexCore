from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('idea/', views.IdeaListView.as_view(), name="idea"),
    path('search/', views.IdeaSearchView.as_view(), name='idea_search'),
    path('add/', views.IdeaCreateView.as_view(), name='add_idea'),
    path('idea/update/<int:pk>/', views.IdeaUpdateView.as_view(), name='update_idea'),
    path('delete/<int:pk>/', views.IdeaDeleteView.as_view(), name='delete'),
]