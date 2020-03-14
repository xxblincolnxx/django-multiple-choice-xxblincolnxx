import datetime
from django.forms import ModelForm
from .models import Card, FigureCard, TextCard, Deck
from django.utils.translation import ugettext_lazy as _


class FigureCardForm(ModelForm):
    class Meta:
        model = FigureCard
        fields = ('title', 'subject', 'raw_image', 'answer', 'decks')
        labels = {
            'title': _('Title:'),
            'subject': _('Subject:'),
            'raw_image':_('Image:'),
            'answer': _('Answer'),
            'decks': _('Associated Decks:')
        }


class TextCardForm(ModelForm):
    class Meta:
        model = TextCard
        fields = ('title', 'subject', 'question', 'answer', 'decks')
        lables = {
            'title': _('Title:'),
            'subject': _('Subject:'),
            'question':_('Question:'),
            'answer': _('Answer:'),
            'decks': _('Associated Decks:')
        }
