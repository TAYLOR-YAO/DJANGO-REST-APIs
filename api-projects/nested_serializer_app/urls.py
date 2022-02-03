from django.urls import path
from nested_serializer_app import views
urlpatterns = [
    path('author/', views.AuthorListView.as_view()),
    path('author/<int:pk>', views.AuthorDetailsView.as_view()),
    path('book/', views.BookListView.as_view()),
    path('book/<int:pk>', views.BookDetailsView.as_view()),
]
