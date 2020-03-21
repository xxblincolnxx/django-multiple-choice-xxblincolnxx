import datetime
from django import forms
from django.forms import ModelForm
from .models import Card, Deck
from django.utils.translation import ugettext_lazy as _

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('title', 'subject', 'question', 'figure_raw','answer', 'decks')
        labels = {
            'title': _(''),
            'subject': _(''),
            'question': _(''),
            'figure_raw':_('Image'),
            'answer': _(''),
            'decks': _('Decks')
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject'}),
            'question': forms.Textarea(attrs={'placeholder': 'Question'}),
            'answer': forms.TextInput(attrs={'placeholder': 'Answer'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = "" 