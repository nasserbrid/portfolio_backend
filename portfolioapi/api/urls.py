from django.urls import path
from .views import ServiceListView, ServiceCreateView, ProjectListView, ProjectCreateView, ProjectDetailView, ContactCreateView

urlpatterns = [
    path('services/', ServiceListView.as_view(), name='services-list'),
    path('services/create/', ServiceCreateView.as_view(), name='services-create'),
    path('projets/', ProjectListView.as_view(), name='projects-list'),
    path('projects/create/', ProjectCreateView.as_view(), name='projects-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='projects-detail'),
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
    
]
