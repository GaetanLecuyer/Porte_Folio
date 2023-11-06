from django import forms
from .models import Article, Comment
from widget_tweaks.templatetags.widget_tweaks import *

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'featured', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'featured': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment  # Assurez-vous que le modèle Comment est importé
        fields = ['content']  # Ajoutez les champs dont vous avez besoin pour les commentaires
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a comment...'}),
        }
