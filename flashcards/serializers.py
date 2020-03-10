from rest_framework import serializers
from .models import Card, FigureCard, TextCard, Deck

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class FigureCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FigureCard
        fields = '__all__'

class TextCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextCard
        fields = '__all__'

class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'
