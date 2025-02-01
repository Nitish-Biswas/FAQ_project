# models.py
from django.db import models
from django.conf import settings
from django.core.cache import cache
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField(help_text="Enter the question in English")
    answer = RichTextField(help_text="Format your answer using the editor")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Dynamic translation fields
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['-created_at']

    def __str__(self):
        return self.question[:100]

    def get_translated_field(self, field_name, language):
        """Get translated content with caching"""
        cache_key = f'faq_{self.id}_{field_name}_{language}'
        
        # Check cache first
        cached_value = cache.get(cache_key)
        if cached_value:
            return cached_value

        # Get the translated field if it exists
        translated_field = f'{field_name}_{language}'
        if hasattr(self, translated_field) and getattr(self, translated_field):
            value = getattr(self, translated_field)
        else:
            # Fallback to English and translate
            translator = Translator()
            original_value = getattr(self, field_name)
            try:
                value = translator.translate(original_value, dest=language).text
                # Store the translation
                setattr(self, translated_field, value)
                self.save()
            except Exception:
                value = original_value  # Fallback to English

        # Cache the result
        cache.set(cache_key, value, timeout=86400)  # Cache for 24 hours
        return value

    def save(self, *args, **kwargs):
        """Auto-translate on save if translations are missing"""
        if not self.pk:  # Only on creation
            translator = Translator()
            for lang in ['hi', 'bn']:  # Add more languages as needed
                if not getattr(self, f'question_{lang}'):
                    try:
                        translated = translator.translate(self.question, dest=lang)
                        setattr(self, f'question_{lang}', translated.text)
                    except Exception:
                        continue
                
                if not getattr(self, f'answer_{lang}'):
                    try:
                        translated = translator.translate(self.answer, dest=lang)
                        setattr(self, f'answer_{lang}', translated.text)
                    except Exception:
                        continue

        super().save(*args, **kwargs)