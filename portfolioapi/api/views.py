from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import render
from rest_framework import generics, status
from .models import Service, Project, ContactMessage
from .serializers import ServiceSerializer, ProjectSerializer, ContactMessageSerializer
from django.core.mail import send_mail
from rest_framework.response import Response
from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

# Create your views here.
class ServiceCreateView(generics.CreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer



class ServiceListView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer


class ProjectCreateView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    parser_classes = (MultiPartParser, FormParser)

class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    @method_decorator(cache_page(60 * 40))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    
    @method_decorator(cache_page(60 * 40))  
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    

class ContactCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer
    
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
       
        try:
            send_mail(
                subject='Nouveau message de contact',
                message=(
                    f"Nom: {serializer.validated_data['name']}\n"
                    f"Email: {serializer.validated_data['email']}\n"
                    f"Message: {serializer.validated_data['message']}"
                ),
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['nasserbrid@gmail.com'],  
            )
        except Exception as e:
            return Response({"error": "Erreur lors de l'envoi de l'email."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
