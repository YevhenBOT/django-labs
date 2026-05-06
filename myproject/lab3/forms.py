from django import forms
from .models import Review, Subscriber

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user_name', 'score', 'comment']
        widgets = {
            'score': forms.NumberInput(attrs={'min': 1, 'max': 5, 'class': 'form-control'}),
            'comment': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'user_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'Введіть ваш Email', 'class': 'form-control'}),
        }