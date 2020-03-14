from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Card, FigureCard, TextCard, Deck
from .forms import FigureCardForm, TextCardForm
from .serializers import CardSerializer, FigureCardSerializer, TextCardSerializer, DeckSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json

class CardView(viewsets.ModelViewSet):
    """
    Handles routing for POST, PATCH, GET, DELETE, etc.
    """
    queryset = Card.objects.select_subclasses()
    serializer_class = CardSerializer


class FigureCardView(viewsets.ModelViewSet):
    queryset = FigureCard.objects.all()
    serializer_class = FigureCardSerializer


class TextCardView(viewsets.ModelViewSet):
    queryset = TextCard.objects.all()
    serializer_class = TextCardSerializer


class DeckView(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer

def homepage(request):
    cards = Card.objects.all()
    decks = Deck.objects.all()
    return render(request, 'flashcards/index.html', {'cards': cards, 'decks': decks})


def new_text_card(request):
    if request.method == "POST":
        form = TextCardForm(request.POST)
        if form.is_valid():
            text = form.save(commit=False)
            text.user = request.user
            text.save()
            return redirect('home')
    else:
        form = TextCardForm()
    return render(request, 'flashcards/new_text_card.html', { 'form': form })

def new_figure_card(request):
    if request.method == "POST":
        form = FigureCardForm(request.POST)
        if form.is_valid():
            fig = form.save(commit=False)
            fig.user = request.user
            fig.save()
            return redirect('home')
    else: 
        form = FigureCardForm()
    return render(request, 'flashcards/new_figure_card.html', { 'form': form })

def take_quiz(request, pk):
    deck = Deck.objects.get(pk=pk)
    return render(request, 'flashcards/take_quiz.html', {'deck': deck})

# @require_POST #POST OR WHATEVER YOURE USING
# @csrf_exempt #IF YOU DONT WANT A CSRF TOKEN
# def json_response_example(request):
#     """
#     used to handle requests for API hits n such
#     """
#     #decode request body
#     data = json.loads(request.body.decode("utf-8"))
#     #find the client
#     client_pk = data.get('clientId')
#     if client_pk is None:
#         return JsonResponse({"status": "error", "message": "clientID is required"})
    
#     client = request.user.clients.filter(pk=client_pk).first()
    
#     #first, check and make sure theres not an open work interval for this user
#     #if no open interval
#         #create a new work interval for user
#     #else
#         #give warning to the user

#     return JsonResponse({"request_data": data})
