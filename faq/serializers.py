from rest_framework import serializers
from .models import FAQ

class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ['id', 'question', 'answer', 'created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        language = self.context.get('language', 'en')
        
        if language != 'en':
            data['question'] = instance.get_translated_field('question', language)
            data['answer'] = instance.get_translated_field('answer', language)
        
        return data