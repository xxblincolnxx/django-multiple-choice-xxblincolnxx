from django.contrib.auth import get_user_model
from django.db import models
from users.models import User
from PIL import Image
from model_utils.managers import InheritanceManager

class Deck(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    # figure_cards = models.ManyToManyField(FigureCard, related_name='decks')
    # text_cards = models.ManyToManyField(TextCard, related_name='decks')

    def __str__(self):
        return f'{self.name}'


class Card(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    objects = InheritanceManager()

    @property
    def type(self):
        if len(FigureCard.objects.all().filter(pk=self.pk)) > 0:
            type = 'Figure'
        elif len(TextCard.objects.all().filter(pk=self.pk)) > 0:
            type = 'Text'
        else:
            type = 'Other'
        return type

    def __str__(self):
        return f'{self.title}'


class FigureCard(Card):
    raw_image = models.FileField(
        upload_to='images', null=True, verbose_name=None)
    card_type = 'Figure'
    decks = models.ManyToManyField(Deck, related_name='figure_cards')
    
    def __str__(self):
        return f'{self.title}'



class TextCard(Card):
    question = models.TextField(blank=True, null=True)
    card_type = 'Text'
    decks = models.ManyToManyField(Deck, related_name='text_cards')

    def __str__(self):
        return f'{self.title}'





