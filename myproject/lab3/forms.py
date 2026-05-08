from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'score', 'comment']
        labels = {
            'user_name': 'Ваше ім’я',
            'score': 'Оцінка (1-5)',
            'comment': 'Ваш відгук'
        }