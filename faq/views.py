from rest_framework import viewsets
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from .models import FAQ
from .serializers import FAQSerializer

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    @method_decorator(cache_page(60 * 15))  # Cache for 15 minutes
    def list(self, request, *args, **kwargs):
        language = request.query_params.get('lang', 'en')
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True, context={'language': language})
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        language = request.query_params.get('lang', 'en')
        instance = self.get_object()
        serializer = self.get_serializer(instance, context={'language': language})
        return Response(serializer.data)