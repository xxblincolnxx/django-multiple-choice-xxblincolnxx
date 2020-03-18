from django.contrib.auth import get_user_model
from django.db import models
from users.models import User
from PIL import Image
from image_cropping import ImageRatioField

class Deck(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

    @property
    def all_cards(self):
        cards = self.cards.all()
        return cards
        


class Card(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    decks = models.ManyToManyField(Deck, related_name='cards',blank=True, null=True )
    figure_raw = models.ImageField(blank=True, null=True)
    cropping = ImageRatioField('figure_raw', '200x400')
    question = models.TextField(blank=True, null=True)


    def __str__(self):
        return f'{self.title}'

    @property
    def all_decks(self):
        decks = self.decks.all()
        return decks

    @property
    def answer_score(self):
        score = 0
        return score

    @property
    def current_frequency(self):
        if score == 0:
            daily_mult = 2
        elif score ==1:
            daily_mult = 1
        elif score ==2:
            daily_mult = 0.5
        else:
            daily_mult = 0.25
        return daily_mult



