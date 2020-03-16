import datetime
from django.forms import ModelForm
from .models import Card, Deck
from django.utils.translation import ugettext_lazy as _

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ('title', 'subject', 'question', 'figure_raw','answer', 'decks')
        labels = {
            'title': _('Title'),
            'subject': _('Subject'),
            'question': _('Question'),
            'figure_raw':_('Image'),
            'answer': _('Answer'),
            'decks': _('Associated Decks')
        }