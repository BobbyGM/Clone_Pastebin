from django.urls import path
from .views import CreatePasteView, DisplayPasteView, UpdatePasteView, DeletePasteView, SearchResultsView

app_name = 'pastes'

urlpatterns = [
    path('create/', CreatePasteView.as_view(), name='create'),
    path('display/<slug>', DisplayPasteView.as_view(), name='display'),
    path('update/<slug>', UpdatePasteView.as_view(), name='update'),
    path('delete/<slug>', DeletePasteView.as_view(), name='delete'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
]