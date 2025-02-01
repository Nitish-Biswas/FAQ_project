from django.urls import path
from .views import FAQList

urlpatterns = [
    path('api/faqs/', FAQList.as_view(), name='faq-list'),
]