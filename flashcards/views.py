from django.shortcuts import render
from rest_framework import viewsets
from .models import Card
from .serializers import CardSerializer


class CardView(viewsets.ModelViewSet):
    """
    Handles routing for POST, PATCH, GET, DELETE, etc.
    """
    queryset = Card.objects.all()
    serializer_class = CardSerializer
