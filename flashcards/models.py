from django.contrib.auth import get_user_model
from django.db import models
from users.models import User
from PIL import Image
from model_utils.managers import InheritanceManager


class Card(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    answer = models.CharField(max_length=100, blank=True, null=True)
    subject = models.CharField(max_length=100, blank=True, null=True)
    objects = InheritanceManager()

class FigureCard(Card):
    raw_image = models.FileField(
        upload_to='images', null=True, verbose_name=None)

class TextCard(Card):
    question = models.CharField(max_length=100, blank=True, null=True)

class Deck(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    cards = models.ManyToManyField(Card, related_name='decks')
