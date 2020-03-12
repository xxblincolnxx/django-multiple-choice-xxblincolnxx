import datetime
from django.forms import ModelForm
from .models import Card, FigureCard, TextCard, Deck
from django.utils.translation import ugettext_lazy as _


class FigureCardForm(ModelForm):
    class Meta:
        model = FigureCard
        fields = ('title', 'subject', 'raw_image', 'answer')
        labels = {
            'title': _('Title:'),
            'subject': _('Subject:'),
            'raw_image':_('Image:'),
            'answer': _('Answer')
        }


class TextCardForm(ModelForm):
    class Meta:
        model = TextCard
        fields = ('title', 'subject', 'question', 'answer')
        lables = {
            'title': _('Title:'),
            'subject': _('Subject:'),
            'question':_('Question:'),
            'answer': _('Answer')
        }


