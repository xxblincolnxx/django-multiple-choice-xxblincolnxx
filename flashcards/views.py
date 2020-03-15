from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Card, FigureCard, TextCard, Deck
from .forms import FigureCardForm, TextCardForm
from .serializers import CardSerializer, FigureCardSerializer, TextCardSerializer, DeckSerializer
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from django.views.decorators.http import require_POST
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

@login_required
def homepage(request):
    cards = Card.objects.all().order_by('id').reverse()[:4]
    decks = Deck.objects.all().order_by('id').reverse()[:2]
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

def view_decks (request):
    decks = Deck.objects.all()

    return render(request, 'flashcards/view_decks.html', {'decks': decks })

@csrf_exempt
@require_POST
def new_deck(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = DeckSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status="ok")
        return JsonResponse(serializer.errors, status=400)    


def show_cards(request, pk)


def take_quiz(request, pk):
    deck = Deck.objects.get(pk=pk)
    return render(request, 'flashcards/take_quiz.html', {'deck': deck})

# USE THIS AS TEMPLATE:
# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)